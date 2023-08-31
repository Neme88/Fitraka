# utils.py

from passlib.hash import sha256_crypt

def hash_password(password):
    # Hash the provided password
    return sha256_crypt.hash(password)

def verify_password(entered_password, hashed_password):
    # Verify the entered password against the hashed password
    return sha256_crypt.verify(entered_password, hashed_password)

