import csv
import re

f = open("/Users/DS/Documents/DM/project/tweetsData_trump.csv","rb")            # Reading from the inputfile
reader = csv.reader(f)
fw = open("/Users/DS/Documents/DM/project/votefortrump.txt","wb")               #writting tweets into text file for backup
data = open("/Users/DS/Documents/DM/project/trump.csv","wb")                    #To Write output into csv file
w = csv.writer(data)

for row in reader:
    flag = False
    line = str(row)
    line = line.translate(None, '[\'')                                          # Removing '[''
    line1 = " ".join([word for word in line.split() if word != 'RT' and not word.startswith('@') ])
    line1 = line1.split("pic.twitter.com", 1)[0]                                # Removing pic link in tweets
    line1 = line1.split("http", 1)[0]                                           # Removing Http links
    line1 = re.sub(r'[^\w]', ' ', line1)                                        # Removing non ascii chars
    line1 = re.sub(r'[^\x00-\x7F]+', ' ', line1)
    line1 = re.sub('[\s]+', ' ', line1)
    line1 = line1.strip('\'"')                                                  # Striping text
    stopwords = ['votefortrump']                                                # StopWords
    querywords = line1.split()
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