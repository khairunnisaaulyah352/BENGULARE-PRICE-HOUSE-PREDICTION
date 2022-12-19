# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RPj_YXEO2Wastk96vqFvWMjsBFHJ5Ggy

nama: khairunnisa aulyah

#**DATA UNDERSTANDING**


import library yang dibutuhkan
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

"""load the dataset"""

df = pd.read_csv('/content/Bengaluru_House_Data.csv')
df

"""informasi dataset"""

df.info()

"""Drop unnessory column for better understanding of data"""

df=df.drop(['location','availability' ,'society' ],axis=1)
df.info()

"""memastikan tidak ada missing value"""

df.isnull().sum()

"""membuang missing value"""

df=df.dropna()
df.isnull().sum()

"""mengecek apakah terdapat missing value dalam 3 fitur"""

bath = (df.bath == 0).sum()
balcony = (df.balcony == 0).sum()
total_sqft = (df.total_sqft == 0).sum()
 
print("Nilai 0 di kolom bath ada: ", bath)
print("Nilai 0 di kolom balcony ada: ", balcony)
print("Nilai 0 di kolom balcony ada: ", total_sqft)

"""mengecek apakah data bernilai 0  fitur balcony juga terdapat pada fitur lain"""

df.loc[(df['balcony']==0)]

""" Drop baris untuk mengatasi missing value dan Cek ukuran data untuk memastikan baris sudah di-drop"""

df = df.loc[(df[['balcony']]!=0).all(axis=1)]
df.shape

"""mengecek ouliners"""

sns.boxplot(x=df['bath'])

sns.boxplot(x=df['balcony'])

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR=Q3-Q1
df=df[~((df<(Q1-1.5*IQR))|(df>(Q3+1.5*IQR))).any(axis=1)]
df.shape

"""#**DATA PREPARATION**
menambahkan fitur bhk yang didapat dari mengubah fitur size ke int
"""

df['size'].unique()

df['BHK']=df['size'].apply(lambda x: int(x.split(' ')[0]))

df=df.drop(['size' ],axis=1)

df.head()

"""Mengubah nilai total_sqft ke nilai float"""

def convert_sqft_tonum(x):
    token=x.split('-')
    if len(token)==2:
        return (float(token[0])+float(token[1]))/2
    try:
        return float(x)
    except:
        return None
df=df.copy()
df['total_sqft']=df['total_sqft'].apply(convert_sqft_tonum)

df.info()

df.describe()

"""Membagi area_type kedalam grup"""

#can split the data into groups by its area type a
grouped=df.groupby('area_type')

#give number of values in different groups in list form
count=list(grouped.size())
print(count)

#mendaptlan nama grup dari list form
grp=list(grouped.groups)
print(grp)

df['area_type'] = df['area_type'].astype(str).str.replace('Super built-up  Area', '0')
df['area_type'] = df['area_type'].astype(str).str.replace('Built-up  Area', '1')
df['area_type'] = df['area_type'].astype(str).str.replace('Plot  Area', '2')
df['area_type'] = df['area_type'].astype(str).str.replace('Carpet  Area', '3')

df.head(5)

df.hist(bins=50, figsize=(15,10))
plt.show()

df.fillna(999, inplace=True)

df.replace([np.inf, -np.inf], np.nan, inplace=True)

"""Membagi dataset menjadi data latih (train) dan data uji (test)"""

from sklearn.model_selection import train_test_split
 
X = df.drop(["price"],axis =1)
y = df["price"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 55)

"""mengecek jumlah sampel"""

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""Standarisasi"""

from sklearn.preprocessing import StandardScaler
 
numerical_features = ['total_sqft','bath','balcony', 'area_type','BHK']
scaler = StandardScaler()
scaler.fit(X_train[numerical_features])
X_train[numerical_features] = scaler.transform(X_train.loc[:, numerical_features])
X_train[numerical_features].head()

X_train[numerical_features].describe().round(4)

"""#**Model Development**

Siapkan dataframe untuk analisis model
"""

models = pd.DataFrame(index=['train_mse', 'test_mse'], 
                      columns=['KNN', 'RandomForest', 'Boosting'])

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
 
knn = KNeighborsRegressor(n_neighbors=3)
knn.fit(X_train, y_train)
 
models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)

"""Import library yang dibutuhkan dan buat model prediksi"""

from sklearn.ensemble import RandomForestRegressor
RF = RandomForestRegressor(n_estimators=80, max_depth=20, random_state=85, n_jobs=-1)
RF.fit(X_train, y_train)
 
models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

from sklearn.ensemble import AdaBoostRegressor
 
boosting = AdaBoostRegressor(learning_rate=0.01, random_state=55)                             
boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""Lakukan scaling terhadap fitur numerik pada X_test sehingga memiliki rata-rata=0 dan varians=1"""

X_test.loc[:, numerical_features] = scaler.transform(X_test[numerical_features])

# Buat variabel mse yang isinya adalah dataframe nilai mse data train dan test pada masing-masing algoritma
mse = pd.DataFrame(columns=['train', 'test'], index=['KNN','RF','Boosting'])
 
# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = {'KNN': knn, 'RF': RF, 'Boosting': boosting}
 
# Hitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train))/1e3 
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test))/1e3
 
# Panggil mse
mse

"""plot metrik dengan bar chart"""

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""prediksi menggunakan beberapa harga dari data test"""

prediksi = X_test.iloc[:1].copy()
pred_dict = {'y_true':y_test[:1]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)
 
pd.DataFrame(pred_dict)