import subprocess
from tkinter import *
from tkinter.ttk import *
import time
root = Tk(className=" Tessy Automation by KPujari")
root.geometry("500x300")

# Create menubar by setting the color 
menubar = Menu(root, background='#F0F8FF', fg='white') 

# Declare file and edit for showing in menubar 
file = Menu(menubar, tearoff=False, background='#E0EEEE') 
edit = Menu(menubar, tearoff=False, background='#E0EEEE') 

# Add commands in in file menu 
file.add_command(label="New") 
file.add_command(label="Exit", command=root.quit) 

w = Label(root,text="Click to Run Regresstion Test ",width= 28)
w.pack()

progress = Progressbar(root, orient = HORIZONTAL, 
			length = 190,  mode = 'determinate') 

def Test_Hal_Layer():
    progress['value'] = 20
    root.update_idletasks() 
    progress['value'] = 40
    root.update_idletasks() 
    subprocess.run([r"C:\Arbeit\CI_CD\HAL_Config.bat"])
    progress['value'] = 60
    root.update_idletasks() 
    progress['value'] = 80
    root.update_idletasks()

    progress['value'] = 100
    root.update_idletasks() 
progress.pack(pady = 10) 

def Test_SDP_Layer():
    progress['value'] = 20
    root.update_idletasks() 
    progress['value'] = 40
    root.update_idletasks() 
    subprocess.run([r"C:\Arbeit\CI_CD\SDP_Config.bat"])
    progress['value'] = 60
    root.update_idletasks() 
    progress['value'] = 80
    root.update_idletasks() 
    progress['value'] = 100
    root.update_idletasks() 
progress.pack(pady = 10) 

def Test_DRV_Layer():
    progress['value'] = 20
    root.update_idletasks() 
    progress['value'] = 40
    root.update_idletasks() 
    subprocess.run([r"C:\Arbeit\CI_CD\DRV_Config.bat"])
    progress['value'] = 60
    root.update_idletasks() 
    progress['value'] = 80
    root.update_idletasks() 
    progress['value'] = 100
    root.update_idletasks()   
progress.pack(pady = 10) 

# Add commands in edit menu 
edit.add_command(label="Cut") 
edit.add_command(label="Copy") 
edit.add_command(label="Paste") 
  
# Display the file and edit declared in previous step 
menubar.add_cascade(label="File", menu=file) 
menubar.add_cascade(label="Edit", menu=edit) 

button1 = Button(root, text=" SDP Layer Regression Test",width=30,command=Test_SDP_Layer).pack()

button2 = Button(root,text="HAL Layer Regression Test",width=30,command=Test_Hal_Layer).pack()

button3 = Button(root, text=" DRV Layer Regression Test",width=30,command=Test_DRV_Layer).pack()

root.config(menu=menubar)

root.mainloop()
