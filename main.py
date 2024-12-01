# main.py

import sys
import os
import time  # Import time module untuk menggunakan sleep
from colorama import Fore, Style, init  # Import untuk warna

# Inisialisasi colorama untuk bekerja di Windows dan Unix
init(autoreset=True)

# Menambahkan folder 'modules' ke sys.path agar bisa mengimpor modul-modul dari folder tersebut
sys.path.append(os.path.join(os.getcwd(), 'modules'))
sys.path.append(os.path.join(os.getcwd(), 'config'))

# Mengimpor modul-modul dari folder solana_modules
from wallet_generator import generate_keypair
from file_handler import save_wallet_to_file
from format_converter import convert_private_key_to_base58, convert_public_key_to_base58

def get_positive_integer_input(prompt, default_value=1):
    """
    Fungsi untuk meminta input berupa angka positif.
    Jika input tidak valid, akan mengembalikan nilai default.
    """
    try:
        value = int(input(prompt))
        if value <= 0:
            print(f"{Fore.RED}Jumlah wallet harus lebih besar dari 0. Menggunakan nilai default.")
            return default_value
        return value
    except ValueError:
        print(f"{Fore.RED}Input tidak valid! Menggunakan nilai default.")
        return default_value

def main():
    # Menampilkan pesan selamat datang dengan warna
    print(f"{Fore.CYAN}{Style.BRIGHT}Selamat datang di generator wallet Solana!{Style.RESET_ALL}\n")

    # Meminta input jumlah wallet yang ingin dibuat
    wallet_count = get_positive_integer_input(f"{Fore.GREEN}Masukkan jumlah wallet yang ingin dibuat: {Style.RESET_ALL}", 3)
    
    # Meminta input jeda waktu antar wallet (dalam detik)
    delay_time = get_positive_integer_input(f"{Fore.GREEN}Masukkan jeda waktu antar wallet (dalam detik): {Style.RESET_ALL}", 2)

    print(f"{Fore.YELLOW}Proses pembuatan {wallet_count} wallet dimulai...\n")

    # Menyimpan semua wallet ke dalam satu file 'walletjadi.txt'
    try:
        with open("walletjadi.txt", "w") as f:  # Membuka file walletjadi.txt untuk menulis
            f.write("===== Daftar Wallet Solana =====\n\n")  # Menulis header tanpa warna
            for i in range(wallet_count):
                # Menghasilkan keypair Solana
                public_key, private_key = generate_keypair()

                # Konversi private key ke base58
                private_key_base58 = convert_private_key_to_base58(private_key)

                # Menulis keypair yang sudah dikonversi ke dalam file tanpa kode warna
                f.write(f"Wallet {i + 1}:\n")
                f.write(f"Public Key: {public_key}\n")
                f.write(f"Private Key (Base58): {private_key_base58}\n")
                f.write("\n")  # Baris kosong antara wallet

                # Menampilkan informasi di terminal dengan warna
                print(f"{Fore.GREEN}Wallet {i + 1} berhasil dibuat dan disimpan dalam walletjadi.txt{Style.RESET_ALL}")

                # Jeda waktu per wallet
                time.sleep(delay_time)  # Menunggu sesuai waktu yang dimasukkan (dalam detik)

        print(f"{Fore.CYAN}\nSemua wallet telah dibuat dan disimpan dalam walletjadi.txt.{Style.RESET_ALL}")
    
    except Exception as e:
        print(f"{Fore.RED}Terjadi kesalahan saat menyimpan wallet: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
