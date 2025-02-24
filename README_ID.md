# UNI436 - Tugas SIC Tahap 2

Halo! 👋 Selamat datang di repositori ini. Proyek ini adalah bagian dari tugas Tahap 2 SIC (Samsung Innovation Campus). Di sini, kita bakal menghubungkan ESP32 dengan beberapa sensor keren dan mengumpulkan datanya lewat REST API.

## Apa Saja yang Ada di Proyek Ini?

### Hardware yang Digunakan

- **Board ESP32 DevKit**
- **Sensor:**
  - DHT22 (Mengukur suhu & kelembaban)
  - HC-SR04 (Mengukur jarak dengan ultrasonik)
  - LDR (Sensor cahaya)

### Software yang Dipakai

1. **Aplikasi MicroPython di ESP32**
   - Ngumpulin data dari sensor
   - Koneksi ke WiFi
   - Kirim data ke server
2. **Flask REST API**
   - Simpan data ke MongoDB
   - Sediakan endpoint buat akses data
   - Bisa jalan di Docker

## Cara Memulai

### Yang Harus Dipersiapkan

Pastikan sudah punya ini dulu:

- Python 3.13 atau lebih baru
- Docker & Docker Compose
- Alat MicroPython (ada di `requirements-dev.txt`)

### Instalasi & Setup

#### 1. Clone repositorinya dulu

```sh
git clone https://www.github.com/fwwz-id/uni436-s2as2
cd uni436-s2as2
```

#### 2. Jalankan API-nya

```sh
docker compose up -d
```

#### 3. Flash ESP32 buat pengembangan

```sh
pip install -r requirements-dev.txt
```

Kalau butuh panduan lebih lengkap, bisa cek [dokumentasi resmi MicroPython](https://micropython.org/download/ESP32_GENERIC/).

## API Endpoints

- `GET /ping` - Cek apakah server nyala
- `GET /dht22` - Ambil data dari sensor DHT22

## Pengembangan & Simulasi

Bisa coba jalankan proyek ini di simulator Wokwi sebelum dipasang ke ESP32 asli. Lihat [diagram.json](diagram.json) buat konfigurasi hardware-nya.

### Cara Pakai Wokwi

#### 1. Instal dulu ekstensi Wokwi
- Download dari [sini](https://marketplace.visualstudio.com/items?itemName=Wokwi.wokwi-vscode).

#### 2. Jalankan Simulasi
- Tekan `Ctrl + Shift + P` di VS Code.
- Cari `Wokwi: Start Simulation` dan pilih `wokwi.toml` kalau diminta.

#### 3. Hubungkan ke ESP32

Jalankan perintah ini buat nyambung ke ESP32:

```sh
mpremote connect port:rfc2217://localhost:4000 run esp32/main.py
```

Buat yang mau lebih lanjut, cek [dokumentasi resmi Wokwi](https://github.com/wokwi/wokwi-vscode-micropython/blob/main/README.md).

#### Troubleshooting

Kalau dapat error `mpremote.transport.TransportError: could not enter raw repl`, coba jalankan ulang. Kalau masih error, restart simulasi.

Buat cek apakah port 4000 aktif:

```sh
# Linux/macOS
netstat -an | grep 4000  

# Windows
netstat -ano | findstr 4000  
```

Harusnya muncul output seperti ini:

```sh
tcp    0    0 127.0.0.1:4000   0.0.0.0:*   LISTEN
```

Kalau masih ada masalah, bisa tanya di komunitas Discord Wokwi atau dukungan resminya.

## Deploy ke ESP32 Asli

Kalau udah siap buat deploy ke perangkat ESP32 asli, jalankan ini:

```sh
mpremote connect port:rfc2217://<esp32-ip>:4000 run esp32/main.py
```

## Lisensi

Proyek ini adalah bagian dari tugas di acara tertentu. Selamat ngoprek! 🚀

