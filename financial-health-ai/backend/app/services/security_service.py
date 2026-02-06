from cryptography.fernet import Fernet
import os

# Keep this constant once generated
SECRET_KEY = os.getenv(
    "FINANCIAL_SECRET_KEY",
    "6IYJqRkQX0dR8cYqYJkz4WjPp9hYV9H5wM2Xc1o8ZzU="
)

cipher = Fernet(SECRET_KEY.encode())


def encrypt_value(value):
    if value is None:
        return None
    return cipher.encrypt(str(value).encode()).decode()


def decrypt_value(value):
    if value is None:
        return None
    return cipher.decrypt(value.encode()).decode()
