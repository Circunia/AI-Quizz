from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

#Start python in terminal : % ./python.exe
#Commandes : bg -> background ; fg -> foreground
#Voir quand finis avec CustomTkinter pour voir si c'est beaux

def resize_img(image):
    l = 500
    h = 500
    image = image.resize((l, h))
    return image

#Création de la fenêtre 6
def Affichage_Score(window):
    window.destroy()
    window6 = Tk()
    window6.geometry('1000x650') #x * y
    window6.title('Score')
    window6['bg'] = '#ffc765' 
    window6.resizable(height=False, width=False) #supprime la possibilité de resize

    #Affichage bouton
    #quizStart = Button(window6, text="Quiz", font=("Verdana", 12, "bold"), command=Quiz())
    #quizStart.place(x='480', y='400')

    #Affichage du score
    text_score1 = Label(window6, text=("Votre score est de : " + str(score) + " sur 8 !"), font=("Verdana", 20, "bold"))
    text_score1.place(x='280', y='270')
    if score > 5:
        text_scoreB = Label(window6, text="Bravo, vous êtes un.e expert.e !", font=("Verdana", 20, "bold")) #Bon
        text_scoreB.place(x='250', y='320')
    else:
        text_scoreM = Label(window6, text="Attention, ne vous faites pas avoir la prochaine fois !", font=("Verdana", 20, "bold")) #Mauvais
        text_scoreM.place(x='110', y='320')


def Affichage_Image(tableau,i, window): #index = i
    tableau[i][0] = resize_img(tableau[i][0])
    tableau[i][0] = ImageTk.PhotoImage(tableau[i][0])
    label_img.config(image=tableau[i][0])
    label_img.image = tableau[i][0]
    if i >= len(tableau)-1:
        Affichage_Score(window)

def Rep_Vrai(tableau, window):
    global score, i
    if tableau[i][1] == True:
        score = score + 1
    i = i + 1
    Affichage_Image(tableau, i, window)
    

def Rep_Fausse(tableau, window):
    global score, i
    if i == 0 :
        score = score + 1
    else :
        if tableau[i][1] == False:
            score = score + 1
    i = i + 1
    Affichage_Image(tableau, i, window)

"""
#IMPORTANT
    img1 = resize_img(img1)
    img1 = ImageTk.PhotoImage(img1)
    lab1 = Label(window3, image=img1)
    lab1.image = img1
    lab1.place(x='250', y='10') 
#IMPORTANT

    for i in len(Tab_PNiv1):
        Tab_PNiv1[i][0] = resize_img((Tab_PNiv1[i][0]))
        Tab_PNiv1[i][0] = ImageTk.PhotoImage(Tab_PNiv1[i][0])

        Tab_LabPNiv1[i] = Label(window3, image=Tab_PNiv1[i][0])
        Tab_LabPNiv1[i].image = Tab_PNiv1[i][0]
        #print(Tab_PNiv1)
"""

"""
#Création de la fênetre 7
#Pas fait
    global window3
    window3.destroy() 
    window4.destroy() 
    window5.destroy() 
    window6 = Tk()
    window6.geometry('1000x650') #x * y
    window6.title('Score')
    window6['bg'] = '#ffc765' 
    window6.resizable(height=False, width=False) #supprime la possibilité de resize
"""

#Création de la fênetre 3
def Niveau1():
    global window3, i, label_img, img1
    window2.destroy() #ferme la fenêtre 2
    window3 = Tk()
    window3.geometry('1000x650') #x * y
    window3.title('Niveau 1')
    window3['bg'] = '#ffc765' 
    window3.resizable(height=False, width=False) #supprime la possibilité de resize

    #Generative AI
    img1 = Image.open("P_Niv1\A_14.png")
    img2 = Image.open("P_Niv1\A_15.png")
    img3 = Image.open("P_Niv1\A_22.png")
    img4 = Image.open("P_Niv1\A_6.png")
    img5 = Image.open("P_Niv1\A_27.png")

    #Real
    img6 = Image.open("P_Niv1\R_6.png")
    img7 = Image.open("P_Niv1\R_16.png")
    img8 = Image.open("P_Niv1\R_7.png")
    img9 = Image.open("P_Niv1\R_14.png")
    img10 = Image.open("P_Niv1\R_18.png")

    #Affichage de la première image du niveau
    Tab_PNiv1 = [[img2,False], [img3,False], [img4,False], [img5,False], [img6,True], [img7,True], [img8,True], [img9,True], [img10,True]]
    random.shuffle(Tab_PNiv1)
    img1 = resize_img(img1)
    img1 = ImageTk.PhotoImage(img1)
    label_img = Label(window3, image=img1)
    label_img.place(x='250', y='10')

    #Affichage des boutons
    buttonV = Button(window3, text="Vrai", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Vrai(Tab_PNiv1, window3))
    buttonV.place(x='350', y='550')
    buttonV.config(width=5, height=2)
    buttonF = Button(window3, text="Faux", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Fausse(Tab_PNiv1, window3))
    buttonF.place(x='550', y='550')  
    buttonF.config(width=5, height=2)

