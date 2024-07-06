from bcrypt import hashpw, gensalt

def hash_password(password):
   password_bytes = password.encode('utf-8')
   generate_salt = gensalt()
   hashed_bytes = hashpw(password_bytes, generate_salt)
   return f"{hashed_bytes.decode('utf-8')}:{generate_salt}"

def verify_password(password, hash_password):
   hash_code, salt = hash_password.split(':')
#    print(password)
#    print(hash_password)
#    print(hash_code)
#    print(salt)
   return (hash_code == hashpw(password.encode('utf-8'), salt.encode('utf-8')).decode('utf-8'))
