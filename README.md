# Mini-system liczb egzotycznych / Exotic Number System Toolkit

## Spis treści / Table of Contents
1. [Cel projektu / Project Objective](#cel-projektu--project-objective)
2. [Potrzeby biznesowe / Business Needs](#potrzeby-biznesowe--business-needs)
3. [Punkty akceptacji / Acceptance Criteria](#punkty-akceptacji--acceptance-criteria)
4. [Wymagania techniczne / Technical Requirements](#wymagania-techniczne--technical-requirements)
5. [Obsługiwane systemy liczbowe / Supported Numeral Systems](#obsługiwane-systemy-liczbowe--supported-numeral-systems)
6. [Przykładowa interakcja / Sample Interaction](#przykładowa-interakcja--sample-interaction)
7. [Moduły i struktura / Modules and Structure](#moduły-i-struktura--modules-and-structure)
8. [Możliwości rozwoju / Potential Extensions](#możliwości-rozwoju--potential-extensions)

---

## Cel projektu / Project Objective

**PL:**  
Celem projektu jest stworzenie interaktywnego narzędzia w trybie tekstowym (CLI), które umożliwia konwersję i operacje arytmetyczne na liczbach zapisanych w różnych, nietypowych systemach liczbowych (np. binarnym, szesnastkowym, rzymskim). Aplikacja ułatwi zrozumienie konwersji oraz sposobu reprezentowania danych w systemach informatycznych i historycznych.

**EN:**  
The goal of the project is to create an interactive command-line tool that enables conversion and arithmetic operations on numbers represented in various exotic numeral systems (e.g., binary, hexadecimal, Roman numerals). The application helps users understand data representation in both computational and historical contexts.

---

## Potrzeby biznesowe / Business Needs

**PL:**  
Projekt odpowiada na potrzebę edukacyjnego narzędzia, które umożliwia naukę systemów liczbowych oraz operacji na nich w sposób praktyczny i przejrzysty. Może być wykorzystany przez:
- studentów informatyki i matematyki
- nauczycieli i edukatorów
- programistów uczących się niskopoziomowego przetwarzania danych
- hobbystów zainteresowanych systemami zapisu

**EN:**  
This project meets the need for an educational tool that facilitates the practical and transparent learning of numeral systems and operations. Potential users include:
- computer science and mathematics students
- teachers and educators
- programmers learning low-level data handling
- enthusiasts of historical or exotic numeral systems

---

## Punkty akceptacji / Acceptance Criteria

- Użytkownik może wybrać system źródłowy i docelowy
- Program poprawnie konwertuje liczby między systemami
- Program wykonuje działania arytmetyczne w wybranym systemie i zwraca wynik w tym systemie
- Działania uwzględniają konwersję pośrednią przez system dziesiętny
- Obsługiwane są błędy wejściowe i niepoprawne formaty
- Interfejs tekstowy jest czytelny i przyjazny

---

## Wymagania techniczne / Technical Requirements

- Python 3.8+
- Brak konieczności użycia zewnętrznych bibliotek (chyba że dla GUI lub rozszerzeń)
- Aplikacja uruchamiana z poziomu terminala
- Kod podzielony na moduły/funkcje
- Struktura projektu zgodna z dobrymi praktykami Pythona
- Wersja podstawowa w trybie tekstowym (CLI)

---

## Obsługiwane systemy liczbowe / Supported Numeral Systems

| System               | Przykład zapisu      | Zakres podstawowy |
|----------------------|----------------------|-------------------|
| Dziesiętny (DEC)     | 42                   | pełne wsparcie    |
| Binarny (BIN)        | 0b101010             | pełne wsparcie    |
| Ósemkowy (OCT)       | 0o52                 | opcjonalny        |
| Szesnastkowy (HEX)   | 0x2A                 | pełne wsparcie    |
| Rzymski (ROMAN)      | XLII                 | ograniczenie: max 3999 |

---

## Przykładowa interakcja / Sample Interaction

**Tryb konwersji / Conversion Mode:**

```
Wybierz system źródłowy: HEX
Podaj liczbę: 0x2A
Wybierz system docelowy: ROMAN
Wynik: XLII
```

**Tryb kalkulatora / Calculator Mode:**

```
Wybierz system: BIN
Podaj działanie: 0b1101 + 0b10
Wynik: 0b1111
```

**Obsługa błędu / Error Handling:**

```
Wybierz system źródłowy: ROMAN
Podaj liczbę: ABC
Błąd: Niepoprawna liczba w systemie rzymskim.
```

---

## Moduły i struktura / Modules and Structure

**Propozycja struktury plików:**

```
exotic_calc/
│
├── main.py                # Punkt wejściowy CLI
├── converter.py           # Funkcje konwertujące między systemami
├── calculator.py          # Operacje arytmetyczne i parser
├── roman_utils.py         # Obsługa systemu rzymskiego
└── utils.py               # Walidacja i pomocnicze funkcje
```

**Główne funkcje:**

- `convert(number: str, from_system: str, to_system: str) -> str`
- `evaluate(expr: str, system: str) -> str`
- `roman_to_decimal(s: str) -> int`
- `decimal_to_roman(n: int) -> str`
- `validate_input(number: str, system: str) -> bool`

---

## Możliwości rozwoju / Potential Extensions

**PL:**
- Dodanie obsługi liczb zmiennoprzecinkowych
- Obsługa liczb ujemnych i działań bitowych (np. XOR, NOT)
- GUI w tkinter/HTML+JS do nauki w formie wizualnej
- Historia działań i zapisywanie wyników do pliku
- Dodanie niestandardowych systemów liczbowych (np. 3-kowy, 12-kowy)

**EN:**
- Support for floating-point numbers
- Negative number handling and bitwise operations (e.g., XOR, NOT)
- GUI (tkinter or HTML+JS) for visual learning
- Operation history and file-based result logging
- Addition of custom numeral systems (e.g., base-3, base-12)
