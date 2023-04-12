import random

def generate_random_file(file_path, size_in_bytes):
    with open(file_path, 'wb') as file:
        chunk_size = 1024 * 1024  # 1 MB
        chunks = size_in_bytes // chunk_size
        
        for i in range(chunks):
            chunk = bytearray(random.getrandbits(8) for _ in range(chunk_size))
            file.write(chunk)
        
        remaining_bytes = size_in_bytes % chunk_size
        if remaining_bytes:
            chunk = bytearray(random.getrandbits(8) for _ in range(remaining_bytes))
            file.write(chunk)
    
    print(f"Utworzono plik o rozmiarze {size_in_bytes} bajtów w ścieżce: {file_path}")

generate_random_file('random_file.bin', 2 * 1024 * 1024 * 1024)