from flask import Flask, jsonify, request,render_template
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")


# Function to clean text
def clean_text(text):
    text = text.lower().strip()
    text = ' '.join(text.split())
    return text

def json_to_df(json_data):
    # create a dictionary from the json data
    data_dict = {
        'Title': [json_data['Anime_Title']],
        'Genre': [json_data['Anime_Genre']],
        'Synopsis': [json_data['Anime_Description']],
        'Type': [json_data['Anime_Type']],
        'Producer': [json_data['Anime_Producer']],
        'Studio': [json_data['Anime_Studio']]
    }

    # create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data_dict)
    return df

"""
@app.route('/')
def home():
    return render_template('index.html')
"""

@app.route('/predict', methods=['POST'])
def predict():
    # Load the JSON data sent by the client
    data = request.get_json()
    
    # Convert the JSON data to a Pandas DataFrame
    test = json_to_df(data)
    # Clean and preprocess the data
    test['Genre'] = test['Genre'].astype(str).apply(lambda x: clean_text(x))
    test['Producer'] = test['Producer'].astype(str).apply(lambda x: clean_text(x))
    test['Studio'] = test['Studio'].astype(str).apply(lambda x: clean_text(x))

    # Define the MultiLabelBinarizer object
    mlb = MultiLabelBinarizer()

    # Apply the MultiLabelBinarizer to the Genre, Studio, and Producer columns of the dataframe
    new_df2 = pd.concat([test, pd.DataFrame(mlb.fit_transform(test['Genre']), columns=mlb.classes_, index=test.index)], axis=1)
    new_df2 = pd.concat([new_df2, pd.DataFrame(mlb.fit_transform(test['Studio']), columns=mlb.classes_, index=test.index)], axis=1)
    new_df2 = pd.concat([new_df2, pd.DataFrame(mlb.fit_transform(test['Producer']), columns=mlb.classes_, index=test.index)], axis=1)

    # one-hot encode the Type column
    type_df = pd.get_dummies(new_df2['Type'])
    new_df2 = pd.concat([new_df2, type_df], axis=1)

    # Drop the original Genre, Studio, and Producer columns from the dataframe
    new_df2 = new_df2.drop(['Genre', 'Studio', 'Producer', 'Type'], axis=1)

    stopWords = stopwords.words('english')

    # Convert the text data into numerical representations
    vectorizer = TfidfVectorizer(lowercase = False,stop_words = stopWords)

    title_vectors = vectorizer.fit_transform(new_df2["Title"])
    new_df2["Title"] = title_vectors.getnnz(axis=1)

    synopsis_vectors = vectorizer.fit_transform(new_df2["Synopsis"].apply(lambda x: np.str_(x)))
    new_df2["Synopsis"] = synopsis_vectors.getnnz(axis=1)

    # Create a new DataFrame with all the columns and all rows set to 0
    new_X_test = pd.DataFrame(0, index=new_df2.index, columns=np.arange(828))

    # Copy the len of the features from X_test to the first 11 columns of new_X_test
    new_X_test.iloc[:, :len(new_df2.columns)] = new_df2.values

    # Make predictions on the testing set
    y_pred = model.predict(new_X_test)
    rounded = [float(np.round(x,decimals=2)) for x in y_pred]
    # Return the predictions as a JSON object
    return jsonify(predictions=list(rounded))

if __name__ == '__main__':
    app.run(debug=True)
