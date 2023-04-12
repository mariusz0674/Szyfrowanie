from Crypto.Cipher import DES3

import enum
import time

@enum.unique
class CryptMode(enum.Enum):
    MODE_ECB = DES3.MODE_ECB
    MODE_CBC = DES3.MODE_CBC
    MODE_CFB = DES3.MODE_CFB
    MODE_OFB = DES3.MODE_OFB
    MODE_CTR = DES3.MODE_CTR

def compare_files(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            byte1 = f1.read(4096)
            byte2 = f2.read(4096)
            if byte1 != byte2:
                return False
            if not byte1:
                return True

def encrypt_file(input_file_path, output_file_path, key, crypt_mode):
    if(crypt_mode == CryptMode.MODE_CTR.value):
        cipher = DES3.new(key, crypt_mode, nonce=b"")
    else:
        cipher = DES3.new(key, crypt_mode)

    # Otwórz plik wejściowy i wczytaj jego zawartość
    with open(input_file_path, 'rb') as input_file:
        input_data = input_file.read()

    # Zaszyfruj dane
    encrypted_data = cipher.encrypt(input_data)
    # Zapisz zaszyfrowane dane do pliku wyjściowego
    with open(output_file_path, 'wb') as output_file:
        output_file.write(encrypted_data)
    print(f"Utworzono zaszyfrowany plik w sciezce: {output_file_path}")


def decode_file(input_file_path, output_file_path, key, crypt_mode):
    if(crypt_mode == CryptMode.MODE_CTR.value):
        cipher = DES3.new(key, crypt_mode, nonce=b"")
    else:
        cipher = DES3.new(key, crypt_mode)

    with open(input_file_path, 'rb') as input_file:
        input_data = input_file.read()

    decrypt_data = cipher.decrypt(input_data)
    
    with open(output_file_path, 'wb') as output_file:
        output_file.write(decrypt_data)
    print(f"Utworzono zdeszyfrowany plik w sciezce: {output_file_path}")

key = b'1234567890123456'

encodeTimes = {}
decodeTimes = {}
for cryptMode in CryptMode.__members__.values():
    print(cryptMode.name)
    stoper = time.time()
    encrypt_file('random_file.bin', 'encrypted_file.bin', key, cryptMode.value)
    encodeTimes[cryptMode.name] = abs(stoper - time.time())
    print(abs(stoper - time.time()))
    stoper = time.time()
    decode_file('encrypted_file.bin', 'random_file1.bin', key, cryptMode.value)
    decodeTimes[cryptMode.name]= abs(stoper - time.time())
    print(abs(stoper - time.time()))
