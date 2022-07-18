import os


class Config:
    POSTGRES_URI = os.getenv("POSTGRES_URI")
    API_KEY = os.getenv("API_KEY")
