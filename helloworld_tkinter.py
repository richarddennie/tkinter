#Python program to print hello world using tkinter module
#tkinter module is nothing but a inbuilt module that is used to create GUI(Graphical User Interface) applications
#GUI is nothing but the interface that initiates the conversation between the user and computers with widgets such as buttons, icons, windows, etc...

#Okay, Let's import the module
# * this symbol means that we are importing every function from the tkinter module
from tkinter import *
import tkinter 
#now we have succesfully imported the modules into the system

#we now have to initalize the widgets
#display window
window=tkinter.Tk()

#Now, a inbuilt function Label is used to initalize the widget and designing its characterstics
#let the widget be named as words

words=Label(window,text="Hello World!")

#the word widget is now created, we now have place the widget in our display window 
#pack function is used for this purpose

words.pack()

#mainloop function, loops the program forever, untill the exit button is clicked
window.mainloop()


#THANKYOU
