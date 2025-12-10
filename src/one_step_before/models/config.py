from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, model_validator
from typing import Optional
from enum import Enum
from typing_extensions import Self


class DataSource(str, Enum):
    API = "api"
    PARQUET = "parquet"
    CSV = "csv"
    YFINANCE = "yfinance"

class Features(str, Enum):
    NONE = "none"
    ALPHA158 = "alpha158"
    ALPHA360 = "alpha360"
    ALL = "all"

class Timespan(str, Enum):
    SECOND = "second"
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    QUARTER = "quarter"
    YEAR = "year"

class ExtractConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    api_key: Optional[str] = Field(default=None, alias="MASSIVE_API_KEY")
    data_source: DataSource = Field(alias="EXTRACT_DATA_SOURCE")
    ticker: str = Field(default="X:BTCUSD",alias="EXTRACT_TICKER")
    start_date: Optional[str] = Field(default=None, alias="EXTRACT_START_DATE")
    end_date: Optional[str] = Field(default=None, alias="EXTRACT_END_DATE")
    multiplier: int = Field(default=1, alias="EXTRACT_MULTIPLIER")
    timespan: Timespan = Field(default=Timespan.DAY, alias="EXTRACT_TIMESPAN")

    @model_validator(mode="after")
    def check_api_key_when_api(self) -> Self:
        if self.data_source == DataSource.API and not self.api_key:
            raise ValueError("API key must be provided when data source is 'api'")
        return self


class TransformConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    features: Features = Field(alias="TRANSFORM_FEATURES")


