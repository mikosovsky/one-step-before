# Cel: wszystkie operacje I/O w jednym miejscu (testowalne).
# Funkcje:
# read_parquet(path) -> df
# write_parquet(df, path)
# ensure_dir(path)
# atomic_save(df, path) — zapis bez utraty danych
# Obsługa błędów, walidacja ścieżek.