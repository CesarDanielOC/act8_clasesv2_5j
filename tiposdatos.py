print("Clases V2 Olave Cruz")
#Zona de Clases
class Datos:
    #El constructor fnc
    def __init__(self,estatura,peso):
        self.estatura= estatura
        self.peso= peso
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, Peso {self.peso} kg")
    def mi_lista(self):
        constructorespythones=["Sam","Pablo","Arturo no"]
        print(constructorespythones)
    
        for cel in constructorespythones:
            print(cel)
#tupleichon
    def mi_tupla(self):
        tupladecarros=("McLaren","Jesko","Porsche")
        print(tupladecarros)

#Seteichon
    def mi_set(self):
        tiposdepollo ={"pollo pollón","pollo pollito","pollo pollero"}
        print(tiposdepollo)

#Diccionariechion



    
    

    

#Creacion de objetos

info= Datos(1.75,64.5)

#Utilizando el objeto
info.mostrar_datos()
print("Lista de constructores pythones Olave Cruz")
info.mi_lista()
print("Lista de carros exóticos")
info.mi_tupla()
print("Lista de tipos de pollos")
info.mi_set()
print("Diccionario")

