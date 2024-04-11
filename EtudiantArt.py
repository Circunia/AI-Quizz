from tkinter import *
from tkinter import ttk

#Création de la fênetre 1
window1 = Tk()
window1.geometry('1000x650') #x * y
window1.title('Etudiant en Art')
window1['bg'] = '#addee9' 
window1.resizable(height=False, width=False) #supprime la possibilité de resize

box1 = Frame(window1)
consigne1 = Label(box1, text="Vous êtes étudiant en art dans une université étrangère", font=("Verdana", 10, "bold"), fg="black")
consigne1.pack(expand=YES)
consigne2 = Label(box1, text="vous n'avez plus beaucoup de temps pour rendre votre projet de fin d'année mais n'avez toujours pas trouvez l'inspiration", font=("Verdana", 10, "bold"), fg="black")
consigne2.pack(expand=YES)
consigne3 = Label(box1, text="aidez vous de tous les outils à votre disposition pour avoir la meilleure note !", font=("Verdana", 10, "bold"), fg="black")
consigne3.pack(expand=YES)
consigne4 = Label(box1, text="Consigne : 通过数字艺术探索现实与幻觉之间的二元性", font=("Verdana", 10, "bold"), fg="black")
consigne4.pack(expand=YES)

box1.place(x='50', y='250')
window1.mainloop()
