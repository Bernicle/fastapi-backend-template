from bcrypt import hashpw, gensalt

def hash_password(password : str) -> str:
   password_bytes = password.encode('utf-8')
   generate_salt = gensalt()
   hashed_bytes = hashpw(password_bytes, generate_salt)
   return f"{hashed_bytes.decode('utf-8')}:{generate_salt.decode('utf-8')}"

def verify_password(password : str, hash_password : str) -> bool:
   hash_code, salt = hash_password.split(':')
   return (hash_code == hashpw(password.encode('utf-8'), salt.encode('utf-8')).decode('utf-8'))
