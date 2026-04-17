from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text_list):
    text = " ".join(text_list)

    wc = WordCloud(width=800, height=400, background_color="white").generate(text)

    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()