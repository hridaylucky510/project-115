import os 
import shutil

source = "main.txt"
dest = "text.txt"
os.rename(source, dest)
print("successfully moved the source to the destination")