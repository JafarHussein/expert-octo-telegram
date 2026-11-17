from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL:str
    
    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )
# Creating an instance of the class Settings allows us to access environment variables through the instance of settings
settings=Settings()