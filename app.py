import os 
import sys
import tkinter as tk
import json

def main():
    if os.path.exists("conti.json"):
        conti=json.load(open("conti.json", "r"))
    else:
        conti={
            "antonio": 100,
            "giuseppe": 200,
            "maria": 350
        }
        json.dump(conti, open("conti.json", "w"))

    clienti=list(conti.keys())   
    finestra=tk.Tk()
    finestra.title("Portafoglio personale")
    finestra.geometry("1920x1080")
    finestra.config(bg="#23272f")
    etichetta=tk.Label(finestra, text="BENVENUTO NEL TUO PORTAFOGLIO PERSONALE!", font=("Verdana",28),bg="#23272f",fg="#D1D5DB", padx=20, pady=20)
    etichetta.pack()
    entry = tk.Entry(finestra, font=("Helvetica", 16),bg="#D1D5DB", fg="#23272f", width=30)
    entry.pack(padx=20, pady=20)
    entry_add=tk.Entry(finestra, font=("Helvetica", 16), bg="#D1D5DB", fg="black")
    entry_minus=tk.Entry(finestra, font=("Helvetica", 16),bg="#D1D5DB", fg="black")
    label_name_currentist=tk.Label(finestra,text=f"Utenti disponibili:{clienti}",font=("Helvetica",16),bg="#23272f",fg="white")
    label_name_currentist.pack()
    label_name_currentist.place(x=10, y=100)
    label_description=tk.Label(finestra, text="Inserisci dettagli :", font=("Helvetica", 16))
    entry_description=tk.Entry(finestra, font=("Helvetica", 16), bg="#D1D5DB", fg="black")
    

    def mostra_saldo():
        nome_correntista = entry.get().strip().lower()
        finestra_nome.pack()
        if not nome_correntista.strip():
            finestra_nome.config(text="Per favore, inserisci il tuo nome.",bg="#23272f", fg="white")
            disponibilita.pack_forget()
        elif nome_correntista in conti:
            saldo=conti[nome_correntista]
            finestra_nome.config(text=f"Ciao, {nome_correntista}!", bg="#23272f", fg="white")
            disponibilita.config(text=f"Il tuo saldo attuale è: {saldo} euro",bg="#23272f", fg="white")
            disponibilita.pack()
            entry_add.pack()
            entry_add.place(x=200,y=300)
            entry_minus.pack()
            entry_minus.place(x=1500,y=300)
            button_add.pack()
            button_add.place(x=290, y=350)
            button_minus.pack()
            button_minus.place(x=1600, y=350)
            label_description.pack()
            label_description.place(x=880, y=250)
            entry_description.pack()
            entry_description.place(x=840, y=300)
        else:
            finestra_nome.config(text="Correntista non trovato.",bg="#23272f", fg="white")
            disponibilita.pack_forget()

    def aggiungi_fondi():
        nome_correntista = entry.get().strip().lower()
        somma=entry_add.get().strip()
        if not nome_correntista:
            finestra_nome.config(text="Per favore, inserisci il tuo nome.")
        if nome_correntista not in conti:
            finestra_nome.config(text="Correntista non trovato.")
        conti[nome_correntista] += int(somma)
        finestra_nome.config(text=f"{nome_correntista} ha aggiunto {somma} euro al suo saldo.")
        disponibilita.config(text=f"Il tuo nuovo saldo è: {conti[nome_correntista]} euro")
        disponibilita.pack()
        dettagli=entry_description.get()
        if dettagli:
            description=tk.Label(finestra, text=f"{nome_correntista} ha aggiunto {somma} euro con descrizione: {dettagli}", font=("Helvetica", 16),bg="#23272f", fg="white")
            description.pack()
            description.place(x=10, y=800)
            open("movimenti.log","a").write(f"{nome_correntista} ha aggiunto {somma} euro con descrizione: {dettagli}\n")
        else:
            description=tk.Label(finestra, text=f"{nome_correntista} ha aggiunto {somma} euro senza descrizione", font=("Helvetica", 16), bg="#23272f", fg="white")
            description.pack()
            description.place(x=10, y=800)
            open("movimenti.log","a").write(f"{nome_correntista} ha aggiunto {somma} euro senza descrizione\n")
        json.dump(conti, open("conti.json", "w"))

    def sottrai_fondi():
        nome_correntista = entry.get().strip().lower()
        somma2=entry_minus.get().strip()
        if not nome_correntista:
            finestra_nome.config(text="Per favore, inserisci il tuo nome.")
        if nome_correntista not in conti:
            finestra_nome.config(text="Correntista non trovato.")
        conti[nome_correntista] -= int(somma2)
        finestra_nome.config(text=f"{nome_correntista} ha sottratto {somma2} euro dal suo saldo.")
        disponibilita.config(text=f"Il tuo nuovo saldo è: {conti[nome_correntista]} euro")
        disponibilita.pack()
        dettagli=entry_description.get()
        if dettagli:
            description=tk.Label(finestra, text=f"{nome_correntista} ha sottratto {somma2} euro con descrizione: {dettagli}", font=("Helvetica", 16), bg="#23272f", fg="white")
            description.pack()
            description.place(x=10, y=800)
            open("movimenti.log","a").write(f"{nome_correntista} ha sottratto {somma2} euro con descrizione: {dettagli}\n")
        else:
            description=tk.Label(finestra, text=f"{nome_correntista} ha sottratto {somma2} euro senza descrizione", font=("Helvetica", 16),bg="#23272f", fg="white")
            description.pack()
            description.place(x=10, y=800)
            open("movimenti.log","a").write(f"{nome_correntista} ha sottratto {somma2} euro senza descrizione\n")
        json.dump(conti, open("conti.json", "w"))


    bottone=tk.Button(finestra, text="Invio", command=mostra_saldo,relief="flat",bg="#D1D5DB", fg="#23272f")
    bottone.pack(padx=20, pady=20)
    finestra_nome=tk.Label(finestra,font=("Helvetica",16))
    disponibilita=tk.Label(finestra, font=("Helvetica", 16))
    button_add=tk.Button(finestra, text="Aggiungi", command=aggiungi_fondi,relief="flat",bg="#D1D5DB", fg="#23272f")
    button_minus=tk.Button(finestra, text="Sottrai", command=sottrai_fondi,relief="flat",bg="#D1D5DB", fg="#23272f")

    finestra.mainloop()


if __name__=="__main__":
    main()
