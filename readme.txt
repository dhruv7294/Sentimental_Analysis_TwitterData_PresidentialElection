1. Used fetchdata_hillary_final.py and fetchdata_trump_final.py to pre-process tweets and remove all the stopwords, remove non ascii chars and links etc.(input fetched Tweets files)

2. Used the output of the above step as input to feature_exctraction.py. Divide the tweets  of trump and hillary for 2 sections. 30000 tweets for training purpose in combined.csv(added a column of the actual candidate information for training purpose) and 5000 tweets for testing purpose in testing.csv(added a column of the actual candidate information for testing purpose to check the confusion matrics and accuracy)

3.fetch_data_wordcloud.py is used to generate the word cloud and input is fetched tweets we have extracted from tweeter.