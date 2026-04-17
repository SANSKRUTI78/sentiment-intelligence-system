from collections import defaultdict

def extract_topics(text):
    text = text.lower()

    topics = {
        "product": ["phone", "laptop", "product", "device"],
        "service": ["service", "support", "help", "response"],
        "delivery": ["delivery", "shipping", "order"],
        "price": ["price", "cost", "expensive", "cheap"]
    }

    found = []

    for topic, keywords in topics.items():
        for word in keywords:
            if word in text:
                found.append(topic)

    return found if found else ["general"]


def topic_sentiment_analysis(df):
    result = defaultdict(lambda: {"Positive": 0, "Negative": 0, "Neutral": 0})

    for _, row in df.iterrows():
        topics = row["topics"]
        sentiment = row["sentiment"]

        for t in topics:
            result[t][sentiment] += 1

    return result