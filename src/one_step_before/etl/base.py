# Cel: interfejs / klasa bazowa dla komponentów ETL.
# Powinno zawierać abstrakcyjną klasę (ABC) BaseETL z metodami:
# fetch(self) -> pd.DataFrame (opcjonalnie dla Extractor)
# transform(self, df: pd.DataFrame) -> pd.DataFrame (dla Transformer)
# save(self, df: pd.DataFrame) -> None
# run(self) -> pd.DataFrame (opcjonalny helper orchestration)
# Dokumentacja wymagań wejścia/wyjścia i standardowych wyjątków.