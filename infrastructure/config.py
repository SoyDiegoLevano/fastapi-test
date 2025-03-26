# infrastructure/config.py

import os

SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 1))

DATABASE_URL = os.getenv("DATABASE_URL", "dbname=bd-test user=postgres password=postgres host=localhost")
