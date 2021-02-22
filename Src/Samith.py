def file_handling(file_name:str):
    #"../Input/b_little_bit_of_everything.in"
    with open("../Input/"+file_name) as f:
        list_of_pizzas=[]
        for line in f:
            line=line[:-1]
            list_of_pizzas.append([])
            for word in line.split(" "):
                list_of_pizzas[-1].append(word)
            #list_of_pizzas[-1].
   # first_line=list_of_pizzas.pop(0)
    no_pizzas,teams_2,teams_3,teams_4=list_of_pizzas.pop(0)
    no_pizzas=int(no_pizzas)
    teams_2=int(teams_2)
    teams_3=int(teams_3)
    teams_4=int(teams_4)
    print(list_of_pizzas)
    #print("hi")
    return no_pizzas,teams_2,teams_3,teams_4,list_of_pizzas


def scoring_system(pizza_list:list,all_ingredients:set,ingredients_of_team:set,pizza_dict:{}):
    pizza_scores={}
    needed_ingredients=set(all_ingredients.difference(ingredients_of_team))
    for ID in pizza_list:
        pizza_scores[ID]=len(needed_ingredients.intersection(pizza_dict[ID]))
    
    return pizza_scores
#print(file_handling("b_little_bit_of_everything.in"))

class ChooseBestPizza():
    def __init__(self):
        self.usedPizzas = set()
    
    def scoring_system(self,pizza_set:set,all_ingredients:set,ingredients_of_team:set,pizza_dict:{}):
        pizza_scores={}
        needed_ingredients=set(all_ingredients.difference(ingredients_of_team))
        for ingredient in needed_ingredients:
            for id in pizza_dict[ingredient]:
                if(id not in self.usedPizzas):
                    pizza_scores[id] += 1

                
        return max(pizza_scores,key=pizza_scores.get)
    

    def usePizza(self,PizzaId):
        self.usedPizzas.add(PizzaId)
#print(scoring_system([],set(),set(),{}))
