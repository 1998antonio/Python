

### Functions ###

#Definicion

def my_function(): #Tabulaciones
    print("Esto es una funcion")
    print("UMG")
    
my_function()
my_function()
my_function()

#Funcion con parametros de entrada/argumentos

def sum_two_values(first_value: int, second_value):
    print(first_value," + ",second_value," = ",first_value + second_value)
    
sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

#Funcion con parametros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


my_result = sum_two_values_with_return(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

#Funcion con parametros de entrada/argumentos por clave


def print_name(name, lastname):
    print(f"{name} {lastname}")
    
    
print_name(lastname="Sandoval", name="Marco")

#Funcion con parametros de entrada/argumentos por defecto

def print_name_with_default(name, lastname, alias="coqueto"):
    print(f"{name} {lastname} {alias}")
    
    
print_name_with_default("Marco", "Sandoval")
print_name_with_default("Marco", "Sandoval", "Perez")

#Funcion con parametros de entrada/argumentos arbitrarios

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())
        
    
print_upper_texts("Hola", "Piton", "Dorado")
print_upper_texts("Hola")   
