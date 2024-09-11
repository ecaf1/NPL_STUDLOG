import re

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stops_words = stopwords.words("english")
lemmatizer = WordNetLemmatizer()

def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    tokens = word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stops_words]
    return " ".join(lemmatized_tokens)


def vectorize(model, X_train, X_test):
    results = model.fit_transform(X_train)
    test = model.transform(X_test)
    df_model = pd.DataFrame(results.toarray(), columns=model.get_feature_names_out())
    df_test = pd.DataFrame(test.toarray(), columns=model.get_feature_names_out())
    return df_model, df_test