# Cel: pobieranie danych z API / pliku.
# Powinien mieć klasę Extractor z:
# init(self, cfg: dict)
# fetch(self) -> pd.DataFrame — zwraca surowy DataFrame
# opcjonalne metody prywatne: _from_api(), _from_parquet(), _from_csv()
# Obsługa retrial/backoff, walidacja schematu, logowanie.