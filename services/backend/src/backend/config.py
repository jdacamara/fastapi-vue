from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import HttpUrl, field_validator
from typing import List


class Settings(BaseSettings):
    front_end_origins: str

    model_config = SettingsConfigDict(env_file=".env")

    # Validation of the environment variable
    @field_validator("front_end_origins")
    @classmethod
    def validate_origins(cls, v: str) -> str:
        origins = [origin.strip() for origin in v.split(",")]

        # Validate each URL
        for origin in origins:
            HttpUrl(origin)  # will raise ValidationError if invalid

        return v

    # Create a new property of type list of front_end_origins
    @property
    def front_end_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.front_end_origins.split(",")]


settings = Settings()
