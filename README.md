# BENGULARE PRICE HOUSE PREDICTION
Disusun oleh: Khairunnisa Aulyah

## Domain Proyek

Tempat tinggal adalah kebutuhan primer bagi manusia untuk berlindung dan hidup menetap salah satunya Rumah.Dalam memilih rumah untuk ditinggali ada hal yang harus menjadi pertimbangan sebelum membeli rumah tersebut. Seperti Lokasi, ukuran properti, jumlah kamar, jumlah kamar mandi dan tipe area rumah. Tetapi ada faktor paling terpenting yaitu harga.

Seperti yang kita ketahui, harga properti rumah dari tahun ketahun semakin tidak pasti. Sehingga sulit untuk memastikan harga sebuah rumah di Bengaluru.Terutama calon pembeli yang sebagaian dari mereka tidak mengerti dan tidak paham tentang harga pasar rumah.

Dengan demikian, maka dilakukanlah penelitian ini untu mengetahui harga pasar rumah. penelitian ini dilakukan dengan metode machine learning.Diharapkan agar calon pembeli mengerti tentang harga pasar rumah  sehingga dapat memilih rumah yang sesuai.

### Business Understanding

Perusahaan memiliki atau membeli rumah dan apartemen kemudian menyewanya ke konsumen.
Perusahaan membuka jasa konsultasi harga sewa rumah dan apartemen ke konsumen.

### Problem Statement
1. Bagaimana cara memproses data agar dapat dilatih dengan baik oleh model?
2. Berapa harga jual rumah di pasaran berdasarkan karakteristik tertentu?
### Goals
1. Melakukan persiapan data untuk dapat dilatih oleh model.
2. Membuat model machine learning yang dapat memprediksi harga jual rumah seakurat mungkin berdasarkan fitur tertentu.

### Solution Statement
1. Menyiapkan data agar bisa digunakan dalam membangun model.
2. Menggunakan aLgoritma  K-Nearest Neighbour, Random Forest, dan AdaBoost untuk memprediksi harga jual rumah

## Data Understanding
Penelitian ini menggunakan dataset harga rumha di bengalure.  Dataset dapat diunduh di : [bengalure house data price](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data/download?datasetVersionNumber=2)

informasi Dataset: 
- Terdapat 13320 sample dengan 9 fitur yang terdiri dari 6 fitur tipe object dan 3 fitur tipe float 
- Terdapat missing value dalam dataset ini
- Dataset yang digunakan memiliki format CSV 

variabel yang terddapat dalam dataset:
- area_type : mmenentukan tipe are rumah
- availability : mennetukan apakah rumah tersebut tersedia atau tidak
- location: dimana rumah tersebut berasa
- size: berapa kamar tidur hall dan dapur dalam rumah tersebut
- society: 
- total_sqft: ukuran besar rumah tersebut
- bath : jumlah kamar mandi dalam rumah
- balcony: jumal balcony dalam rumah
- price: mempresentasikan harga rumah tersebut (fitur target)

### Menampilkan informasi dari dataset
Pada penelitian ini digunakan fungsi info() untuk menampilkan informasi dari dataset

| # |       column | Non-Null Count    | Dtype   |
|--:|-------------:|-------------------|---------|
| 0 |    area_type | 13320    non-null | object  |
| 1 | availability | 13320    non-null | object  |
| 2 |     location | 13319    non-null | object  |
| 3 | size         | 7818     non-null | object  |
| 4 | society      | 7818     non-null | object  |
| 5 | total_sqft   | 13320    non-null | object  |
| 6 | bath         | 13247    non-null | float64 |
| 7 | balcony      | 12711    non-null | float64 |
| 8 | price        | 13320    non-null | float64 |

dari info diatas, dapat dilihat bahwa:
- Terdapat 6 kolom dengan tipe object, yaitu: area_type, availability, location, size, society, total_sqft. Kolom ini merupakan categorical features (fitur non-numerik).
- Terdapat 3 kolom numerik dengan tipe data float64 yaitu: bath,balcony,price. bath,balcony merupakan fitur numerik yang merupakan hasil pengukuran secara fisik. price, merupakan target fitur kita.

