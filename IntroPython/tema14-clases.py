class OpeeacionesBasicas:
        #declaracion de propiedades
            num1= 0
            num2 = 0 
            nume = 0

        #Declara el contructor de las clase
            def __init__(self,a,b):
                self.num1= a
                self.num2 = b

        #Declaracion de lo metodos de la clase
            def suma(self):
                self.res =self.num1 + self.num2
                print("La suma es : {}".format(self.res))

def main():
        obj = OpeeacionesBasicas(9,10)
        obj.suma()

if __name__=="__main__":
        main()