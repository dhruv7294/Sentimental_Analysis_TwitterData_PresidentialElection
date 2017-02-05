import pandas as pd                                               # Using panda to work with CSV file
from sklearn.feature_extraction.text import CountVectorizer       # Tokenizing text with scikit-learn
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB                     # Suitable Naive_bayes classifier for word count
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier                    # SVM classifier
from sklearn import metrics
import numpy as np

input_file = "/Users/DS/Documents/DM/project/combined.csv"        # CSV file for training purpose
output_file = "/Users/DS/Documents/DM/project/answer.csv"         # CSV file for printing
testing_file = "/Users/DS/Documents/DM/project/testing.csv"       # CSV file for testing purpose


df = pd.read_csv(input_file, header = None)                       # Reading csv file with dataframe
count_vector = CountVectorizer()
train_counts = count_vector.fit_transform(df[df.columns[0]])      # 0st column of df dataframe is for Training Tweets
#print train_counts.shape
tfidf_transformer = TfidfTransformer()
train_tfidf = tfidf_transformer.fit_transform(train_counts)       # 1st column of df dataframe is for Actual Candidate
clf = MultinomialNB().fit(train_tfidf, df[df.columns[1]])         # Used naive bayes classifier to generate model with training data set


df2 = pd.read_csv(testing_file, header= None)                     # Creating DataFrame for testing purpose by reading csv file
#df2.iloc[np.random.permutation(len(df2))]
new_counts = count_vector.transform(df2[df2.columns[0]])          # 0th column of df2 dataframe is for testing tweets
new_tfidf = tfidf_transformer.transform(new_counts)
predicted_nb = clf.predict(new_tfidf)                             # Predicted data using naive bayes classifier
print "naive_bayes Prediction = %s" % (predicted_nb)


pipe_line = Pipeline([('vect', CountVectorizer()),                # Used Pipeline with SVM classifier to train the model
                     ('tfidf', TfidfTransformer()),
                      ('clf', SGDClassifier()),])
pipe_line = pipe_line.fit(df[df.columns[0]], df[df.columns[1]])
predicted_svm = pipe_line.predict(df2[df2.columns[0]])            # Predicted outcome using svm classifier
print "svm Prediction = %s" % (predicted_svm)
df_output = pd.DataFrame(index=[df2[df2.columns[0]],df2[df2.columns[1]],predicted_nb,predicted_svm])    # Creating dataframe with Tweets, Actual Candidate, Predicated candidate using naive based, Predicated candidate using svm based
df_output.to_csv(output_file)                                     # Exporting data to csv file


accuracy_nb = np.mean(predicted_nb == df2[df2.columns[1]])
print "accuracy_nb = %s" % accuracy_nb
print "Confusion_Metrics_nb = \n %s" % metrics.confusion_matrix(df2[df2.columns[1]], predicted_nb)      # Creating confusion metric using predicted_nb

accuracy_svm = np.mean(predicted_svm == df2[df2.columns[1]])
print "accuracy_svm = %s" % accuracy_svm
print "Confusion_Metrics_svm = \n %s" % metrics.confusion_matrix(df2[df2.columns[1]], predicted_svm)    # Creating confusion metric using predicted_svm
