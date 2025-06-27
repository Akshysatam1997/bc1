from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
class RSA_Client:
 def __init__(self, key_size=2048):
  self.key_size = key_size
  self.private_key = None
  self.public_key = None
 def generate_keys(self):
  key = RSA.generate(self.key_size)
  self.private_key = key.export_key()
  self.public_key = key.publickey().export_key()
 def encrypt(self, message):
  cipher = PKCS1_OAEP.new(RSA.import_key(self.public_key))
  encrypted_message = cipher.encrypt(message.encode())
  return encrypted_message
 def decrypt(self, encrypted_message):
  cipher = PKCS1_OAEP.new(RSA.import_key(self.private_key))
  decrypted_message = cipher.decrypt(encrypted_message)
  return decrypted_message.decode()
# Test the RSA client
rsa_client = RSA_Client()
rsa_client.generate_keys()
message = "Hello, RSA!"
print("Original message:", message)
encrypted_message = rsa_client.encrypt(message)
print("Encrypted message:", encrypted_message)
decrypted_message = rsa_client.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message)
