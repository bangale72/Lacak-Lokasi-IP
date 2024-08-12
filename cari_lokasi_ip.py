import requests

def cari_lokasi_ip(ip_address, token):
    url = f"https://ipinfo.io/{ip_address}/json?token={token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def tampilkan_lokasi(data):
    if data:
        print(f"Alamat IP: {data.get('ip', 'Tidak Diketahui')}")
        print(f"Hostname: {data.get('hostname', 'Tidak Diketahui')}")
        print(f"Lokasi: {data.get('city', 'Tidak Diketahui')}, {data.get('region', 'Tidak Diketahui')}, {data.get('country', 'Tidak Diketahui')}")
        print(f"Koordinat: {data.get('loc', 'Tidak Diketahui')}")
        print(f"Organisasi: {data.get('org', 'Tidak Diketahui')}")
    else:
        print("Gagal mendapatkan informasi lokasi untuk alamat IP ini.")

def main():
    token = input("Masukkan token API ipinfo.io Anda: ")
    ip_address = input("Masukkan alamat IP yang ingin dicari: ")
    
    data = cari_lokasi_ip(ip_address, token)
    tampilkan_lokasi(data)

if __name__ == "__main__":
    main()
