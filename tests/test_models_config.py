import pytest
import importlib
from src.one_step_before.models.config import ExtractConfig

def test_api_requires_api_key(monkeypatch):
    monkeypatch.setenv("EXTRACT_DATA_SOURCE", "api")
    monkeypatch.setenv("MASSIVE_API_KEY", "")
    
    with pytest.raises(ValueError):
        ExtractConfig()

def test_parquet_does_not_require_api_key(monkeypatch):
    monkeypatch.setenv("EXTRACT_DATA_SOURCE", "parquet")
    monkeypatch.setenv("MASSIVE_API_KEY", "")
    config = ExtractConfig()
    assert config.data_source == "parquet"

def test_csv_does_not_require_api_key(monkeypatch):
    monkeypatch.setenv("EXTRACT_DATA_SOURCE", "csv")
    monkeypatch.setenv("MASSIVE_API_KEY", "")
    config = ExtractConfig()
    assert config.data_source == "csv"
