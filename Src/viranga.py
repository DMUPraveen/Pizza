


ingredients=open("b_little_bit_of_everything.in","r").readlines()

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

n=1

ingredients_num=[]

for k in range(1,len(ingredients_list_2[n])):
    number=ingredients_list_3.index(ingredients_list_2[n][k])
    ingredients_num.append(number)

# print(ingredients_num)
# print(ingredients_list_3)

