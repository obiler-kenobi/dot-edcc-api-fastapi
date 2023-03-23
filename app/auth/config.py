from pydantic import BaseModel

class Settings(BaseModel): #USE PYDANTIC SETTINGS MANAGEMENT WHEN DEPLOYING FOR PRODUCTION
    authjwt_secret_key: str =  "d838ebf914726238d85df4bddcbf5b33d93bc3f2bfcb78a34ef39e1b37ed7be2"
    authjwt_algorithm: str = "H6256"
    authjwt_access_token_expires: int = 15
    authjwt_refresh_token_expires: int = 60 * 2