import re

def filtriraj_ics(input_file, output_file, predmet_skupina):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    filtrirane_vrstice = []
    is_event = False
    current_event = []
    current_predmet = None
    vrsta_dogodka = None

    for line in lines:
        if line.startswith("BEGIN:VEVENT"):
            is_event = True
            current_event = []
            current_predmet = None
            vrsta_dogodka = None
        
        if is_event:
            current_event.append(line)
            
            # Prepozna ime predmeta iz SUMMARY vrstice
            if line.startswith("SUMMARY:"):
                current_predmet = line.split("SUMMARY:")[1].strip()

            # Prepozna vrsto dogodka iz DESCRIPTION (PR, SV, RV)
            if line.startswith("DESCRIPTION:"):
                description = line.split("DESCRIPTION:")[1].strip()
                if "PR" in description:
                    vrsta_dogodka = "Predavanje"
                elif "SV" in description:
                    vrsta_dogodka = "Seminarske vaje"
                elif "RV" in description:
                    vrsta_dogodka = "Računalniške vaje"

        if line.startswith("END:VEVENT"):
            is_event = False
            event_description = ''.join(current_event)
            
            if current_predmet:
                # Preveri, ali gre za predavanje ali vajo
                if "RIT 2 VS" in event_description:
                    if "RV" in event_description:
                        # Preveri številko skupine za specifičen predmet
                        match = re.search(r'RV (\d+)', event_description)
                        if match:
                            skupina = match.group(1)
                            # Preveri, če predmet obstaja v naši tabeli in skupina ustreza
                            if current_predmet in predmet_skupina and predmet_skupina[current_predmet] == skupina:
                                # Dodaj vrsto dogodka v naslov (SUMMARY)
                                current_event = dodaj_vrsto_v_summary(current_event, vrsta_dogodka)
                                filtrirane_vrstice.extend(current_event)
                    else:
                        # Če ni označena z RV (je predavanje), ohrani in dodaj vrsto
                        current_event = dodaj_vrsto_v_summary(current_event, vrsta_dogodka)
                        filtrirane_vrstice.extend(current_event)

    # Zapiši filtrirane dogodke v novo datoteko
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:WISE TIMETABLE\n")
        f.writelines(filtrirane_vrstice)
        f.write("END:VCALENDAR\n")

def dodaj_vrsto_v_summary(event_lines, vrsta):
    """Dodaj vrsto dogodka (predavanje, seminarske, vaje) v polje SUMMARY."""
    for i, line in enumerate(event_lines):
        if line.startswith("SUMMARY:"):
            predmet = line.split("SUMMARY:")[1].strip()
            nova_summary = f"SUMMARY:{predmet} ({vrsta})\n"
            event_lines[i] = nova_summary
    return event_lines

# Definiraj predmete in njihove skupine
predmet_skupina = {
    "UVOD V PLATFORMNO ODVISEN RAZVOJ APLIKACIJ": "1",
    "PODATKOVNE BAZE I": "1",
    "RAČUNALNIŠKA OMREŽJA": "3",
    "UPORABNIŠKI VMESNIKI": "4",
    "DISKRETNA MATEMATIKA": None,
    "OSNOVE STATISTIKE": "3"
}

input_file = 'calendar.ics'  # Pot do tvoje .ics datoteke
output_file = 'filtriran_urnik.ics'  # Ime nove filtrirane .ics datoteke

filtriraj_ics(input_file, output_file, predmet_skupina)