### Menampilkan statistik dataset
Pada penelitian ini digunakan fungsi describe() untuk menampilkan statistik dari dataset,
|       | total_sqft   | bath         | balcony      | price        | BHK          |
|-------|--------------|--------------|--------------|--------------|--------------|
| count | 12669.000000 | 12711.000000 | 12711.000000 | 12711.000000 | 12711.000000 |
| mean  | 1511.842126  | 2.617339     | 1.584376     | 106.059200   | 2.737157     |
| std   | 1162.051672  | 1.225956     | 0.817263     | 131.761025   | 1.205052     |
| min   | 5.000000     | 1.000000     | 0.000000     | 8.000000     | 1.000000     |
| 25%   | 1100.000000  | 2.000000     | 1.000000     | 49.040000    | 2.000000     |
| 50%   | 1260.000000  | 2.000000     | 2.000000     | 70.000000    | 3.000000     |
| 75%   | 1640.000000  | 3.000000     | 2.000000     | 115.000000   | 3.000000     |
| max   | 52272.000000 | 40.000000    | 3.000000     | 29122.000000 | 43.000000    |

Fungsi describe() memberikan informasi sebagai berikut:

- Count adalah jumlah sampel pada data.
- Mean adalah nilai rata-rata
- Std adalah standar deviasi
- Min yaitu nilai minimum setiap kolom
- 25% adalah kuartil pertama. Kuartil adalah nilai yang menandai batas interval dalam empat bagian sebaran yang sama.
- 50% adalah kuartil kedua, atau biasa juga disebut median (nilai tengah).
- 75% adalah kuartil ketiga
- Max adalah nilai maksimum.

### Menghapus kolom yang tidak dibutuhkan 

| # |       column | Non-Null Count    | Dtype   |
|--:|-------------:|-------------------|---------|
| 0 |    area_type | 13320    non-null | object  |
| 1 | size         | 13304    non-null | object  |
| 2 | total_sqft   | 13320    non-null | object  |
| 3 | bath         | 13247    non-null | float64 |
| 4 | balcony      | 12711    non-null | float64 |
| 5 | price        | 13320    non-null | float64 |

<p align="center"> Gambar 2.  menampilkan informasi</p>
setelah dihapus tersisa 6 fitur. 
- 3 fitur tipe object yaitu area_type,size dan total_sqft 
- 3 fitur lainnya tipe float64 yaitu bath, balcony dan price

### Menangani Missing Value
pada penelitian ini daya menggunakan dua cara unttuk menemukan nilai missing value.
- cara pertama menggunakan fungsi isnull().sum(). hasil dari menggunakan fungsi tersebut yaitu.
 <p align="center">
 <img src="https://user-images.githubusercontent.com/71605581/208482612-c4c76f04-9106-4dac-a1f7-6202447f0311.png" width="180"  height="200"> </p>
 <p align="center"> Gambar 3. output pencarian missing value </p>

  Dari gambar diatas dapat dilihat bahwa terdapat 3 fitur yang terdapat missing value yaitu size, bath dan balcony. kemudian missing value tersebut dibuang menggunakan fungsi .dropna(). sehingga menjadi seperti berikut.
  <p align="center">
  <img src="https://user-images.githubusercontent.com/71605581/208482678-5481af33-a50b-4dd9-a085-d0384292ede7.png" width="180"  height="200"> </p>
  <p align="center"> Gambar 4. hasil missinng value </p>

- cara kedua yaitu menggunakan fungsi .loc() difitur bath, balcony, total_sqft
<p align="center">
<img src="https://user-images.githubusercontent.com/71605581/208482751-9880b982-b0ed-4d4e-aae9-a1babb986dfa.png" width="300"  height="120"> </p>
  <p align="center"> Gambar 5. output misisng value di 3 fitur  </p>
  Diantara 3 fitur tersebut, terdapat 1 fitur yang memiliki missing value yaitu fitur balcony.
Dicek apakah data yang bernilai 0 dalam fitur balcony terdapat juga pada fitur lain seperti berikut:

