# BENGULARE PRICE HOUSE PREDICTION
Disusun oleh: Khairunnisa Aulyah

## Domain Proyek

Tempat tinggal adalah kebutuhan primer bagi manusia untuk berlindung dan hidup menetap salah satunya Rumah.Dalam memilih rumah untuk ditinggali ada hal yang harus menjadi pertimbangan sebelum membeli rumah tersebut. Seperti Lokasi, ukuran properti, jumlah kamar, jumlah kamar mandi dan tipe area rumah. Tetapi ada faktor paling terpenting yaitu harga.

Seperti yang kita ketahui, harga properti rumah dari tahun ketahun semakin tidak pasti. Sehingga sulit untuk memastikan harga sebuah rumah di Bengaluru.Apalagi sebagian calon pembeli tidak mengerti dan tidak paham tentang harga pasar rumah.

Dengan demikian, maka dilakukanlah penelitian ini untu mengetahui harga pasar rumah. penelitian ini dilakukan dengan metode machine learning.Diharapkan agar calon pembeli mengerti tentang harga pasar rumah  sehingga dapat memilih rumah yang sesuai.

### Business Understanding

Perusahaan memiliki atau membeli rumah dan apartemen kemudian menyewanya ke konsumen.
Perusahaan membuka jasa konsultasi harga sewa rumah dan apartemen ke konsumen.

### Problem Statement
1. Bagaimana cara memproses data agar dapat dilatih dengan baik oleh model?
2. Berapa harga jual rumah di pasaran berdasarkan karakteristik tertentu?
3. 
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
- price: mempresentasikan harga rumah tersebut (fitur target)\\


