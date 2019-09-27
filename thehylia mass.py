import thehylia
#import khinsider as thehylia
import os

def download(things, outdir):
    os.system("cls")
    #basedir = "G:/Users/Jozhus/Desktop/Files/mulp/Animusic/_Games" + "/" + outdir
    basedir = "H:/Dump/Good vibrations" + "/" + outdir
    print("Starting!")
    if not os.path.isdir(basedir):
            os.mkdir(basedir)
    for y, x in enumerate(things):
        outPath = basedir + "/" + x
        if not os.path.isdir(outPath):
            os.mkdir(outPath)
        print("\n" + str(y + 1) + "/" + str(len(things)) + " - " + x)
        thehylia.download(x, path=outPath, verbose=True)
    input("\nDone!")

def search():
    while (True):
        search = thehylia.search(input("Search: "))
        if len(search) > 0:
            for x in search:
                print(x)
            if input("Download? (y,n): ") == "y":
                return search
        else:
            input("Nothing found")
        os.system("cls")

while(True):
    os.system("cls")
    download(search(), input("New Folder: "))
