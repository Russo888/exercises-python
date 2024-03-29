import pyperclip

pwd = {
    'facebook': '123',
    'instagram': '999',
    'youtube': '000',
    }

print("Quale password ti interessa?")
for sito in pwd:
    print(" -", sito)

sito_scelto = input("Inserisci il sito : ")

try:
    passwd_scelta = pwd[sito_scelto]
    pyperclip.copy(passwd_scelta)
    print("\nPassword trovata! Puoi incollarla sul sito")
    input()
except:
    print("Sito non trovato!!!")
    input()


"""pip install pyperclip"""
