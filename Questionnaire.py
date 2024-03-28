from tkinter import *
from tkinter import ttk

#Start python in terminal : % ./python.exe
#Commandes : bg -> background ; fg -> foreground
#Voir quand finis avec CustomTkinter pour voir si c'est beaux

"""
def PhotosNiv1():
    img1 = PhotoImage(window3, file='')

"""


#Création de la fênetre 3
def Niveau1():
    window2.destroy() #ferme la fenêtre 2
    window3 = Tk()
    window3.geometry('1000x650') #x * y
    window3.title('Niveau 1')
    window3['bg'] = '#ffc765' 
    window3.resizable(height=False, width=False) #supprime la possibilité de resize

    buttonV = Button(window3, text="Vrai", bg='white', fg='black', font=("Verdana", 15, "bold"))
    buttonV.place(x='350', y='550')
    buttonV.config(width=5, height=2)
    buttonF = Button(window3, text="Faux", bg='white', fg='black', font=("Verdana", 15, "bold"))
    buttonF.place(x='550', y='550')  
    buttonF.config(width=5, height=2)

#Création de la fênetre 4
def Niveau2():
    window2.destroy() #ferme la fenêtre 2
    window4 = Tk()
    window4.geometry('1000x650') #x * y
    window4.title('Niveau 2')
    window4['bg'] = '#ffc765' 
    window4.resizable(height=False, width=False) #supprime la possibilité de resize

    buttonV = Button(window4, text="Vrai", bg='white', fg='black', font=("Verdana", 15, "bold"))
    buttonV.place(x='350', y='550')
    buttonV.config(width=5, height=2)
    buttonF = Button(window4, text="Faux", bg='white', fg='black', font=("Verdana", 15, "bold"))
    buttonF.place(x='550', y='550')  
    buttonF.config(width=5, height=2)

#Création de la fênetre 5
def Niveau3():
    window2.destroy() #ferme la fenêtre 2
    window5 = Tk()
    window5.geometry('1000x650') #x * y
    window5.title('Niveau 3')
    window5['bg'] = '#ffc765' 
    window5.resizable(height=False, width=False) #supprime la possibilité de resize

    buttonV = Button(window5, text="Vrai", bg='white', fg='black', font=("Verdana", 15, "bold"))
    buttonV.place(x='350', y='550')
    buttonV.config(width=5, height=2)
    buttonF = Button(window5, text="Faux", bg='white', fg='black', font=("Verdana", 15, "bold"))
    buttonF.place(x='550', y='550')  
    buttonF.config(width=5, height=2)

#Création de la fênetre 2
def Pchoix_du_niv():
    global window2
    window1.destroy() #ferme la fenêtre 1
    window2 = Tk()
    window2.geometry('1000x650') #x * y
    window2.title('Niveau')
    window2['bg'] = '#cce9ad' 
    window2.resizable(height=False, width=False) #supprime la possibilité de resize

    consigne_choix_niv = Label(window2, text="Choisissez votre niveau !", font=("Verdana", 15, "bold"), fg="black")
    consigne_choix_niv.place(x='370', y='200')
    choix1 = Button(window2, text="Niveau facile",bg='white', fg='black', command=Niveau1)
    choix1.place(x='470', y='250')
    choix2 = Button(window2, text="Niveau intermédiaire",bg='white', fg='black', command=Niveau2)
    choix2.place(x='450', y='280')
    choix3 = Button(window2, text="Niveau impossible",bg='white', fg='black', command=Niveau3)
    choix3.place(x='458', y='310')

#Création de la fênetre 1
window1 = Tk()
window1.geometry('1000x650') #x * y
window1.title('Questionnaire')
window1['bg'] = '#addee9' 
window1.resizable(height=False, width=False) #supprime la possibilité de resize

consigne1 = Label(window1, text="Vous allez voir des photos, et vous devrez répondre !", font=("Verdana", 15, "bold"), fg="black")
consigne1.place(x='200', y='200')
consigne2 = Label(window1, text="VRAI pour les photos que vous pensez réelles")
consigne2.place(x='380', y='250')
consigne3 = Label(window1, text="FAUX pour les photos que vous pensez générées par Intelligence Artificielle")
consigne3.place(x='290', y='280')
start = Label(window1, text="C'est partis ?")
start.place(x='465', y='350')

buttonStart = Button(window1, text="Oui !", bg='white', fg='black', command=Pchoix_du_niv)
buttonStart.place(x='482', y='400')




"""
    buttonV = Button(window1, text="Vrai", bg='white', fg='black')
    buttonV.place(side=LEFT, padx=50)
    buttonF = Button(window1, text="Faux", bg='white', fg='black')
    buttonF.place(side=RIGHT, padx=50)  
"""
#Faire les commandes en fonction des réps

"""
#Variables
score = 0

#Niveau et images
#A_1.jpg -> IA -> False
#R_1.jpg -> Réelles -> True

Niveaux = [[Niv1], [Niv2], [Niv3]]
Niv1 = [(A_1, False),    



 ]
Niv2 = []
Niv3 = []

#Comptage du score

#Choix du niveau
#Radiobutton 
def choix_niv():
niv = input("Choisis ton niveau !")
if niv = m  

#Niveau 1 
if  Niveaux[0] == true & Niv1[i] = true :
    score += 1

print("Score :", score, "/10")


#Niveau 2
if Niveaux[1]

print("Score :", score, "/10")

"""
#Affichage de la fênetre
window1.mainloop()

#Niveau 3

#On a décidé de pas mettre de feedback à chaque réponse au questionnaire (compteur visible) pour éviter un apprentissage et qu'ils soient plus impacté psychologiquement à la fin si il s'est trompé 