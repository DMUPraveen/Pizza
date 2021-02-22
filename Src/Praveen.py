class Pizza_Key_Maker:
    def __init__(self):
        self.dictionary = {}

    def add_pizza(self,id,line):
        ingrediants = line.split(" ")[1:]
        for ingrediant in ingrediants:
            if(ingrediant in self.dictionary):
                self.dictionary[ingrediant].append(id)
            else:
                self.dictionary[ingrediant] = [id]
                
class Deliveries:
    def __init__(self,two,three,four):
        self.two_deliveries = []
        self.three_deliveris =[]
        self.four_deliveries = []
    

    def deliver(self):
    


        
