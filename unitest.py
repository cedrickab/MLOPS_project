import unittest
import requests
from backend import app

def test_end_to_end():
    # Create a test client
    with app.test_client() as client:
        # Make a request to the predict endpoint with sample data
        data = {
            "Anime_Title": "Spirited Away",
            "Anime_Genre": ["Adventure", "Fantasy"],
            "Anime_Description": "In this animated feature by noted Japanese director Hayao Miyazaki, 10-year-old Chihiro (Rumi Hiiragi) and her parents (Takashi Naitô, Yasuko Sawaguchi) stumble upon a seemingly abandoned amusement park.",
            "Anime_Type": "Movie",
            "Anime_Producer": ["Studio Ghibli"],
            "Anime_Studio": ["Studio Ghibli"]
        }
        response = client.post('/predict', json=data)
        assert response.status_code == 200

        # Verify that the predicted rating is between 0 and 10
        prediction = response.json['predictions'][0]
        assert 0 <= prediction <= 10
        
 
class TestApi(unittest.TestCase):

    def test_predict(self):
        # Create a test client
        with app.test_client() as client:
            # define the test data
            data = {
                "Anime_Title": "Naruto",
                "Anime_Genre": ["Action", "Adventure"],
                "Anime_Description": "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the village, the Fourth Hokage, sacrificed his life and sealed the monstrous beast inside the newborn Naruto. Now, Naruto is a hyperactive and knuckle-headed ninja still living in Konohagakure. Shunned because of the Kyuubi inside him, Naruto struggles to find his place in the village, while his burning desire to become the Hokage of Konohagakure leads him not only to some great new friends, but also some deadly foes. ",
                "Anime_Type": "TV",
                "Anime_Producer": ["Aniplex", "Shueisha", "TV Tokyo"],
                "Anime_Studio": ["Studio Pierrot", "TV Tokyo"]
            }

            # send a POST request to the Flask endpoint with the test data
            response = client.post('/predict', json=data)



            # check that the response contains the expected predictions
            expected_predictions = {'predictions': [7.45]}
            self.assertDictEqual(response.json, expected_predictions)







def main():
    # Run the unit tests
    unittest.main()

    # Run the end-to-end test
    test_end_to_end()


if __name__ == '__main__':
    main()
