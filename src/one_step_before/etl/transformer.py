# Cel: czyszczenie, indeksowanie, kalkulacja cech (alpha158/alpha360).
# Klasa Transformer:
# init(self, cfg: dict)
# clean_index(self, df) -> df (ustawienie daty, drop kolumn)
# compute_features(self, df) -> df (wszystkie cechy)
# ew. mniejsze prywatne metody compute_alpha158, compute_alpha360
# Nie mutuje wejściowego df (kopiuje), używa konfigurowalnych okien, min_periods, loguje problemy.