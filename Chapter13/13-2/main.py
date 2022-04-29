from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib as mpl
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger') # for POS_tag
nltk.download('maxent_ne_chunker') # for NER
nltk.download('words') # for NER
from nltk.tokenize import word_tokenize
mpl.use("pdf")

data = open('dronning.txt', 'r')
content = data.read()
data.close()

#remove empty lines from data
content = content.replace('\n\n', '\n')
print(content)
wordcloud = WordCloud().generate(content)


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('./dronning_with_stop_words.png')


tokens = word_tokenize(content)
tokens = [word.lower() for word in tokens]
# or better
tokens = list(map(str.lower,tokens))


stop_words = set(stopwords.words('danish'))
print(stop_words)
tokens = [w for w in tokens if not w in stop_words]

#add tokens together to one string
tokens = ' '.join(tokens)


wordcloud = WordCloud().generate(tokens)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('./dronning_without_stop_words.png')




