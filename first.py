import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def read_article(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        article = file.read()

    sentences = sent_tokenize(article)
    processed_sentences = []

    for sentence in sentences:
        cleaned = ''.join([ch if ch.isalpha() or ch.isspace() else ' ' for ch in sentence])
        words = cleaned.split()
        processed_sentences.append(words)

    return sentences, processed_sentences

def generate_summary(file_name, top_n):
    original_sentences, processed_sentences = read_article(file_name)
    stop_words = set(stopwords.words("english"))

    word_frequencies = {}
    for sentence in processed_sentences:
        for word in sentence:
            word = word.lower()
            if word not in stop_words:
                if word in word_frequencies:
                    word_frequencies[word] += 1
                else:
                    word_frequencies[word] = 1

    # Normalize frequencies
    max_freq = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] /= max_freq

    # Score sentences
    sentence_scores = {}
    for idx, sentence in enumerate(processed_sentences):
        score = 0
        for word in sentence:
            word = word.lower()
            if word in word_frequencies:
                score += word_frequencies[word]
        sentence_scores[idx] = score

    # Pick top N scored sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:top_n]

    print("\n--- Summary ---\n")
    for idx in sorted(top_sentences):
        print(original_sentences[idx])

# Example usage
generate_summary("TheGritCity.txt", 4)
