## Filtriranje in Urejanje iCalendar (.ics) Datoteke

Ta Python skripta omogoča filtriranje dogodkov iz .ics datoteke glede na predmete, v katerih si vpisan, ter skupine, ki jim pripadaš. Poleg tega doda vrsto dogodka (predavanje, seminarske vaje ali računalniške vaje) v naslov vsakega dogodka.
Zahteve:

    Python 3.x

Uporaba:

Namestitev: Prepričaj se, da imaš nameščen Python na svojem računalniku. Skripta ne potrebuje dodatnih knjižnic.

Priprava predmeta in skupin: Odpri skripto in v del predmet_skupina dodaj predmete, v katerih si vpisan, ter skupine, ki jim pripadaš. Oblika vnosa je naslednja:

```python

predmet_skupina = {
    "UVOD V PLATFORMNO ODVISEN RAZVOJ APLIKACIJ": "1",
    "PODATKOVNE BAZE I": "1",
    "RAČUNALNIŠKA OMREŽJA": "3",
    "UPORABNIŠKI VMESNIKI": "4",
    "DISKRETNA MATEMATIKA": None,  # Če so vse skupine za predmet, uporabi None
    "OSNOVE STATISTIKE": "3"
}
```

Za vsak predmet je potrebno vnesti ime predmeta, kakor je zapisano v .ics datoteki, in številko skupine, v kateri si (npr. "1" za skupino rv1). Če si v vseh skupinah za določen predmet (npr. predavanja), vpiši None.

Nastavitev vhodne in izhodne datoteke: Vnesi ime datotek, kjer:

    input_file je pot do tvoje izvorne .ics datoteke.
    output_file je ime ali pot do filtrirane .ics datoteke, ki jo bo skripta ustvarila.

```python

input_file = 'urnik.ics'  # Pot do tvoje .ics datoteke
output_file = 'filtriran_urnik.ics'  # Ime nove filtrirane .ics datoteke

```

Zagon skripte: Shrani skripto in zaženi z ukazom v terminalu:

```bash

python filtriraj_urnik.py

```

Po uspešnem zagonu bo skripta ustvarila novo .ics datoteko, kjer so filtrirani dogodki glede na tvoje predmete in skupine. Poleg tega bo vsakemu dogodku v polju SUMMARY dodana vrsta dogodka (Predavanje, Seminarske vaje, Računalniške vaje).

Primer .ics datoteke:

    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:WISE TIMETABLE
    BEGIN:VEVENT
    UID:wtt_um_feri-S-1790-1
    LOCATION:(RU) G2-HERTZ b, 2. nadstropje
    DTSTART:20241001T110000
    DTSTAMP:20241001T110000
    DTEND:20241001T130000
    SUMMARY:PODATKOVNE BAZE I
    DESCRIPTION:PODATKOVNE BAZE I, RV, NIKA JERŠIČ, RIT 2 VS RV 3
    END:VEVENT
    BEGIN:VEVENT
    UID:wtt_um_feri-S-1792-1
    LOCATION:(RU) G2-HERTZ a, 2. nadstropje
    DTSTART:20241001T110000
    DTSTAMP:20241001T110000
    DTEND:20241001T130000
    SUMMARY:PODATKOVNE BAZE I
    DESCRIPTION:PODATKOVNE BAZE I, RV, LUKA HRGAREK, RIT 2 VS RV 1
    END:VEVENT
    BEGIN:VEVENT
    UID:wtt_um_feri-S-1889-1
    LOCATION:G2-P2 BETA, pritličje
    DTSTART:20241001T130000
    DTSTAMP:20241001T130000
    DTEND:20241001T150000
    SUMMARY:UVOD V PLATFORMNO ODVISEN RAZVOJ APLIKACIJ
    DESCRIPTION:UVOD V PLATFORMNO ODVISEN RAZVOJ APLIKACIJ, SV, MIHA RAVBER, RIT 2 VS
    END:VEVENT
    END:VCALENDAR

Opombe:

    Skripta ohranja vse predavanja, saj so ta vedno za vse skupine.
    Računalniške in seminarske vaje pa bodo filtrirane glede na to, ali pripadajo tvoji skupini.