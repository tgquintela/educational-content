import random as random
import numpy as np
import pandas as pd

class Operation:

    def __init__(self,operation):
        self.operation=operation
        self.number1, self.number2, self.number3 = self.election(operation)
        self.printer = self.printing(operation)

    def election(self,operation):
        if operation=='sum':
            a1 = random.randint(0,90)
            a2 = random.randint(0,90)
            return a1, a2, a1+a2
        
        elif operation=='rest':
            a1 = random.randint(0,10)
            a2 = random.randint(0,10)
            return a1+a2, a1, a2
            
        elif operation=='mult':
            a1 = random.randint(0,10)
            a2 = random.randint(0,10)
            return a1, a2, a1*a2

        elif operation=='div':
            a1 = random.randint(0,10)
            a2 = random.randint(0,10)
            return a1*a2, a1, a2
        
    def printing(self,operation):
        if operation=='sum':
            return '\$' + str(self.number1) 		+ '\qquad + \qquad ' 	+ '\square \qquad'  + 	' = ' + '\qquad' + str(self.number3) + '\$'
        elif operation=='rest':
            return '\$' + str(self.number1) 		+ '\qquad - \qquad ' 	+ '\square \qquad'  + 	' = '+ '\qquad' + str(self.number3) + '\$'
        elif operation=='mult':
            return '\$' + str(self.number1) 		+ '\qquad \cdot \qquad' + '\square \qquad'  + 	' = '+ '\qquad' + str(self.number3) + '\$'
        elif operation=='div':
            return '\$' + str(self.number1) 		+ '\qquad  :\qquad  ' 	+ '\square \qquad'  + 	' = '+ '\qquad' + str(self.number3) + '\$'


#operation = ['sum','rest','mult','div']


class Block:

    def __init__(self,number):
        self.block = number
        self.list = self.generate(number)

    def generate(self,number):
        if number == 1:
            lista = []
            for i in range(30):
                lista.append(Operation('sum').printer)
            return lista

        elif number ==2:
            lista = []
            for i in range(15):
                lista.append(Operation('sum').printer)
                lista.append(Operation('rest').printer)
            return lista            

        elif number ==3:
            lista = []
            for i in range(6):
                lista.append(Operation('div').printer)
                lista.append(Operation('sum').printer)
                lista.append(Operation('rest').printer)
                lista.append(Operation('mult').printer)
                lista.append(Operation('sum').printer)
            return lista            
            

class sheet():
    def __init__(self):
        self.b1 = block(1)
        self.b1 = block(2)
        self.b1 = block(3)
    def printer(self):
        pass
        




b = Block(2)
l = b.list

table_1 = pd.DataFrame(np.array(l).reshape(5,6),columns=['A','B','C','D','E','F'])
table_1
