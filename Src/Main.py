from Praveen import main
import os

os.chdir("C:\\Users\\USER\\Desktop\\Competition\\HashCode\\Pizza\\Src")
fileNames = os.listdir("..\\Input")
print(fileNames)

score = 0
for fileName in fileNames:
    print(fileName)
    if(fileName[0] == "c"):
        continue
    score += main(fileName)
    print(score)
print(score)

