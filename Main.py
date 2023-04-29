import subprocess
import time
import emoji

try:
    import tkinter
    print("Tkinter Module is already downloaded")
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    print("Tkinter module is not installed. Installing now...")
    subprocess.check_call(["python", "-m", "pip", "install", "tk"])
    time.sleep(2)




mainframe = Tk()
def firstWindow():
    first = Toplevel() 
    first.title("Asking For Gussa Ho Ki Nahi")
    Label(first, text="Aabhi Tak Gussa Ho Kya ?", font=('Arial', 15), ).pack()
    
    first.geometry("600x200")
    
def MainFraming():
    mainframe.title("Dear, BestFriend")
    # emo = emoji.emojize("zipper-mouth_face:")
    content = Label(mainframe, text=f"Kya Aap Aage Badhna Chahenge?", font=('Arial', 15), pady=20).pack()

    yesbtn = Button(mainframe, text="Yes",  font=('Arial', 15), padx=56, borderwidth=3, command=yes).pack()
    nobtn = Button(mainframe, text="No",  font=('Arial', 15),padx=62, borderwidth=3, command=no).pack()
    
    # firstWindow()
    mainframe.geometry("600x200")
    mainframe.mainloop()
    

def yes():
    firstWindow()
    
        
def no():
    response = messagebox.askyesno("Hayyy Hayyy", "Aap Kal Milna Merko, Niche. At Sharp 11:05.")
    if response == 1:
        # Emoji        
        pass
    else:
        no()
MainFraming()
