#variables

my_string_variable = "My string variable"
#print(my_string_variable)

my_int_variable = 5
#print(my_int_variable)
#print(type(my_int_variable))

my_float_variable = 1.8
#print(my_float_variable)
#print(type(my_float_variable))

my_int_to_str_variable = str(my_int_variable)
#print(my_int_to_str_variable)
#print(type(my_int_to_str_variable))

my_bool_variable = True
#print(my_bool_variable)
#print(type(my_bool_variable))

#concatenacion de variables en un print
print(my_string_variable,my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:" , my_bool_variable)

#Algunas funciones del sistema
#len obtiene el largo de la cadena
print(len(my_string_variable))

#Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age ="lari", "cañonga", "MoureDev", 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)
      
      
# inputs
name = input('¿Cual es tu nombre? ')
age = input('¿Cual es tu edad? ')
print(name)
print(age)
print(type(name))
print(type(age))


#Cambiar su tipo
name= 35
age= "brais"
print(name)
print(age)
print(type(name))
print(type(age))

#Forzamos el tipo 
address: int = 1
#address = input('¿Cual es tu direccion? ')
#address = True
#address = 5
#address = 1.2
print(type(address))
