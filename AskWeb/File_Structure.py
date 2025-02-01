import os
from pathlib import Path
Project_Name = "AskWeb"

Files = [

    f"{Project_Name}/__init__.py",
    f"{Project_Name}/Stream/__init__.py",
    f"{Project_Name}/Stream/Main.py",  
    f"{Project_Name}/Stream/Fetch_Url.py", 
    f"{Project_Name}/Stream/Get_Data.py", 

    f"{Project_Name}/Models/__init__.py",
    f"{Project_Name}/Models/Result.py",

    f"{Project_Name}/Requirements.txt",
    f"{Project_Name}/Setup.py"


]


for EachFile in Files:
    File = Path(EachFile)
    FileFolder, FileName = os.path.split(File)
    if FileFolder != "":
        os.makedirs(FileFolder, exist_ok=True)

    if (not os.path.exists(File)) or (os.path.getsize(File) == 0):
        with open(File, "w") as f:
            pass
    else:
        print(f"Already Present: {File}")
