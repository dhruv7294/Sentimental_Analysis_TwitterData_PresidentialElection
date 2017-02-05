import csv
import re
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud, STOPWORDS

f = open("/Users/DS/Documents/DM/project/crookedhillary.csv","rb")
reader = csv.reader(f)

ans = ''
for row in reader:
    line = str(row)         #pre-processing tweets
    line = line.translate(None, '[\'')
    tweet = " ".join([word for word in line.split() if word != 'RT' and not word.startswith('@') ])

    tweet = tweet.split("pic.twitter.com", 1)[0]
    tweet = tweet.split("http", 1)[0]
    tweet = re.sub(r'[^\w]', ' ', tweet)
    stopwords = ['votefortrump', 'trumpforpresident','crookedhillary']
    querywords = tweet.split()
    resultwords = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    result = result.strip()
    if result and not result.isspace():
        ans = ans + " " + result               #pre-processed tweet

wordcloud = WordCloud(   # Created Word-Cloud with removing stopwords and with tweets as input
    stopwords=STOPWORDS,
    background_color='black',
    width=1800,
    height=1400
).generate(ans)

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('./my_twitter_wordcloud_1.png', dpi=300)
plt.show()                #Plotting the word cloud