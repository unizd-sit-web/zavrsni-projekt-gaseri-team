# Opis projekta
Napravili smo web aplikaciju "izmišljenog noćnog kluba". (Razlog je što kolega Bucić radi za noćni klub Opera kao lightman, a kolega Zubčić kao fotograf te smo koristili slike i ideje kako bi izgledala web stranica noćnog kluba Opera)

Glavna mogučnost aplikacije je rezervacija stola u klubu pomoću web forme. Podaci o rezervaciji upisuju se u MySQL bazu podataka te se korisniku šalje potvrda o rezervaciji. Osim toga, dodali smo mogučnost pretplate na newsletter gdje se također podaci (točnije e-mail adresa) upisuje u bazu podataka, a korisniku se šalje potvrda na mail. U aplikaciji postoji mogučnost i toga da se korisnik obrati "osoblju" kluba koristeći kontakt formu na dnu svake stranice.

Baza podataka se nalazi na besplatnom hosting servisu (https://www.freemysqlhosting.net/), a podaci za pristup se mogu naći u kodu aplikacije. Osim toga, koristili smo i MySQL Workbench za lakše snalaženje s bazom. Za slanje mailova koristili smo gmail.
NAPOMENA: Pošto je google prije nekoliko dana ukinuo pristup manje sigurnim aplikacijama, morali smo koristiti generiranje zaporaka za aplikacije.
Još jedna NAPOMENA: Stranica galerije nekad učita slike odmah, a nekad tek nakon što se stranica refresha (nije nam jasno zašto :D)

EDIT: Promijenili smo da aplikacija koristi SQLite bazu podataka umjesto MySql jer nam je istekao besplatni hosting za MySql bazu.

## Upute za pokretanje putem terminala:
**1. python -m venv venv**

**2. venv/Scripts/Activate.ps1** 

**3. pip install -r requirements.txt**

**4. python app.py**
