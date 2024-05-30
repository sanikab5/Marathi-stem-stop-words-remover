#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Creating Marathi stemmer AKSHAR
import streamlit as st
import string
import matplotlib.pyplot as plt

def load_stopwords(stopwords_file):
    with open(stopwords_file, 'r', encoding='utf-8') as f:
        stopwords = set([word.strip() for word in f.readlines()])
    return stopwords

def load_suffixes(suffixes_file):
    with open(suffixes_file, 'r', encoding='utf-8') as f:
        suffixes = set([suffix.strip() for suffix in f.readlines()])
    return suffixes

def remove_suffix(word, suffixes):
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:len(word) - len(suffix)]
    return word

def preprocess_text(text):
    # Remove punctuation symbols
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Convert text to lowercase
    text = text.lower()

    return text

def main():
    st.title("Marathi Stemmer: Akshar")

    # Load stopwords and suffixes
    stopwords_file = "marathi_stopwords.txt"
    suffixes_file = "marathi_suffixes.txt"
    stopwords = load_stopwords(stopwords_file)
    suffixes = load_suffixes(suffixes_file)

    # User Input
    input_text = st.text_area("Enter Marathi Text:", height=200)
    if not input_text:
        st.warning("Please enter some text.")
        return

    # Preprocess the input text
    processed_text = preprocess_text(input_text)

    # Process the input text
    stemmed_words = []
    stopwords_count = 0
    for word in processed_text.split():
        if word in stopwords:
            stopwords_count += 1
        else:
            stemmed_word = remove_suffix(word, suffixes)
            stemmed_words.append(stemmed_word)

    # Create bar graph data
    labels = ['Stopwords', 'Stemmed Words']
    counts = [stopwords_count, len(stemmed_words)]

    # Display Results
    st.subheader("Stemmed Text (without stopwords):")
    if stemmed_words:
        stemmed_text = ' '.join(stemmed_words)
        st.text(stemmed_text)
    else:
        st.info("All words are stopwords.")

    # Display Bar Graph
    st.subheader("Bar Graph - Count of Stopwords and Stemmed Words")
    fig, ax = plt.subplots(figsize=(3, 4)
    bar_color = ['yellow', 'pink', 'yellow']  # Example colors for each bar
    ax.bar(labels, counts, color=bar_color)
    ax.set_ylabel('Count')
    ax.set_title('Count of Stopwords and Stemmed Words')
    st.pyplot(fig)

if __name__ == "__main__":
    main()


# In[ ]:




