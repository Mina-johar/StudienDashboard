# pruefungsleistung.py
from datetime import date

class Pruefungsleistung:
    """
    Repräsentiert eine Prüfungsleistung mit Note, Datum und Status.
    """
    def __init__(self, note: float, datum: date, bestanden: bool):
        self.note: float = note
        self.datum: date = datum
        self.bestanden: bool = bestanden
