import os

def read_file(path):
    with open(path, "rb") as file:
        return file.read()

def getfolders(folder):
    files = []
    folders = []
    for file in os.listdir(folder):
        currentpath = f"{folder}\\{file}"

        if os.path.isdir(currentpath):
            folders.append(currentpath)
            fol, fil = getfolders(currentpath)
            folders.extend(fol)
            files.extend(fil)

        else:
            files.append(currentpath)

    return folders, files
