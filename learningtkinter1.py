#Import the tkinter module for >= Python 3.3.
#Use capital T for earlier Python versions.
import tkinter
#Create a new window object called window.
window = tkinter.Tk() 

#Add a title to the window
window.title("My First Python Window")

# Set window size
window.geometry ("400x400")

# Set an icon
window.wm_iconbitmap('Fasticon-Cat-Cat-Black.ico')

#draw the window and start the 'app'
window.mainloop()


