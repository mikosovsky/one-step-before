from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, model_validator
from typing import Optional
from enum import Enum
from typing_extensions import Self

class DataSource(str, Enum):
    API = "api"
    PARQUET = "parquet"
    CSV = "csv"

class ExtractConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    api_key: Optional[str] = Field(default=None, alias="MASSIVE_API_KEY")
    data_source: DataSource = Field(alias="EXTRACT_DATA_SOURCE")

    @model_validator(mode="after")
    def check_api_key_when_api(self) -> Self:
        if self.data_source == DataSource.API and not self.api_key:
            raise ValueError("API key must be provided when data source is 'api'")
        return self
