import bcrypt

#salt = bcrypt.gensalt()
# TBD: temporal hack to demo password protection for experiments
#salt = bcrypt.gensalt()

pwd = input('Password: ')
pwd = pwd.strip()

password_salt = b'$2b$12$ionIRWe5Ft7jkn4y/7C6/e'
password_hash2 = bcrypt.hashpw(pwd.encode('utf-8'), password_salt)

print ('"password_hash":"{}"'.format(password_hash2.decode('utf-8')))
