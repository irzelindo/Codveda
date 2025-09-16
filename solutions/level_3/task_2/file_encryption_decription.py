from cryptography.fernet import Fernet

KEY_FILE = "secret.key"

def generate_key():
    """
    Generates a Fernet key and saves it to the file specified by KEY_FILE.

    The key is generated using Fernet.generate_key() and is saved to the file in binary format.
    A message is printed to the console indicating that the key has been generated and saved.
    """
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    print("Key generated and saved to secret.key")

def load_key():
    """
    Loads a Fernet key from the file specified by KEY_FILE.

    The key is read from the file in binary format and returned as a bytes object.

    If the file does not exist, FileNotFoundError is raised.

    Returns:
        bytes: The Fernet key loaded from the file.
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    return open(KEY_FILE, "rb").read()

def encrypt_file(filename):
    """
    Encrypts a file using a Fernet key.

    The file is read in binary format and encrypted using Fernet.encrypt(). The encrypted data is then written to a new file with the same name as the input file but with a ".enc" extension.

    Args:
        filename (str): The name of the file to encrypt.

    Returns:
        None
    """
    fernet = Fernet(load_key())
    with open(filename, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(filename + ".enc", "wb") as f:
        f.write(encrypted)
    print(f"Encrypted file saved as {filename}.enc")

def decrypt_file(filename):
    """
    Decrypts a file using a Fernet key.

    The file is read in binary format and decrypted using Fernet.decrypt(). The decrypted data is then written to a new file with the same name as the input file but with a ".dec" extension.

    Args:
        filename (str): The name of the file to decrypt.

    Returns:
        None
    """
    fernet = Fernet(load_key())
    with open(filename, "rb") as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    output_file = filename.replace(".enc", ".dec")
    with open(output_file, "wb") as f:
        f.write(decrypted)
    print(f"Decrypted file saved as {output_file}")



if __name__ == "__main__":
    generate_key()
    encrypt_file("data.txt")
    decrypt_file("data.txt.enc")