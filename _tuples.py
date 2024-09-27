

### Tuples ###

#Definicion

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Marco", "Sandoval", "Antonio")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

#Acceso a elementos y busqueda 

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[4]) #IndexError
#print(my_tuple[-6]) #IndexError

print(my_tuple.count("Marco"))
print(my_tuple.index("Sandoval"))
print(my_tuple.index("Antonio"))

#my_tuple[1] = 1.80 #Cuando se declara una tupla no se puede modificar

#Concatenacion

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

#Subtuplas

print(my_sum_tuple[3:6])

#Tupla notable con conversion a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "AntonioDev"
my_tuple.insert(1, "Rojo")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#Eliminacion

#del my_tuple[1]
del my_tuple

print(my_tuple)


