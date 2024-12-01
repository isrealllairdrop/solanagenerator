# file_handler.py
def save_wallet_to_file(public_key, private_key, filename="walletjadi.txt"):
    """
    Menyimpan alamat (public key) dan kunci privat ke dalam file.
    
    Args:
        public_key (str): Alamat public key Solana dalam format base58.
        private_key (str): Kunci privat dalam format hexadecimal.
        filename (str): Nama file tempat menyimpan data wallet.
    """
    with open(filename, "w") as file:
        file.write(f"Alamat Solana: {public_key}\n")
        file.write(f"Private Key: {private_key}\n")
    print(f"Wallet berhasil disimpan ke {filename}")
