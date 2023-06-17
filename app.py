import hashlib

def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash

# Usage example
file_path = 'text.txt'
md5 = calculate_md5(file_path)
print("File MD5 hash:", md5)
