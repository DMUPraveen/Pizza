from Samith import file_handling
from viranga import score
import os


class ChooseBestPizza():
    def __init__(self):
        self.usedPizzas = set()
    def scoring_system(self,all_ingredients:set,ingredients_of_team:set,pizza_dict:{},PizzaToppings):
        pizza_scores={}
        needed_ingredients=set(all_ingredients.difference(ingredients_of_team))
        for ingredient in needed_ingredients:
            for id in pizza_dict[ingredient]:
                if(id not in self.usedPizzas):
                    if(id not in pizza_scores):
                        pizza_scores[id] =0
                    else:
                        pizza_scores[id] +=1
        try :                
            return max(pizza_scores,key=pizza_scores.get)
        except:
            return min(PizzaToppings,key = lambda x:len(PizzaToppings[x]))
            
    def usePizza(self,PizzaId,PizzaToppings):
        self.usedPizzas.add(PizzaId)
        del(PizzaToppings[PizzaId])
        #self.PizzaToppingList.remove()


class Pizza_Key_Maker:
    def __init__(self):
        self.dictionary = {}
        self.allIngrediants =set()
        self.PizzaToppings = {}
        self.PizzaToppingList = []

    def add_pizza(self,id,line):
        ingrediants = line[1:]
        self.PizzaToppings[id] = set()
        for ingrediant in ingrediants:
            self.allIngrediants.add(ingrediant)
            self.PizzaToppings[id].add(ingrediant)
            if(ingrediant in self.dictionary):
                self.dictionary[ingrediant].append(id)
            else:
                self.dictionary[ingrediant] = [id]

    def createSortedList(self):
        self.PizzaToppingList = [(key,self.PizzaToppings[key]) for key in self.PizzaToppings]
        self.PizzaToppingList = sorted(self.PizzaToppingList,key = lambda x: len(x[1]) )           
class DeliverSystem:
    def __init__(self,twoSize,threeSize,fourSize):
        self.Stack = [] # [set()->Ingrediants , []->PizzaIds]
        self.max_Sizes = [0,0,twoSize,threeSize,fourSize]
        self.current_Delviery = []
        self.current_Delivery_team_type = -1
        self.Sizes = [0,0,0,0,0]

    def push_delivery(self,team_type):
        if(self.current_Delivery_team_type != -1):
            if(len(self.current_Delviery[1]) != self.current_Delivery_team_type):
                raise Exception("Previous Team unfilled")
        if not(team_type ==2 or team_type == 3 or team_type ==4):
            raise Exception("Unknown Team")
        
        self.current_Delviery = []
        self.current_Delivery_team_type = team_type
        if(self.Sizes[team_type] > self.max_Sizes[team_type]):
            raise Exception(f"team_type {team_type} overflow")
        self.Stack.append([set(),[]])
        self.current_Delviery = self.Stack[-1]
        

    def add_Pizza_to_delivery(self,PizzaId,toppingSet):
        if(len(self.current_Delviery[1]) >= self.current_Delivery_team_type):
            raise Exception("Team overflow")
        self.current_Delviery[0] = set.union(self.current_Delviery[0],toppingSet)
        self.current_Delviery[1].append(PizzaId)
   

    def createSolution(self,filePath):
        with open(filePath,"w+") as f:
            f.write(f"{len(self.Stack)}\n")
            for delivery in self.Stack:
                ids = " ".join([str(i) for i in delivery[1]])
                team_type = len(delivery[1])
                f.write(f"{team_type} {ids}\n")
                

    
def main(File_name):
    os.chdir("C:\\Users\\USER\\Desktop\\Competition\\HashCode\\Pizza\\Src")
    _,teams_2,teams_3,teams_4,list_of_pizzas = file_handling(File_name)
    PizzaData = Pizza_Key_Maker()
    for id,line in enumerate(list_of_pizzas):
        PizzaData.add_pizza(id,line)

    deliveries = DeliverSystem(teams_2,teams_3,teams_4)
    chooser = ChooseBestPizza()
    MiddleBreak = False
    Pizzaid = -1
    for team_type in range(4,1,-1):

        for _ in range(deliveries.max_Sizes[team_type]):
            deliveries.push_delivery(team_type)
            for _ in range(team_type):
                if(len(PizzaData.PizzaToppings) == 0):
                    MiddleBreak = True
                    break
                '''
                Pizzaid = chooser.scoring_system(
                    PizzaData.allIngrediants,
                    deliveries.current_Delviery[0],
                    PizzaData.dictionary,
                    PizzaData.PizzaToppings
                    )
                '''
                #Pizzaid = max(PizzaData.PizzaToppings,key = lambda x:len(PizzaData.PizzaToppings[x]))
                Pizzaid +=1
                deliveries.add_Pizza_to_delivery(Pizzaid,PizzaData.PizzaToppings[Pizzaid])
                chooser.usePizza(Pizzaid,PizzaData.PizzaToppings)
            if(MiddleBreak):
                break    
    
        if(MiddleBreak):
            break
    
    if(MiddleBreak):
        deliveries.Stack.pop(-1)
    deliveries.createSolution(f"..\\Output\\{File_name}")
    return score(f"..\\Output\\{File_name}",f"..\\Input\\{File_name}")



if __name__ == "__main__":
    print(main("b_little_bit_of_everything.in"))




        
