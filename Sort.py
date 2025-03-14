#!/usr/bin/env python3


import os
import shutil
from argparse import ArgumentParser

def make_dir(datei, verzeichnis, faktor):                                #erstellt Ordner entweder nach Name oder Art der Daatei, und verschiebt die datein in die Richtigen ordner
    try:
        
        ziel_ordner = os.path.join(verzeichnis, faktor[1:] if faktor[0] == '.' else faktor)
        os.makedirs(ziel_ordner, exist_ok=True)
        ziel_datei = os.path.join(ziel_ordner, datei)
        shutil.move(datei, ziel_datei)
    except Exception as e:
        print(f'Fehler beim verschieben von {datei}: {e}')

def daten_auslesen(daten, verzeichnis, wahl):                           #liest die datein im verzeichnis aus.
    for datei in daten:
        if os.path.isfile(datei):
            try: 
                name, art = os.path.splitext(datei)
            except NameError:
                pass
            if wahl:
                make_dir(datei, verzeichnis, name )
            else:
                make_dir(datei, verzeichnis, art)   
        else:
            pass

def nach_namen_sortieren():
    pass


def main():

    parser = ArgumentParser(description='Sortiert die Datein in verschiedene Ordner')
    parser.add_argument( '-n', '--name', action='store_true', help='Sortiert das die Datein nach Namen ')
    parser.add_argument( '-d', '--dictionary', help='Sortiert angegebenes Verzeichnis (Dictionary) auf')
    
    args = parser.parse_args()

    aktuelles_verzeichnis = os.getcwd()

    if args.dictionary:
        verzeichnis = os.listdir(args.dictionary)
    else:
        verzeichnis = aktuelles_verzeichnis
    
    dateien = os.listdir(verzeichnis)

    if args.name:                                           #prüft ob der Parameter '--name' benutzt wurde
        daten_auslesen(dateien, verzeichnis, True)
    else:
        daten_auslesen(dateien, verzeichnis, False)    
    


if __name__ == '__main__':
    main()