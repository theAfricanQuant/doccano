"""
Preprocessor.
"""
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer

t = MeCab.Tagger('-Owakati')


def tokenize(text):
    """Tokenize Japanese text.

    Args:
        text: Japanese string.

    Returns:
        A list of words.
    """
    return t.parse(text).rstrip().split()


def build_vectorizer():
    return TfidfVectorizer(tokenizer=tokenize)
