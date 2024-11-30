# format_converter/__init__.py
import base58

def convert_private_key_to_base58(private_key_hex):
    """
    Mengonversi kunci privat dari hexadecimal ke format base58.
    
    Args:
        private_key_hex (str): Kunci privat dalam format hexadecimal.
        
    Returns:
        str: Kunci privat dalam format base58.
    """
    private_key_bytes = bytes.fromhex(private_key_hex)
    private_key_base58 = base58.b58encode(private_key_bytes).decode()
    return private_key_base58

def convert_public_key_to_base58(public_key_hex):
    """
    Mengonversi kunci publik ke dalam format base58.
    
    Args:
        public_key_hex (str): Kunci publik dalam format hexadecimal.
        
    Returns:
        str: Kunci publik dalam format base58.
    """
    public_key_bytes = bytes.fromhex(public_key_hex)
    public_key_base58 = base58.b58encode(public_key_bytes).decode()
    return public_key_base58
