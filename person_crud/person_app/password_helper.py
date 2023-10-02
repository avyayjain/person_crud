from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# code to verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# code to generate hashed password
def get_password_hash(password):
    return pwd_context.hash(password)


print(get_password_hash("123456"))
