import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

le = LabelEncoder()
encoded_income = le.fit_transform(data[['income']])

ohe = OneHotEncoder(sparse=False)
src_items = items[..., np.newaxis]
ohe.fit(src_items)
rv = ohe.transform(src_items)


result2 = pd.get_dummies(df, columns=['Item', 'Level'])
result2

# join


# X, y 나누기
y = adult_data['income']   # type: series
X = adult_data.drop(columns='income')


print(adult_data.shape, X.shape, y.shape)
X.columns
y.value_counts()


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# train/test 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)
# train set을 train/validation set으로 분리
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, stratify=y_train, random_state=0)

# DecisionTreeClassifier 사용
tree = DecisionTreeClassifier(random_state=0, max_depth=7)
# 학습 - train
tree.fit(X_train, y_train)

# 평가 - 예측 -> 평가 (train set으로)
pred_train = tree.predict(X_train)
train_acc = accuracy_score(y_train, pred_train)
print('train 정확도: ', train_acc)
# 평가 - 예측 -> 평가 (validation set으로)
pred_val = tree.predict(X_val)
val_acc = accuracy_score(y_val, pred_val)
print('val 정확도: ', val_acc)


# 최종평가
pred_test = tree.predict(X_test)
test_acc = accuracy_score(y_test, pred_test)
print('test 정확도: ', test_acc)