# wallet_generator/__init__.py
from solana.keypair import Keypair

def generate_keypair():
    """
    Menghasilkan keypair baru untuk wallet Solana.
    
    Returns:
        tuple: Public key (base58), Private key (hexadecimal).
    """
    keypair = Keypair.generate()
    public_key = keypair.public_key.to_base58().decode()  # Public key dalam format base58
    private_key = keypair.secret_key.hex()  # Private key dalam format hexadecimal
    
    return public_key, private_key
