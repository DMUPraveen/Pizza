from Samith import file_handling


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
        self.two_stack = [] #contains a pair (set(ingrediants),pizza ids)
        self.three_stack = []
        self.four_stack = []
        self.two_max_size = twoSize
        self.three_max_size = threeSize
        self.four_max_size = fourSize
        self.current_Delviery = None
        self.current_Delivery_team_type = -1

    def push_delivery(self,team_type):
        if(team_type == 2):
            self.two_stack.append([set(),[]])
            self.current_Delviery = self.two_stack[-1]
            if(len(self.two_stack) > self.two_max_size):
                Exception("two stack overflow")
        elif(team_type == 3):
            self.three_stack.append([set(),[]])
            self.current_Delviery = self.three_stack[-1]
            if(len(self.three_stack) > self.three_max_size):
                Exception("two stack overflow")
        elif(team_type == 4):
            self.four_stack.append([set(),[]])
            self.current_Delviery = self.four_stack[-1]
            if(len(self.four_stack) > self.four_max_size):
                Exception("four stack overflow")
        else:
            Exception("Unknown Team")
        


    def add_Pizza_to_delivery(self,PizzaId,toppingSet):
        if(len(self.current_Delviery[1]) > self.current_Delivery_team_type):
            return False
        self.current_Delviery[0] = set.union(self.current_Delviery[0],toppingSet)
        self.current_Delviery[1].append(PizzaId)
        return True

    


no_pizzas,teams_2,teams_3,teams_4,list_of_pizzas = file_handling()
PizzaData = Pizza_Key_Maker()
for id,line in enumerate(list_of_pizzas):
    PizzaData.add_pizza(id,line)

deliveries = DeliverSystem(teams_2,teams_3,teams_4)









        
