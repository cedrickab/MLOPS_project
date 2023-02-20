# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:41:51 2023

@author: hp
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
import re
from nltk.corpus import stopwords
import joblib


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

rf = joblib.load("model.pkl")


"""
new_data = {
    'Title': ["My Hero Academia Season 4"],
    'Genre': ["Action, Adventure, Superhero"],
    'Synopsis': ["The story follows a young boy named Izuku Midoriya who dreams of becoming a hero in a world where most people possess powers known as Quirks. Despite being born without a Quirk, he is scouted by the world's greatest hero and enrolls in a school for professional heroes."],
    'Type': ["TV"],
    'Producer': ["Funimation, MBS, Dentsu"],
    'Studio': ["Bones, MBS", "Wit Studio, Production I.G"]
}
"""


def predict(new_data):
    test = pd.DataFrame(new_data)
    test.head()
    test['Genre'] = test['Genre'].astype(str).apply(lambda x: clean_text(x))
    test['Producer'] = test['Producer'].astype(str).apply(lambda x: clean_text(x))
    test['Studio'] = test['Studio'].astype(str).apply(lambda x: clean_text(x))

    # Define the MultiLabelBinarizer object
    mlb = MultiLabelBinarizer()

    # Apply the MultiLabelBinarizer to the Genre, Studio, and Producer columns of the dataframe
    new_df2 = pd.concat([test, pd.DataFrame(mlb.fit_transform(test['Genre']), columns=mlb.classes_, index=test.index)], axis=1)
    new_df2 = pd.concat([test, pd.DataFrame(mlb.fit_transform(test['Studio']), columns=mlb.classes_, index=test.index)], axis=1)
    new_df2 = pd.concat([test, pd.DataFrame(mlb.fit_transform(test['Producer']), columns=mlb.classes_, index=test.index)], axis=1)

    # one-hot encode the Type column
    type_df = pd.get_dummies(new_df2['Type'])


    # Drop the original Genre, Studio, and Producer columns from the dataframe
    new_df2 = new_df2.drop(['Genre', 'Studio', 'Producer', 'Type'], axis=1)

    stopWords = stopwords.words('english')

    # Convert the text data into numerical representations
    vectorizer = TfidfVectorizer(lowercase = False,stop_words = stopWords)
    #new_df2 = [str (item) for item in new_df2]

    title_vectors = vectorizer.fit_transform(new_df2["Title"])
    new_df2["Title"] = title_vectors.getnnz(axis=1)

    synopsis_vectors = vectorizer.fit_transform(new_df2["Synopsis"].apply(lambda x: np.str_(x)))
    new_df2["Synopsis"] = synopsis_vectors.getnnz(axis=1)

    len(new_df2.columns)

    new_df2.head()

    new_df2.columns

    # Create a new DataFrame with all the columns and all rows set to 0
    new_X_test = pd.DataFrame(0, index=new_df2.index, columns=np.arange(828))

    # Copy the len of the  features from X_test to the first 11 columns of new_X_test
    new_X_test.iloc[:, :len(new_df2.columns)] = new_df2.values

    # Make predictions on the testing set
    y_pred = rf.predict(new_X_test)

    return y_pred
