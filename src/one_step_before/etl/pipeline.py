# Cel: orkiestracja całego procesu.
# Klasa ETLPipeline lub funkcja run_pipeline(cfg):
# inicjalizuje Extractor, Transformer, I/O
# wykonuje fetch -> clean -> features -> save (do data/silver, data/gold)
# zwraca finalny df lub zapisuje lokalnie
# Obsługa try/except, retry, zapisywanie checkpointów i logging.