from sklearn.preprocessing import StandardScaler

X, y = iris['data'], iris['target']
df = pd.DataFrame(X, columns=iris['feature_names'])

s_scaler = StandardScaler()
s_scaler.fit(df)   # pandas DataFrame도 지원
s_df = s_scaler.transform(df)
s_df   # 처리 결과는 ndarray로 반환됨

s_df = pd.DataFrame(s_df, columns=iris['feature_names'])
s_df

from sklearn.preprocessing import MinMaxScaler