#Création de la fênetre 4
def Niveau2():
    global window4, i, label_img, img1
    window2.destroy() #ferme la fenêtre 2
    window4 = Tk()
    window4.geometry('1000x650') #x * y
    window4.title('Niveau 2')
    window4['bg'] = '#ffc765' 
    window4.resizable(height=False, width=False) #supprime la possibilité de resize

    #Generative IA
    img1 = Image.open("P_Niv2\A_4.png")
    img2 = Image.open("P_Niv2\A_5.png")
    img3 = Image.open("P_Niv2\A_17.png")
    img4 = Image.open("P_Niv2\A_19.png")
    img5 = Image.open("P_Niv2\A_26.png")

    #Real
    img6 = Image.open("P_Niv2\R_1.png")
    img7 = Image.open("P_Niv2\R_17.png")
    img8 = Image.open("P_Niv2\R_8.png")
    img9 = Image.open("P_Niv2\R_11.png")
    img10 = Image.open("P_Niv2\R_13.png")

    #Affichage de la première image du niveau
    Tab_PNiv2 = [[img2,False], [img3,False], [img4,False], [img5,False], [img6,True], [img7,True], [img8,True], [img9,True], [img10,True]]
    random.shuffle(Tab_PNiv2)
    img1 = resize_img(img1)
    img1 = ImageTk.PhotoImage(img1)
    label_img = Label(window4, image=img1)
    label_img.place(x='250', y='10')

    #Affichage des boutons
    buttonV = Button(window4, text="Vrai", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Vrai(Tab_PNiv2, window4))
    buttonV.place(x='350', y='550')
    buttonV.config(width=5, height=2)
    buttonF = Button(window4, text="Faux", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Fausse(Tab_PNiv2, window4))
    buttonF.place(x='550', y='550')  
    buttonF.config(width=5, height=2)

#Création de la fênetre 5
def Niveau3():
    global window5, i, label_img, img1
    window2.destroy() #ferme la fenêtre 2
    window5 = Tk()
    window5.geometry('1000x650') #x * y
    window5.title('Niveau 3')
    window5['bg'] = '#ffc765' 
    window5.resizable(height=False, width=False) #supprime la possibilité de resize

    #Generative IA
    img1 = Image.open("P_Niv3\A_1.png")
    img2 = Image.open("P_Niv3\A_2.png")
    img3 = Image.open("P_Niv3\A_7.png")
    img4 = Image.open("P_Niv3\A_10.png")
    img5 = Image.open("P_Niv3\A_11.png")

    #Real
    img6 = Image.open("P_Niv3\R_3.png")
    img7 = Image.open("P_Niv3\R_4.png")
    img8 = Image.open("P_Niv3\R_9.png")
    img9 = Image.open("P_Niv3\R_10.png")
    img10 = Image.open("P_Niv3\R_12.png")

    #Affichage de la première image du niveau
    Tab_PNiv3 = [[img2,False], [img3,False], [img4,False], [img5,False], [img6,True], [img7,True], [img8,True], [img9,True], [img10,True]]
    random.shuffle(Tab_PNiv3)
    img1 = resize_img(img1)
    img1 = ImageTk.PhotoImage(img1)
    label_img = Label(window5, image=img1)
    label_img.place(x='250', y='10')

    #Affichage des boutons
    buttonV = Button(window5, text="Vrai", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Vrai(Tab_PNiv3, window5))
    buttonV.place(x='350', y='550')
    buttonV.config(width=5, height=2)
    buttonF = Button(window5, text="Faux", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Fausse(Tab_PNiv3, window5))
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

score = 0
i = 0 #index

consigne1 = Label(window1, text="Vous allez voir des photos, et vous devrez répondre !", font=("Verdana", 15, "bold"), fg="black")
consigne1.place(x='200', y='200')
consigne2 = Label(window1, text="VRAI pour les photos que vous pensez réelles")
consigne2.place(x='380', y='250')
consigne3 = Label(window1, text="FAUX pour les photos que vous pensez générées par Intelligence Artificielle")
consigne3.place(x='290', y='280')
start = Label(window1, text="C'est parti  ?")
start.place(x='465', y='350')

buttonStart = Button(window1, text="Oui !", bg='white', fg='black', command=Pchoix_du_niv)
buttonStart.place(x='482', y='400')

#Affichage de la fênetre
window1.mainloop()

#Niveau 3

#On a décidé de pas mettre de feedback à chaque réponse au questionnaire (compteur visible) pour éviter un apprentissage et qu'ils soient plus impacté psychologiquement à la fin si il s'est trompé 