|       |           area_type | total_sqft | bath | balcony |   price | BHK |
|------:|--------------------:|-----------:|-----:|--------:|--------:|----:|
|    24 | Super built-up Area |      510.0 |  1.0 |     0.0 |  25.250 |   1 |
|    30 | Super built-up Area |     2475.0 |  4.0 |     0.0 | 186.000 |   4 |
|    42 | Super built-up Area |      600.0 |  1.0 |     0.0 |  38.000 |   1 |
|    43 |           Plot Area |      660.0 |  1.0 |     0.0 |  48.000 |   1 |
|    46 | Super built-up Area |      970.0 |  2.0 |     0.0 |  33.000 |   2 |
|   ... |                 ... |        ... |  ... |     ... |     ... | ... |
| 13260 |       Built-up Area |     1420.0 |  2.0 |     0.0 | 120.000 |   2 |
| 13265 | Super built-up Area |     1258.5 |  2.0 |     0.0 |  59.135 |   2 |
| 13291 |           Plot Area |      812.0 |  1.0 |     0.0 |  26.000 |   1 |
| 13299 | Super built-up Area |     2856.0 |  5.0 |     0.0 | 154.500 |   4 |
| 13315 |       Built-up Area |     3453.0 |  4.0 |     0.0 | 231.000 |   5 |

  Drop missing value tersebut. sehingga jumlah sampel berkurang menjadi 11682 dan terdapat 6 fitur.
  
### Menangani Outliers

outliers adalah sampel yang nilainya sangat jauh dari cakupan umum data utama. Ia adalah hasil pengamatan yang kemunculannya sangat jarang dan berbeda dari data hasil pengamatan lainnya.
Ada beberapa teknik untuk menangani outliers, antara lain:
- Hypothesis Testing
- Z-score method
- IQR Method

Pada penelitian ini, untuk mendeteksi outliers diggunakan teknik visualisasi data (boxplot). ddan menangani outliers dengan menggunakan teknik IQR method. IQR adalah singkatan dari Inter Quartile Range. Untuk memahami apa itu IQR, mari kita ingat lagi konsep kuartil. Kuartil dari suatu populasi adalah tiga nilai yang membagi distribusi data menjadi empat sebaran. Seperempat dari data berada di bawah kuartil pertama (Q1), setengah dari data berada di bawah kuartil kedua (Q2), dan tiga perempat dari data berada di kuartil ketiga (Q3). Dengan demikian interquartile range atau IQR = Q3 - Q1.
Mengecek outliners difitur bath
<p align="center">
  <img src="https://user-images.githubusercontent.com/71605581/208490912-dbd4400a-ce0d-47a5-94d6-8f4d7a312dfa.png" width="180"  height="200"> </p>
    <p align="center"> Gambar 7. Visualisasi boxplot outliers bath </p>
Mengecek outliners difitur balcony
<p align="center">
  <img src="https://user-images.githubusercontent.com/71605581/208491087-2f3afdc8-570f-4b41-9c9b-8bf53c0b21d2.png" width="180"  height="200"> </p>
    <p align="center"> Gambar 8. Visualisasi boxplot outliers balcony  </p>
  Dari 2 fitur dapat disimpulkan bahwa terdapat outliers di fitur bath. maka digunakanlah metode IQR untuk mengidentifikasi outlier yang berada di luar Q1 dan Q3. Nilai apa pun yang berada di luar batas ini dianggap sebagai outlier. 
persamaannya adalah:
- Batas bawah = Q1 - 1.5 * IQR
- Batas atas = Q3 + 1.5 * IQR
output yaitu: 
Dataset sekarang telah bersih dan memiliki 10.245 sampel.

## Data Preparation
### Encoding Fitur Kategori
#### menambahkan fitur bhk yang didapat dari mengubah fitur size ke int
untuk menambahkan fitur bhk maka diperlukan fungsi .unique untuk mengembalikan elemen unik array yang diurutkan.
<p align="center">
  <img src="https://user-images.githubusercontent.com/71605581/208494097-28670e55-3b7c-4f56-85ee-bc719186d99b.png" width="400"  height="80">
</p>
 <p align="center"> Gambar 9. output array fitur BHK </p>
