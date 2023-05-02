# FastAPI
Build Python web development with Fast API


# Create database with alembic upgrade

First run alembic upgrade for task table -> user -> company

# Note on MacOS
MacOS cann't run this code:


from passlib.context import CryptContext

bcrypt_context = CryptContext(schemes=["bcrypt"])


################################ 

So, we replace by:

from passlib.hash import pbkdf2_sha256
