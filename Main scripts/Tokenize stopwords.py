from nltk.tokenize import word_tokenize, sent_tokenize

def words(text):
	sents = sent_tokenize(text)
	print(sents)
	words = word_tokenize(text.lower())
	print(words)
	print(stopwords.words('english'))


if __name__ == '__main__':
	text = "The book is a continuation of this article, and it covers end-to-end implementation of neural network projects in areas such as face recognition, sentiment analysis, noise removal etc. Every chapter features a unique neural network architecture, including Convolutional Neural Networks, Long Short-Term Memory Nets and Siamese Neural Networks. If you’re looking to create a strong machine learning portfolio with deep learning projects, do consider getting the book!"
	words(text)