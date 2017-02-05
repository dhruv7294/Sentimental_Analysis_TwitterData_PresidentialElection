import csv
import re

f = open("/Users/DS/Documents/DM/project/output_got.csv","rb")              # Reading from the inputfile
reader = csv.reader(f)
fw = open("/Users/DS/Documents/DM/project/voteforhillary.txt","wb")         #writting tweets into text file for backup
data = open("/Users/DS/Documents/DM/project/hillary.csv","wb")              #To Write output into csv file
w = csv.writer(data)

for row in reader:
    flag = False
    line = str(row)
    line = line.translate(None, '[\'')                                      # Removing '[''
    tweet = " ".join([word for word in line.split() if word != 'RT' and not word.startswith('@') ])
    tweet = tweet.split("pic.twitter.com", 1)[0]                            # Removing pic link in tweets
    tweet = tweet.split("http", 1)[0]                                       # Removing Http links
    tweet = re.sub(r'[^\w]', ' ', tweet)                                    # Removing non ascii chars
    tweet = re.sub(r'[^\x00-\x7F]+', ' ', tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = tweet.strip('\'"')                                              # Striping text
    stopwords = ['voteforhillary','imwithher','hillaryforpresident']        # StopWords
    querywords = tweet.split()
    resultwords = [word.lower() for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    result = result.strip()
    if result and not result.isspace():
        my_row = []
        my_row.append(result)
        w.writerow(my_row)
        flag = True
        fw.write(result)

    if flag == True:
        fw.write("\n")