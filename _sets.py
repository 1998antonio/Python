

### Sets ###

#Definicion

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set ={"Marco", "Sandoval", 26}
print(type(my_other_set))

print (len(my_other_set))

#Insercion

my_other_set.add("MarcoDev")
print(my_other_set) #Un set no es una estructura ordenada
my_other_set.add("MarcoDev") #Un ser no admite repetidos
print(my_other_set)    

#Busqueda

print("Marco" in my_other_set)
print("Marcou" in my_other_set)

#Eliminacion

my_other_set.remove("Sandoval")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set

#Tranformacion

my_set = {"Marco", "Sandoval", 26}
my_list = list(my_set)
print(my_list)
print(my_list[0])
my_other_set = {"kotlin", "Swift", "Python"}

#Otras Operaciones 

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))
