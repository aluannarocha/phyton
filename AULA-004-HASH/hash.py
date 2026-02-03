# -> hashear
# 1 pedimos a password
# 2 calculamos a hash da password
# 3 guardamos o hash

# -> desashear
# 1 pedimos o password
# 2 passamos o hash da password registada
# 3 ele analisa ambas e retorna ou True ou uma exceção

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

def criar_hash (password: str) -> str:
    ph = PasswordHasher()

    hash = ph.hash(password) # utiliza o metodo para hashear

    return hash # retorna o hash

def login(tentativa, hash_db):
    ph = PasswordHasher()

    try:
        ph.verify(hash_db, tentativa)

    except VerifyMismatchError:
        print('Password inválida')

    else:
        print ('Login Bem sucedido!')

palavra_passe='123456789'
hash = criar_hash (palavra_passe)
login_pass = input ('Password: ')
login(login_pass,hash)




palavra_passe = input('Digite um password: ')
print(criar_hash(palavra_passe))