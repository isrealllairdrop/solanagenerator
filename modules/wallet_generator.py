from solana.keypair import Keypair
from mnemonic import Mnemonic
from file_handler import save_wallet_to_file

def generate_keypair():
    """
    Menghasilkan keypair baru untuk wallet Solana dan mnemonic, serta menyimpan data ke dalam file.
    
    Returns:
        tuple: Public key (base58), Private key (hexadecimal), Mnemonic.
    """
    keypair = Keypair.generate()
    public_key = keypair.public_key.to_base58().decode()  # Public key dalam format base58
    private_key = keypair.secret_key.hex()  # Private key dalam format hexadecimal

    # Menghasilkan mnemonic
    mnemonic = Mnemonic("english").generate()  # Tidak perlu 'entropy' di sini
    
    # Simpan wallet dan mnemonic ke dalam file
    save_wallet_to_file(public_key, private_key, mnemonic)

    return public_key, private_key, mnemonic
