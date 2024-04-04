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
def Affichage_Score(score):
    window3.destroy() 
    window4.destroy() 
    window5.destroy() 
    window6 = Tk()
    window6.geometry('1000x650') #x * y
    window6.title('Score')
    window6['bg'] = '#ffc765' 
    window6.resizable(height=False, width=False) #supprime la possibilité de resize

    #Affichage du score
    text_score1 = Label(window6, text=("Votre score est de :", score, " sur 10 !"))
    text_score1.place(x='300', y='400')
    if score > 5:
        text_scoreB = Label(window6, text="Bravo, vous êtes un.e expert.e !") #Bon
        text_scoreB.place(x='300', y='400')
    else:
        text_scoreM = Label(window6, text="Attention, ne vous faites pas avoir la prochaine fois") #Mauvais
        text_scoreM.place(x='300', y='400')

def Affichage_Image(tableau,i): #index = i
    tableau[i][0] = resize_img(tableau[i][0])
    tableau[i][0] = ImageTk.PhotoImage(tableau[i][0])
    label_img.config(image=tableau[i][0])
    label_img.image = tableau[i][0]

def Rep_Vrai(tableau):
    global score, i
    if tableau[i][1] == True:
        score = score + 1
    i = i + 1
    Affichage_Image(tableau, i)

def Rep_Fausse(tableau):
    global score, i
    if tableau[i][1] == False:
        score = score + 1
    i = i + 1
    Affichage_Image(tableau, i)



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
    global window3, i, label_img
    i = 0 #index
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
    img5 = Image.open("P_Niv1\A_3.png")

    #Real
    img6 = Image.open("P_Niv1\R_6.png")
    img7 = Image.open("P_Niv1\R_10.png")
    img8 = Image.open("P_Niv1\R_11.png")
    img9 = Image.open("P_Niv1\R_12.png")
    img10 = Image.open("P_Niv1\R_13.png")

    Tab_PNiv1 = [[img1,False], [img2,False], [img3,False], [img4,False], [img5,False], [img6,True], [img7,True], [img8,True], [img9,True], [img10,True]]
    label_img = Label(window3)
    label_img.place(x='250', y='10')

    #Affichage de la première image ???????????????????????? et destruction
    img1 = resize_img(img1)
    img1 = ImageTk.PhotoImage(img1)
    lab1 = Label(window3, image=img1)
    lab1.image = img1
    lab1.place(x='250', y='10') 

    #Affichage des boutons
    buttonV = Button(window3, text="Vrai", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Vrai(Tab_PNiv1))
    buttonV.place(x='350', y='550')
    buttonV.config(width=5, height=2)
    buttonF = Button(window3, text="Faux", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Fausse(Tab_PNiv1))
    buttonF.place(x='550', y='550')  
    buttonF.config(width=5, height=2)
    
    #if i == len(Tab_PNiv1):
    #Affichage_Score(score)

#Création de la fênetre 4
def Niveau2():
    global window4
    window2.destroy() #ferme la fenêtre 2
    window4 = Tk()
    window4.geometry('1000x650') #x * y
    window4.title('Niveau 2')
    window4['bg'] = '#ffc765' 
    window4.resizable(height=False, width=False) #supprime la possibilité de resize

    #Generative IA
    img1 = Image.open("P_Niv1\A_4.png")
    img2 = Image.open("P_Niv1\A_5.png")
    img3 = Image.open("P_Niv1\A_17.png")
    img4 = Image.open("P_Niv1\A_19.png")
    img5 = Image.open("P_Niv1\A_26.png")

    #Real
    img6 = Image.open("P_Niv1\R_1.png")
    img7 = Image.open("P_Niv1\R_6.png")
    img8 = Image.open("P_Niv1\R_8.png")
    img9 = Image.open("P_Niv1\R_11.png")
    img10 = Image.open("P_Niv1\R_13.png")

    Tab_PNiv2 = [[img1,False], [img2,False], [img3,False], [img4,False], [img5,False], [img6,True], [img7,True], [img8,True], [img9,True], [img10,True]]
    label_img = Label(window4)
    label_img.place(x='250', y='10')

    buttonV = Button(window4, text="Vrai", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Vrai(Tab_PNiv2))
    buttonV.place(x='350', y='550')
    buttonV.config(width=5, height=2)
    buttonF = Button(window4, text="Faux", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Fausse(Tab_PNiv2))
    buttonF.place(x='550', y='550')  
    buttonF.config(width=5, height=2)

#Création de la fênetre 5
def Niveau3():
    global window5
    window2.destroy() #ferme la fenêtre 2
    window5 = Tk()
    window5.geometry('1000x650') #x * y
    window5.title('Niveau 3')
    window5['bg'] = '#ffc765' 
    window5.resizable(height=False, width=False) #supprime la possibilité de resize

    #Generative IA
    img1 = Image.open("P_Niv1\A_1.png")
    img2 = Image.open("P_Niv1\A_2.png")
    img3 = Image.open("P_Niv1\A_7.png")
    img4 = Image.open("P_Niv1\A_10.png")
    img5 = Image.open("P_Niv1\A_11.png")

    #Real
    img6 = Image.open("P_Niv1\R_3.png")
    img7 = Image.open("P_Niv1\R_4.png")
    img8 = Image.open("P_Niv1\R_9.png")
    img9 = Image.open("P_Niv1\R_10.png")
    img10 = Image.open("P_Niv1\R_12.png")

    Tab_PNiv3 = [[img1,False], [img2,False], [img3,False], [img4,False], [img5,False], [img6,True], [img7,True], [img8,True], [img9,True], [img10,True]]
    label_img = Label(window5)
    label_img.place(x='250', y='10')

    buttonV = Button(window5, text="Vrai", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Vrai(Tab_PNiv3))
    buttonV.place(x='350', y='550')
    buttonV.config(width=5, height=2)
    buttonF = Button(window5, text="Faux", bg='white', fg='black', font=("Verdana", 15, "bold"), command=lambda: Rep_Fausse(Tab_PNiv3))
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


#Affichage de la fênetre
window1.mainloop()

#Niveau 3

#On a décidé de pas mettre de feedback à chaque réponse au questionnaire (compteur visible) pour éviter un apprentissage et qu'ils soient plus impacté psychologiquement à la fin si il s'est trompé 
