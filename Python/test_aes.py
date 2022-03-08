from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
 
# Valores generados previamente en base64 para que puedan ser almacenables
# Al decodificar estos valores se debe obtener bytes de largo 32 y 16 bits respectivamente
b64_key = 'IvJ2CqXRXHA3tOqy9z0E95gYIrTif0w3JQCl4zpYWlU='
b64_iv = 'gxT1zrBfXC28JC4AvHGkYA=='
 
# Decodificacion de base64 a bytes
key = b64decode(b64_key) # 16 bits (AES-128), 24 (AES-192), or 32 (AES-256)
iv = b64decode(b64_iv) # Para que de el mismo resultado siempre (Largo 16 bits)
 
# -----------------------------------------------------------------------------------------------------
 
# Encriptacion
cipher = AES.new(key, AES.MODE_CBC, iv=iv) # Create a AES cipher object with the key using the mode CBC
ciphered_data = cipher.encrypt(pad(data.encode(), AES.block_size))
 
# Desencriptacion
cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher
original_data = unpad(cipher.decrypt(b64decode(data)), AES.block_size)