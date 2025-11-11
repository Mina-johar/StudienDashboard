# studiengang.py
from __future__ import annotations
from typing import List, Optional
from entities.semester import Semester

class Studiengang:
    """Repräsentiert einen Studiengang mit mehreren Semestern."""

    def __init__(self, name: str, gesamt_ects: int):
        self.name: str = name
        self.gesamt_ects: int = gesamt_ects
        self.semester: List[Semester] = []

    def add_semester(self, semester: Semester) -> None:
        """Fügt dem Studiengang ein Semester hinzu."""
        self.semester.append(semester)

    def berechne_notendurchschnitt(self) -> Optional[float]:
        """Berechnet den Durchschnitt aller Prüfungsnoten."""
        noten: List[float] = []
        for sem in self.semester:
            for mod in sem.module:
                pl = getattr(mod, "pruefungsleistung", None)
                if pl is not None and pl.note is not None:
                    noten.append(pl.note)
        return round(sum(noten) / len(noten), 2) if noten else None

    def berechne_fortschritt(self) -> tuple[int, float]:
        """Berechnet die erreichten ECTS in Anzahl und Prozent."""
        ects_summe = 0
        for sem in self.semester:
            for mod in sem.module:
                pl = getattr(mod, "pruefungsleistung", None)
                if pl is not None and getattr(pl, "bestanden", False):
                    ects_summe += mod.ects
        prozent = round((ects_summe / self.gesamt_ects) * 100, 1) if self.gesamt_ects > 0 else 0.0
        return ects_summe, prozent
