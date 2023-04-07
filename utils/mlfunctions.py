from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

def get_model_and_vectorizer():
	df = pd.read_excel('dataset.xlsx') 

	df=df.sample(frac=1)

	train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)

	vectorizer = CountVectorizer() 
	X_train = vectorizer.fit_transform(train_df['data'])
	X_val = vectorizer.transform(val_df['data'])

	y_train = train_df['label']
	y_val = val_df['label']

	model = MultinomialNB() 
	model.fit(X_train, y_train)
	return model,vectorizer


def isIllegal(tag):
	model,vectorizer=get_model_and_vectorizer()
	
	tag = '"""{}"""'.format(tag)
	print("Supplied tag: ")
	print(tag)
	val=vectorizer.transform([tag])
	print(val)
	y_pred = model.predict(val)
	print(y_pred)
	if y_pred[0]==0:
		return False
	else:
		return True