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

        elif operation=='tocent':
            t = random.randint(0,2)
            if t==0:
                n = random.randint(0,10)
                return n, 10-n, 10
            elif t==1:
                n = random.randint(0,100)
                return n, 100-n, 100
            elif t==2:
                n = random.randint(0,1000)
                return n, 1000-n, 1000
        
    def printing(self,operation):
        if operation=='sum':
            return str(self.number1) + ' + ' + u"\u25A1"  + ' = '+ str(self.number3)
        elif operation=='rest':
            return str(self.number1) + ' - ' + u"\u25A1"  + ' = '+ str(self.number3)
        elif operation=='mult':
            return str(self.number1) + ' '+u"\u2027"+' ' + u"\u25A1"  + ' = '+ str(self.number3)
        elif operation=='div':
            return str(self.number1) + ' : ' + u"\u25A1"  + ' = '+ str(self.number3)
        elif operation=='tocent':
            if self.number3==10:
                return str(self.number1) + ' |D|'
            elif self.number3==100:
                return str(self.number1) + ' |C|'
            elif self.number3==1000:
                return str(self.number1) + ' |M|'

#operation = ['sum','rest','mult','div']


class Block:

    def __init__(self,number):
        self.block = number
        self.list, self.sol = self.generate(number)

    def generate(self,number):
        if number == 1:
            lista = []
            sol = []
            pos = 'sum'
            for i in range(30):
                o = Operation(pos)
                lista.append(o.printer)
                sol.append(o.number2)
            return lista, sol

        elif number ==2:
            lista = []
            sol = []
            pos = ['sum','rest']
            for i in range(15):
                for e in pos:
                    o = Operation(e)
                    lista.append(o.printer)
                    sol.append(o.number2)
            return lista , sol           

        elif number ==3:
            lista = []
            sol = []
            pos = ['div','sum','rest','mult','sum']
            for i in range(6):
                for e in pos:
                    o = Operation(e)
                    lista.append(o.printer)
                    sol.append(o.number2)
            return lista, sol
        elif number ==4:
            lista = []
            sol = []
            pos = 'tocent'
            for i in range(30):
                o = Operation(pos)
                lista.append(o.printer)
                sol.append(o.number2)
            return lista, sol
                    
            
            
            

class Sheet:
    def __init__(self,idn):
        self.b = [Block(1), Block(2), Block(3),Block(4)]
        self.l = [self.b[i].list for i in range(len(self.b))]
        self.s = [self.b[i].sol for i in range(len(self.b))]
        self.name_q = 'questions_' + str(idn)
        self.name_s = 'solutions_' + str(idn)
        self.printer_questions()
        self.printer_sol()
        
    def printer_questions(self):
        table_0 = pd.DataFrame(np.array(['A','B','C','D','E','F']).reshape(1,6),columns=['A','B','C','D','E','F'],index=np.array(['']))
        table_sol = pd.DataFrame(np.array([ [' '] for i in range(36)]).reshape(6,6).T,columns=['A','B','C','D','E','F'],index=np.array( [' ' for j in range(6) ]))
        l = [pd.DataFrame(np.array(self.l[i]).reshape(6,5).T,columns=['A','B','C','D','E','F'],index=np.arange(1,6)) for i in range(len(self.l))]
        c=[]
        for i in range(len(self.l)):
            c = c + [l[i]] + [table_sol] + [table_0]
        trash = c.pop
        table = pd.concat(c)
        table.to_excel(self.name_q + '.xls')

  
    def printer_sol(self):
        table_0 = pd.DataFrame(np.array(['A','B','C','D','E','F']).reshape(1,6),columns=['A','B','C','D','E','F'],index=np.array(['']))
        table_sol = pd.DataFrame(np.array([ [' '] for i in range(36)]).reshape(6,6).T,columns=['A','B','C','D','E','F'],index=np.array( [' ' for j in range(6) ]))
        l = [pd.DataFrame(np.array(self.l[i]).reshape(6,5).T,columns=['A','B','C','D','E','F'],index=np.arange(1,6)) for i in range(len(self.l))]
        s = [pd.DataFrame( np.concatenate([np.array(self.s[i]).reshape(6,5).T, np.array([['   ' for j in range(6)]])] ) ,columns=['A','B','C','D','E','F'],index=np.array( [' ' for k in range(6) ])) for i in range(len(self.s))]
        c = []
        for i in range(len(self.l)):
            c = c + [l[i]] + [s[i]] + [table_0]
        trash = c.pop
        table = pd.concat(c)
        table.to_excel(self.name_s + '.xls')



for i in range(20):
    Sheet(i)

    
    


##for i in range(1):
##    sheet(i)



##b = Block(1)
##l1 = b.list
##b = Block(2)
##l2 = b.list
##b = Block(3)
##l3 = b.list
##
##
##writer = pd.ExcelWriter('block.xls')
##
##
##table_0.to_excel(writer,sheet_name='sheet0')
##
##table_1 = pd.DataFrame(np.array(l1).reshape(6,5).T,columns=['A','B','C','D','E','F'],index=np.arange(1,6))
##table_1.to_excel(writer,sheet_name='sheet1')
##
##table_2 = pd.DataFrame(np.array(l2).reshape(6,5).T,columns=['A','B','C','D','E','F'],index=np.arange(1,6))
##table_2.to_excel(writer,sheet_name='sheet2')
##
##table_3 = pd.DataFrame(np.array(l3).reshape(6,5).T,columns=['A','B','C','D','E','F'],index=np.arange(1,6))
##table_3.to_excel(writer,sheet_name='sheet3')
##writer.save()
##
##
##table_sol = pd.DataFrame(np.array([ [' '] for i in range(36)]).reshape(6,6).T,columns=['A','B','C','D','E','F'],index=np.array( [' ' for i in range(6) ]))
##
##pd.concat([table_1,table_sol,table_0,table_2,table_sol,table_0,table_3,table_sol]).to_excel('hola.xls')



##        table_1 = pd.DataFrame(np.array(self.b1.list).reshape(6,5).T,columns=['A','B','C','D','E','F'],index=np.arange(1,6))
##        table_2 = pd.DataFrame(np.array(self.b2.list).reshape(6,5).T,columns=['A','B','C','D','E','F'],index=np.arange(1,6))
##        table_3 = pd.DataFrame(np.array(self.b3.list).reshape(6,5).T,columns=['A','B','C','D','E','F'],index=np.arange(1,6))
##        table_4 = pd.DataFrame(np.array(self.b4.list).reshape(6,5).T,columns=['A','B','C','D','E','F'],index=np.arange(1,6))
##        table_sol = pd.DataFrame(np.array([ [' '] for i in range(36)]).reshape(6,6).T,columns=['A','B','C','D','E','F'],index=np.array( [' ' for i in range(6) ]))
##        pd.concat([table_1,table_sol,table_0,table_2,table_sol,table_0,table_3,table_sol,table_0,table_4,table_sol]).to_excel('hola.xls')
##  
