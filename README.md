

![test](https://github.com/user-attachments/assets/3aa7391d-e768-40e3-941a-081c16a063b8)

# **Spam Email Classifier Using NLP and Machine Learning**
Project Overview
The Spam Email Classifier is a machine learning-based web application designed to classify emails as spam or not spam. Using Natural Language Processing (NLP) techniques and a Naïve Bayes classifier, this project offers an effective solution for identifying spam emails, improving email security and productivity.

The application takes email content as input, applies preprocessing (like stopword removal, lemmatization, and stemming), and uses a pre-trained model to classify the text. The results are displayed in a user-friendly web interface built with Streamlit.

## Features

1. **Spam Classification**: Classify email content as spam or not spam.
2. **User-Friendly Interface**: Built using Streamlit for an intuitive experience.
3. **Efficient NLP**: Includes techniques like stopword removal, lemmatization, stemming, and TF-IDF vectorization.
4. **Pre-trained Model**: Classifier and vectorizer are saved and loaded using Pickle for faster execution.

## How to Run the Project

### 1. Clone the Repository
Clone the project repository to your local machine:

```git clone https://github.com/AmlanPandey/P3-Spam-Email-Classification-using-NLP-and-Machine-Learning.git```

```cd P3-Spam-Email-Classification-using-NLP-and-Machine-Learning```


2. Install Dependencies
Install the required libraries from requirements.txt:
```pip install -r requirements.txt```

3. Run the Project
Now that all dependencies are installed, run the Streamlit app:
```streamlit run spamdect.py```
This will launch the app, and Streamlit will provide a local URL (e.g., http://localhost:8501) where you can view the app in your browser.

Project Components:
1. Data Preprocessing
Removed stopwords and special characters.
Text normalization by converting to lowercase.
Lemmatization and stemming to reduce words to their root forms.
2. Modeling
Trained a Naïve Bayes classifier on the preprocessed email text.
3. Feature Extraction
Used TF-IDF vectorization to convert text into numerical features.
Example Output
Input: "Congratulations! You've won a $1000 gift card. Click here to claim."

Output: ❌ This is a spam email!

Input: "Please find the attached report. Let me know if you have any questions."

Output: ✅ This is NOT a spam email!



