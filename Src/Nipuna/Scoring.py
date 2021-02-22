f=open("submission.txt", "r").readlines()

for i in range (0,len(f)):
    f[i]=f[i].rstrip()
    f[i]=f[i].replace(" ",",")
    f[i]=[int(x) for x in f[i].split(",")]
        
f.remove(f[0])

print(f)



