import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import pickle

df= pd.read_csv("/Users/debajyotidas/Documents/GitHub/Deployment of ML Models using Cloud Frameworks/NLP-Deployment-Heroku/spam.csv", encoding="latin-1")
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
# Features and Labels
df['label'] = df['class'].map({'ham': 0, 'spam': 1})
X = df['message']
y = df['label']

# Extract Feature With CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(X) # Fit the Data

pickle.dump(cv, open('/Users/debajyotidas/Documents/GitHub/Deployment of ML Models using Cloud Frameworks/NLP-Deployment-Heroku/transform.pkl', 'wb')) #saving the CountVectorizer transformation model for pre-processing the incoming test set, during run-time

#Splitting the data for model training and validation
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)

clf.fit(X,y) #Fitting on the entire data for better training the model
filename = '/Users/debajyotidas/Documents/GitHub/Deployment of ML Models using Cloud Frameworks/NLP-Deployment-Heroku/nlp_model.pkl'
pickle.dump(clf, open(filename, 'wb'))

#Alternative Usage of Saved Model
# joblib.dump(clf, filename)
# NB_spam_model = open(filename,'rb')
# clf = joblib.load(NB_spam_model)