Dari hasil tersebut digunakanlah fungsi .apply(lambda x: int(x.split(' ')[0]) untuk membagi dan mengubah fitur dan fungsi .drop untuk membuang fitur size yang sudah tidak digunakan lagi dengan hasil seperti berikut.

|   | area_type           | total_sqft | bath | balcony | price | BHK |
|---|---------------------|------------|------|---------|-------|-----|
| 0 | Super built-up Area | 1056       | 2.0  | 1.0     | 39.07 | 2   |
| 2 | Built-up Area       | 1440       | 2.0  | 3.0     | 62.00 | 3   |
| 3 | Super built-up Area | 1521       | 3.0  | 1.0     | 95.00 | 3   |
| 4 | Super built-up Area | 1200       | 2.0  | 1.0     | 51.00 | 2   |
| 5 | Super built-up Area | 1170       | 2.0  | 1.0     | 38.00 | 2   |

#### Mengubah nilai total_sqft ke nilai float
Mengubah fitur tipe total_sqft dari objek ke float64 digunakanlah fungsi convert_sqft_tonum(x) dan diapply kedalam fitur total_sqft tersebut. 
output:

| # |       column | Non-Null Count    | Dtype   |
|--:|-------------:|-------------------|---------|
| 0 | area_type    | 10245    non-null | object  |
| 1 | total_sqft   | 10245    non-null | float64 |
| 2 | bath         | 10245    non-null | float64 |
| 3 | balcony      | 10245    non-null | float64 |
| 4 | price        | 10245    non-null | float64 |
| 5 | BHK          | 10245    non-null | int64   |

#### Membagi area_type kedalam grup 
terdapat 4 area didalam fitur area_type, yaitu Super built-up Area, Built-up Area, Plot Area, Carpet Area. karena hal itu maka setiap area akan dikelompokkan dan diubah menjadi angka menggunakan fungsi .replace 
output: 

|   | area_type | total_sqft | bath | balcony | price | BHK |
|---|-----------|------------|------|---------|-------|-----|
| 0 |     0     | 1056       | 2.0  | 1.0     | 39.07 | 2   |
| 2 |     1     | 1440       | 2.0  | 3.0     | 62.00 | 3   |
| 3 |     0     | 1521       | 3.0  | 1.0     | 95.00 | 3   |
| 4 |     0     | 1200       | 2.0  | 1.0     | 51.00 | 2   |
| 5 |     0     | 1170       | 2.0  | 1.0     | 38.00 | 2   

### Train-Test-Split
  Membagi dataset menjadi data latih (train) dan data uji (test) merupakan hal yang harus kita lakukan sebelum membuat model. Kita perlu mempertahankan sebagian data yang ada untuk menguji seberapa baik generalisasi model terhadap data baru. Ssetiap transformasi dilakukan pada data juga merupakan bagian dari model. Karena data uji (test set) berperan sebagai data baru, kita perlu melakukan semua proses transformasi dalam data latih. Tujuannya adalah agar tidak mengotori data uji dengan informasi yang kita dapat dari data latih.

untuk melakukan pembagian dataset, kita perlu mengimport library split data yaitu train_test_split, kemudian buat 2 variabel yaitu X yang berfungsi untuk menghapus kolom charges dan y untuk menampilkan kolom charges lalu bagi dataset menjadi 4 variabel baru yaitu X_train, X_test, y_train, y_test dengan library train_test_split dengan parameter yang digunakan yaitu :

- X = berfungsi untuk menghapus kolom charges
- y = berfungsi menampilkan kolom charges
- test_size = adalah ukuran pembagian dataset yaitu sekitar 80 % untuk training dan 20 % untuk testing, data testing ini bertujuan untuk mengukur kinerja model pada data baru.
- random_state = untuk mengontrol random number generator. penelitian ini menggunakan random_state = 55

Untuk mengecek jumlah sampel pada masing-masing bagian digunakan fungsi print
output: 
- Total sampel diseluruh dataset: 10245
- Total sampel ditrain dataset: 9220
- Total sampel ditest dataset: 1025

### Standarisasi
Standardisasi adalah teknik transformasi yang digunakan dalam tahap persiapan pemodelan. kita akan menggunakan teknik StandarScaler dari library Scikitlearn. StandardScaler melakukan proses standarisasi fitur dengan mengurangkan mean (nilai rata-rata) kemudian membaginya dengan standar deviasi untuk menggeser distribusi.  StandardScaler menghasilkan distribusi dengan standar deviasi sama dengan 1 dan mean sama dengan 0. Sekitar 68% dari nilai akan berada di antara -1 dan 1. 
Untuk menghindari kebocoran informasi pada data uji, kita hanya akan menerapkan fitur standarisasi pada data latih. Kemudian, pada tahap evaluasi, kita akan melakukan standarisasi pada data uji.
output: 

|      | total_sqft |      bath |   balcony | area_type |       BHK |
|-----:|-----------:|----------:|----------:|----------:|----------:|
| 7618 |   0.834721 |  1.007651 |  0.476906 | -0.532967 |  0.710586 |
| 9145 |   0.207169 |  2.505161 | -0.998622 |  2.557569 |  2.088132 |
| 7100 |  -0.479895 | -0.489858 | -0.998622 | -0.532967 | -0.666959 |
| 3530 |  -1.010807 | -1.987367 | -0.998622 | -0.532967 | -2.044505 |
| 4786 |  -0.842165 | -1.987367 | -0.998622 | -0.532967 | -0.666959 |


proses standarisasi mengubah nilai rata-rata (mean) menjadi 0 dan nilai standar deviasi menjadi 1. Untuk mengecek nilai mean dan standar deviasi pada setelah proses standarisasi digunakan fungsi .describe()
output:
|       | total_sqft |      bath |   balcony | area_type |       BHK |
|------:|-----------:|----------:|----------:|----------:|----------:|
| count |  9220.0000 | 9220.0000 | 9220.0000 | 9220.0000 | 9220.0000 |
|  mean |    -0.0000 |   -0.0000 |   -0.0000 |   -0.0000 |   -0.0000 |
|   std |     1.0001 |    1.0001 |    1.0001 |    1.0001 |    1.0001 |
|   min |    -1.6529 |   -1.9874 |   -0.9986 |   -0.5330 |   -2.0445 |
|   25% |    -0.3150 |   -0.4899 |   -0.9986 |   -0.5330 |   -0.6670 |
| 50%   | -0.1239    | -0.4899   | 0.4769    | -0.5330   | -0.6670   |
| 75%   | 0.2309     | 1.0077    | 0.4769    | 1.0123    | 0.7106    |
| max   | 63.6319    | 2.5052    | 1.9524    | 4.1028    | 7.5983    |

## Model Development

Pada tahap ini, model machine learning akan dikembangkan dengan tiga algoritma. Kemudian, mengevaluasi performa masing-masing algoritma dan menentukan algoritma mana yang memberikan hasil prediksi terbaik. Ketiga algoritma yang akan kita gunakan, antara lain:

1. *K-Nearest Neighbor*
2. *Random Forest*
3. *Boosting Algorithm*

### *K-Nearest Neighbor*
Algoritma KNN menggunakan ‘kesamaan fitur’ untuk memprediksi nilai dari setiap data yang baru. Dengan kata lain, setiap data baru diberi nilai berdasarkan seberapa mirip titik tersebut dalam set pelatihan.

KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat (dengan k adalah sebuah angka positif). Nah, itulah mengapa algoritma ini dinamakan K-nearest neighbor (sejumlah k tetangga terdekat). KNN bisa digunakan untuk kasus klasifikasi dan regresi. Pada kasus ini, kita akan menggunakannya untuk kasus regresi.

Kita menggunakan k = 10 tetangga dan metric Euclidean untuk mengukur jarak antara titik. Pada tahap ini kita hanya melatih data training dan menyimpan data testing untuk tahap evaluasi yang akan dibahas di Modul Evaluasi Model.

### *Random Forest*
Algoritma *random forest* adalah salah satu algoritma supervised learning. Ia dapat digunakan untuk menyelesaikan masalah klasifikasi dan regresi. Random forest juga merupakan algoritma yang sering digunakan karena cukup sederhana tetapi memiliki stabilitas yang mumpuni. 

*Random forest* merupakan salah satu model machine learning yang termasuk ke dalam kategori ensemble (group) learning. Apa itu model ensemble? Sederhananya, ia merupakan model prediksi yang terdiri dari beberapa model dan bekerja secara bersama-sama. Ide dibalik model ensemble adalah sekelompok model yang bekerja bersama menyelesaikan masalah. Sehingga, tingkat keberhasilan akan lebih tinggi dibanding model yang bekerja sendirian. Pada model ensemble, setiap model harus membuat prediksi secara independen. Kemudian, prediksi dari setiap model ensemble ini digabungkan untuk membuat prediksi akhir. 

cara untuk menerapkan algoritma ini apda dataset yaitu, pertama, Anda mengimpor RandomForestRegressor dari library scikit-learn. Anda juga mengimpor mean_squared_error sebagai metrik untuk mengevaluasi performa model. Selanjutnya, Anda membuat variabel RF dan memanggil RandomForestRegressor dengan beberapa nilai parameter. Berikut adalah parameter-parameter yang digunakan:

- n_estimator: jumlah trees (pohon) di forest. Di sini kita set n_estimator=50.
- max_depth: kedalaman atau panjang pohon. Ia merupakan ukuran seberapa banyak pohon dapat membelah (splitting) untuk membagi setiap node ke dalam jumlah pengamatan yang diinginkan.
- random_state: digunakan untuk mengontrol random number generator yang digunakan. 
- n_jobs: jumlah job (pekerjaan) yang digunakan secara paralel. Ia merupakan komponen untuk mengontrol thread atau proses yang berjalan secara paralel. n_jobs=-1 artinya semua proses berjalan secara paralel.

### *Boosting Algorithm*
*boosting* algoritma ini bertujuan untuk meningkatkan performa atau akurasi prediksi. Caranya adalah dengan menggabungkan beberapa model sederhana dan dianggap lemah (weak learners) sehingga membentuk suatu model yang kuat (strong ensemble learner). Algoritma boosting muncul dari gagasan mengenai apakah algoritma yang sederhana seperti linear regression dan decision tree dapat dimodifikasi untuk dapat meningkatkan performa. 
Algoritma boosting terdiri dari dua metode:
- *Adaptive boosting*
- *Gradient boosting*
Pada kasus ini, kita akan menggunakan metode adaptive boosting.
parameter yang digunakan adalah:
- *learning_rate*: bobot yang diterapkan pada setiap regressor di masing-masing proses iterasi boosting.
- *random_state*: digunakan untuk mengontrol random number generator yang digunakan.

## Evaluasi Model
Metrik yang akan digunakan pada prediksi ini adalah MSE atau Mean Squared Error yang menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi. MSE didefinisikan dalam persamaan berikut: 

MSE = $\frac{1}{n} \Sigma_{i=1}^n({y}-\hat{y_i})^2$ 

Keterangan:

- N = jumlah dataset

- y = nilai sebenarnya

- yi = nilai prediksi

Sebelum menghitung nilai MSE dalam model, kita perlu melakukan proses scaling fitur numerik pada data uji. Sebelumnya, kita baru melakukan proses scaling pada data latih untuk menghindari kebocoran data. Sekarang, setelah model selesai dilatih dengan 3 algoritma, yaitu KNN, Random Forest, dan Adaboost, kita perlu melakukan proses scaling terhadap data uji. Hal ini harus dilakukan agar skala antara data latih dan data uji sama dan kita bisa melakukan evaluasi.
Hasil evaluasi pada data latih dan data test adalah sebagai berikut:

|          |    train | test     |
|---------:|---------:|----------|
|      KNN | 0.412901 | 0.573547 |
|       RF |   0.2558 | 0.508534 |
| Boosting |  0.63323 | 0.553535 |


Untuk memudahkan, mari kita plot metrik tersebut dengan bar chart, output:
<p align="center">
  <img src="https://user-images.githubusercontent.com/71605581/208509610-a0fa3e58-dd4c-4d0b-96fd-67e2a36bc3c3.png" width="300"  height="200"></p>
   <p align="center"> Gambar 12. Visualisasi Hasil MSE  </p>

Dari gambar di atas, terlihat bahwa, model *Random Forest* (RF) memberikan nilai eror yang paling kecil. Sedangkan model dengan algoritma Boosting memiliki eror yang paling besar. Model inilah yang akan kita pilih sebagai model terbaik untuk melakukan prediksi harga jual rumah di bengalure.Untuk mengujinya, kita buat prediksi menggunakan beberapa harga dari data test.

Hasilnya adalah sebagai berikut:
- y_true = 88.0
- prediksi_KNN = 78.5
- prediksi_RF = 83.5
- prediksi_Boosting = 72.5

Terlihat pada gambar 12 adalah hasil dari prediksi dengan 3 ALgoritma yaitu *Random Forest (RF)*, *K-Nearest Neighbor* dan *Boosting alghorthm*. pada hasil diatas dapat dijabarkan bahwa algortima *Random Forest (RF)* memberikan hasil yang paling mendekati dengan hasil prediksi 83.5 sedangkan algoritma *Boosting* dengan hasil prediksi terjauh yaitu 72.5.

Referensi :

[1] [ANAND G. RAWOOL, D. V. (2021). House Price Prediction Using Machine Learning. IRE Journals.](https://www.irejournals.com/formatedpaper/1702692.pdf)

