import subprocess

try:
    import tkinter
    print("Tkinter Module is already downloaded")
except ImportError:
    print("Tkinter module is not installed. Installing now...")
    subprocess.check_call(["python", "-m", "pip", "install", "tk"])
