import os
import hashlib
import base58
from ecdsa import SigningKey, SECP256k1

def generate_wallet():
    # 1. Private Key Generate karna
    private_key = os.urandom(32)
    
    # 2. Public Key Generate karna (using SECP256k1 curve)
    sk = SigningKey.from_string(private_key, curve=SECP256k1)
    vk = sk.get_verifying_key()
    public_key = b'\x04' + vk.to_string()
    
    # 3. Public Address banana (Hashing)
    sha256_pk = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_pk)
    hashed_pk = ripemd160.digest()
    
    # Add network byte (0x00 for Bitcoin Mainnet)
    full_hash = b'\x00' + hashed_pk
    
    # Checksum calculation
    checksum = hashlib.sha256(hashlib.sha256(full_hash).digest()).digest()[:4]
    address = base58.b58encode(full_hash + checksum).decode('utf-8')

    # 4. Result dikhana aur file mein save karna
    wallet_art = f"""
    ***************************************************
    * CRYPTO PAPER WALLET (BTC)             *
    ***************************************************
    * *
    * PUBLIC ADDRESS:                                *
    * {address}           *
    * *
    * PRIVATE KEY (KEEP SECRET!):                    *
    * {private_key.hex()}    *
    * *
    ***************************************************
    """
    print(wallet_art)
    
    with open("paper_wallet.txt", "w") as f:
        f.write(wallet_art)
    print("✅ Wallet saved to paper_wallet.txt")

if __name__ == "__main__":
    generate_wallet()
