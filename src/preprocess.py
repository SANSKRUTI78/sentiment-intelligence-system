import re

def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"http\S+", "", text)   # remove links
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # remove punctuation/numbers
    text = text.strip()

    return text