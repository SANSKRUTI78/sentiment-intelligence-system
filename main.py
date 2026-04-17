from src.data_loader import load_data
from src.preprocess import clean_text
from src.sentiment import get_sentiment
from src.visualize import plot_sentiment
from src.wordcloud_gen import generate_wordcloud

print("🚀 Sentiment System Starting...")

df = load_data("data/sample_data.csv")

df["clean_text"] = df["text"].apply(clean_text)
df["sentiment"] = df["clean_text"].apply(get_sentiment)

print(df)

plot_sentiment(df)

generate_wordcloud(df["clean_text"].tolist())