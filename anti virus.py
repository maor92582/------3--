import requests
import os
import json
from tkinter import filedialog
from tkinter import *
import time


import customtkinter
def openfile():
    global filepath
    filepath=filedialog.askdirectory(parent=app, initialdir="/", title='Please select a directory')
    print(filepath)
    app.destroy()
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app=customtkinter.CTk()
button=Button(text="open",command=openfile)
button.pack()
app.mainloop()
os.chdir(filepath)


url = 'https://www.virustotal.com/vtapi/v2/file/scan'
l=os.listdir()
print(l)
def reqest(url,files,params):
    response = requests.post(url, files=files, params=params)
    x=response.json()

    time.sleep(10)
    x=dict(x)
    print(x.get('verbose_msg'))  
    x=x.get('resource')
    url = 'https://www.virustotal.com/vtapi/v2/file/report'

    params = {'apikey': '88d8b29ec58ef67874875290da0393ae1fb1b5d52590baa77ac84bb1f24ab12c', 'resource': x}

    response = requests.get(url, params=params)
    x=response.json()
    x=dict(x)
    print(str(x.get('positives'))+" "+"positives were found")

for name in l:
    os.chdir(filepath)
    print(name)
    params = {'apikey': '88d8b29ec58ef67874875290da0393ae1fb1b5d52590baa77ac84bb1f24ab12c'}
    files = {'file': (name, open(name, 'rb'))}
    reqest(url,files,params)
