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
                


        
