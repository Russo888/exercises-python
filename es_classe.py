class Libro:
    def __init__(titolo, autore, anno, pagine, editore, città, soggetto):
        self.titolo = titolo
        self.autore = autore
        self.anno=anno
        self.pagine=pagine
        self.editore=editore
        self.città=città
        self.soggetto=soggetto
        bool inPrestito=False

    def presta(inPrestito):
        inPrestito=True
    def restituisci(inPrestito):
        inPrestito=False

titolo=str(input("\nInserisci il titolo: "))
autore=str(input("\nInserisci l'autore: "))
anno=str(input("\nInserisci l'anno: "))
pagine=str(input("\nInserisci le pagine: "))
editorestr(input("\nInserisci l'editore: "))
città=str(input("\nInserisci la città: "))
soggetto=str(input("\nInserisci il soggetto: "))

libro=Libro(titolo, autore, anno, pagine, editore, città, soggetto)
