import toml
from pydantic_settings import BaseSettings



class GeneralSettings(BaseSettings):
    debug: bool
    port: int


class DatabaseSettings(BaseSettings):
    host: str
    name: str
    user: str
    password: str
    port: int


class Settings(BaseSettings):

    general: GeneralSettings
    database: DatabaseSettings

    @classmethod
    def from_toml(cls, toml_file):
        config = toml.load(toml_file)
        
        # Extract section from toml 
        general_config = config.get("general", {})
        database_config = config.get("database", {})
        
        return cls(
            general=GeneralSettings(**general_config),
            database=DatabaseSettings(**database_config)
        )