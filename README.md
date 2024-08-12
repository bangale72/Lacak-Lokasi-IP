# Lacak-Lokasi-IP
Berikut adalah contoh sederhana dari script Python untuk menghitung nilai rata-rata dan menentukan ranking siswa. Kita akan membuatnya dalam dua bagian: pertama untuk menghitung rata-rata, dan kedua untuk menentukan ranking berdasarkan nilai-nilai tersebut.

Langkah-langkah:
Daftar untuk Mendapatkan Token API: Anda perlu mendapatkan token API dari ipinfo.io. Token ini akan digunakan untuk mengautentikasi permintaan API.

Instalasi Paket requests: Jika Anda belum menginstal paket requests, Anda bisa melakukannya dengan menjalankan pip install requests di terminal atau command prompt.

Penjelasan:
1. cari_lokasi_ip(ip_address, token): Fungsi ini membuat permintaan ke API ipinfo.io untuk mendapatkan informasi lokasi berdasarkan alamat IP yang diberikan.
2. tampilkan_lokasi(data): Fungsi ini menampilkan informasi lokasi yang diperoleh dari API.
2. main(): Fungsi utama yang meminta token API dan alamat IP dari pengguna, kemudian menampilkan hasilnya.

Cara Menjalankan:
$ pkg update && pkg upgrade
$ git clone https://github.com/Farhanale-sys/Lacak-Lokasi-IP
$ cd Lacak-Lokasi-IP
$ pip install requests
$ python cari_lokasi_ip.py
