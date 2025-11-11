# main.py
from entities.studiengang import Studiengang
from entities.semester import Semester
from entities.modul import Modul
from datetime import date

def main():
    # Studiengang anlegen
    studiengang = Studiengang("Informatik", 180)

    # 1. Semester anlegen
    semester_1 = Semester(1)
    studiengang.add_semester(semester_1)

    # Beispiel-Module (Name, ECTS, Note, Datum, bestanden)
    module_daten = [
        ("Programmierung", 5, 2.3, "2025-03-15", True),
        ("Mathematik",     5, 1.7, "2025-03-20", True),
        ("Künstliche Intelligenz", 5, 2.0, "2025-04-10", True),
    ]

    for name, ects, note, datum_str, bestanden in module_daten:
        m = Modul(name, ects)
        # String in date umwandeln
        year, month, day = map(int, datum_str.split('-'))
        datum_obj = date(year, month, day)
        m.set_pruefungsleistung(note, datum_obj, bestanden)
        semester_1.add_modul(m)

    # Ausgabe
    print("=== Machbarkeitstest: Dashboard-Prototyp ===")
    print(f"Studiengang: {studiengang.name}")
    avg = studiengang.berechne_notendurchschnitt()
    print(f"Notendurchschnitt: {avg:.2f}" if avg is not None else "Notendurchschnitt: -")
    ects, prozent = studiengang.berechne_fortschritt()
    print(f"ECTS-Fortschritt: {ects}/{studiengang.gesamt_ects} ({prozent:.1f}%)")

if __name__ == "__main__":
    main()
