
def score(y,z):


    f=open(y, "r").readlines()

    for i in range (0,len(f)):
        f[i]=f[i].rstrip()
        f[i]=f[i].replace(" ",",")
        f[i]=[int(x) for x in f[i].split(",")]
        
    f.remove(f[0])

    # print(f)


    ingredients=open(z,"r").readlines()

    ingredients_list=[]

    for i in range(1,len(ingredients)):
        ingredients_list.append(ingredients[i].strip().replace(" ",","))
   

    ingredients_list_2=[]

    for a in range(0,len(ingredients_list)):
        new_list=[x for x in ingredients_list[a].split(",")]
        ingredients_list_2.append(new_list)

    ingredients_list_3=[]

    for b in range(0,len(ingredients_list_2)):
        for c in range(1,len(ingredients_list_2[b])):
            ingredients_list_3.append(ingredients_list_2[b][c])

    ingredients_list_3=list(dict.fromkeys(ingredients_list_3))

    # print(ingredients_list_2)


    topping_count=[]

    for p in range(0,len(f)):
        topping_num=[]
        for q in range(1,len(f[p])):
            n=f[p][q]

            for k in range(1,len(ingredients_list_2[n])):
                number=ingredients_list_3.index(ingredients_list_2[n][k])
                topping_num.append(number+1)
        topping_num=list(dict.fromkeys(topping_num))
        topping_count.append(len(topping_num)**2)

    return sum(topping_count)


#print(score("Submission.txt","b_little_bit_of_everything.in"))