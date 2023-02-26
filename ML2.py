import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
import re
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from nltk.corpus import stopwords
import joblib
import nltk
nltk.download('stopwords')


df = pd.read_csv("C:\\Users\\Arthy\\Desktop\\S9_efrei\\MachineLearninginProduction\\mlops_final_project\\data\\raw_data\\Anime_data.csv",)
df = df.dropna()
df = df[["Title", "Genre", "Synopsis", "Type", "Producer", "Studio","Rating"]]
def clean_text(text):
    # Remove special characters, excluding commas
    text = re.sub(r'[^\w\s,]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove trailing and leading whitespaces
    text = ' '.join(text.strip().split())

    #value of list 
    text = text.split(",")
    text = [x.strip(' ') for x in text]
    
    return text

df['Genre'] = df['Genre'].astype(str).apply(lambda x: clean_text(x))
df['Producer'] = df['Producer'].astype(str).apply(lambda x: clean_text(x))
df['Studio'] = df['Studio'].astype(str).apply(lambda x: clean_text(x))
df.head()

# Get the unique values in the 'Genre' column
unique_genres = set([genre for row in df['Genre'] for genre in row])
unique_Producer = set([Producer for row in df['Producer'] for Producer in row])
unique_Studio = set([Studio for row in df['Studio'] for Studio in row])

# Print the unique genres
print(len(unique_genres))
print(len(unique_Producer))
print(len(unique_Studio))



"""
genre_str=', '.join(unique_genres)
genre_list=genre_str.split(", ")
Studio_str =', '.join(unique_Studio)
Studio_list =Studio_str.split(", ")
Procucer_str = ', '.join(unique_Producer)
Procucer_list =Procucer_str.split(", ")
"""

# Define the MultiLabelBinarizer object
mlb = MultiLabelBinarizer()

# Apply the MultiLabelBinarizer to the Genre, Studio, and Producer columns of the dataframe
new_df = pd.concat([df, pd.DataFrame(mlb.fit_transform(df['Genre']), columns=mlb.classes_, index=df.index)], axis=1)
new_df = pd.concat([df, pd.DataFrame(mlb.fit_transform(df['Studio']), columns=mlb.classes_, index=df.index)], axis=1)
new_df = pd.concat([df, pd.DataFrame(mlb.fit_transform(df['Producer']), columns=mlb.classes_, index=df.index)], axis=1)

# one-hot encode the Type column
type_df = pd.get_dummies(df['Type'])


# Drop the original Genre, Studio, and Producer columns from the dataframe
new_df = new_df.drop(['Genre', 'Studio', 'Producer', 'Type'], axis=1)

new_df.columns

# Convert the text data into numerical representations
stopWords = stopwords.words('english')
vectorizer = TfidfVectorizer(lowercase = False,stop_words = stopWords)
title_vectors = vectorizer.fit_transform(new_df["Title"])
new_df["Title"] = [str (item) for item in new_df["Title"]]
new_df["Title"] = title_vectors.getnnz(axis=1)

synopsis_vectors = vectorizer.fit_transform(new_df["Synopsis"].apply(lambda x: np.str_(x)))
new_df["Synopsis"] = synopsis_vectors.getnnz(axis=1)

X= new_df.drop(columns="Rating")
y= new_df['Rating']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a random forest model with 100 trees
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model on the training set
rf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean squared error: %.2f" % mse)

# Calculate the coefficient of determination
r2 = r2_score(y_test, y_pred)
print("Coefficient of determination (R^2): %.2f" % r2)


# save the model
joblib.dump(rf, "model.pkl")