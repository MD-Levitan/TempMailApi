from Crypto.Hash import MD5
import base64

def encrypt(value: str, xor_value: int = 1573252) -> str:
    """! Encrypt str. """
    hash = MD5.new(value.encode("utf-8")).digest()
    hash_str = hash.hex()

    xored = "".join(map(lambda x: chr((ord(x) ^ (xor_value & 0xFFFF))), hash_str))
    return base64.b64encode(xored.encode("utf-8")).decode("utf-8")


def b64encode(value: str) -> str:
    return base64.b64decode(value.encode("utf-8")).decode("utf-8") 