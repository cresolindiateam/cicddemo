# tests/test_app.py
import sys


from main import classify_text #Importing classify Function from main.py file
import pickle

def test_classify_text():
    with open("spam_model.pkl", "rb") as f:
        model = pickle.load(f)

    assert classify_text("You've won a prize!", model) == "Spam"
    #Python's assert statement allows you to write sanity checks in your code. 
    #It will pass this statement if is it spam then it will pass otherwise throw error
    
    assert classify_text("Hello, how are you?", model) == "Not Spam"

test_classify_text()

