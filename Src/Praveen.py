from Samith import file_handling,scoring_system
import os


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
        return max([pizza_scores[i] for i in pizza_scores])
    def usePizza(self,PizzaId):
        self.usedPizzas.add(PizzaId)
        




class Pizza_Key_Maker:
    def __init__(self):
        self.dictionary = {}
        self.allIngrediants =set()
        self.PizzaToppings = {}

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
            return False
        self.current_Delviery[0] = set.union(self.current_Delviery[0],toppingSet)
        self.current_Delviery[1].append(PizzaId)
        return True

    def createSolution(self,filePath):
        with open(filePath,"w+") as f:
            f.write(f"{len(self.Stack)}\n")
            for delivery in self.Stack:
                ids = " ".join(delivery[1])
                team_type = len(ids)
                f.write(f"{team_type} {ids}\n")
                

    
def main():
    os.chdir("C:\\Users\\USER\\Desktop\\Competition\\HashCode\\Pizza\\Src")
    no_pizzas,teams_2,teams_3,teams_4,list_of_pizzas = file_handling()
    PizzaData = Pizza_Key_Maker()
    for id,line in enumerate(list_of_pizzas):
        PizzaData.add_pizza(id,line)

    deliveries = DeliverSystem(teams_2,teams_3,teams_4)
    chooser = ChooseBestPizza()
    deliveries.push_delivery(2)
    deliveries.add_Pizza_to_delivery(0,PizzaData.PizzaToppings[0])
    deliveries.add_Pizza_to_delivery(1,PizzaData.PizzaToppings[1])
    deliveries.push_delivery(3)
    deliveries.add_Pizza_to_delivery(2,PizzaData.PizzaToppings[2])
    deliveries.add_Pizza_to_delivery(3,PizzaData.PizzaToppings[3])
    deliveries.add_Pizza_to_delivery(4,PizzaData.PizzaToppings[4])
    deliveries.createSolution("..\\Output\\test.txt")
    






        
