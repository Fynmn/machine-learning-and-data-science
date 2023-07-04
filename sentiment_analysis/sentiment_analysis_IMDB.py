import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from bs4 import BeautifulSoup


print("+++++++++++++++++++++++++++++++++++++++++")
print("+           Sentiment Analysis          +")
print("+          on the IMDB Dataset          +")
print("+     with Logistic Regression and      +")
print("+           Feature Extraction          +")
print("+   written by Natalie Jane Pacificar   +")
print("+++++++++++++++++++++++++++++++++++++++++")

# Loading the dataset
dataset = pd.read_csv('IMDB_Dataset.csv')
print(dataset.head(10))

print("\nCleaning the Dataset...\n")
# I trained the model with 10000 reviews from the dataset 
dataset_len = len(dataset.iloc[:10000, 0])
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')

porter_stemmer = PorterStemmer()

# a list of text with the cleaned data
corpus = []

for i in range(dataset_len):
  review = BeautifulSoup(dataset[0:10000]['review'][i], "html.parser").get_text()
  review = re.sub('\[[^]]*\]',' ',review)
  review = re.sub('[^a-zA-z0-9]',' ',review)
  review = review.lower()
  review = review.split()
  review = [porter_stemmer.stem(word) for word in review if not word in set(all_stopwords)]
  review = ' '.join(review)

  corpus.append(review)
    
print("Done cleaning the data!")

# print(corpus)


print("\nExtracting the features and training the classifier...\n")

features = [100, 500, 1500, 2000]

for feature in features:
    # Feature Extraction with TfidfVectorizer
    from sklearn.feature_extraction.text import TfidfVectorizer
    tv = TfidfVectorizer(max_features = feature)
    x = tv.fit_transform(corpus).toarray()
    y = dataset.iloc[:10000,1].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=0)

    # Fitting the Logistic Regression algorithm to the Training set
    from sklearn.linear_model import LogisticRegression

    classifier = LogisticRegression(max_iter = 500,random_state = 0)
    classifier.fit(x_train, y_train)

    # Metrics
    from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

    y_pred = classifier.predict(x_test)
    print("\nMETRICS\n")
    print(f"{feature} Features Results\n")
    print(f"Confusion Matrix:\n {confusion_matrix(y_test, y_pred)}\n")
    print(f"Classification Report:\n {classification_report(y_test, y_pred)}")
    print(f"Accuracy: {str(int(accuracy_score(y_test, y_pred)*100))}%\n")

