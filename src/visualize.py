import matplotlib.pyplot as plt

def plot_sentiment(df):
    counts = df["sentiment"].value_counts()

    plt.figure(figsize=(6,4))
    counts.plot(kind="bar", color=["green", "gray", "red"])
    plt.title("Sentiment Analysis Result")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()