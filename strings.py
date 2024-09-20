'''
my_string = "My string"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este en un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

#Formato
# %s para tipo string 
# %d para tipo int
name, lastname, age = "Marco", "Perez", 26
print("Mi nombre es: {} {} y mi edad es {}".format(name, lastname, age))
print(" Mi nombre es %s %s y mi edad es %d" % (name, lastname, age))
print(" Mi nombre es " + name + " " +  lastname + " y mi edad es " + age)
print(f"Mi nombre es {name} {lastname} y mi edad es {age}")
'''

#Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
'''
print(b)
print(e)

#Dividir la cadena

language_slice = language[1:3]
print(language_slice)

language_slice = language[0:5]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

#reversa

reversed_language = language[::-1]
print(reversed_language)
'''
#Funciones del lenguaje con cadenas

print(language.capitalize()) #primera mayusucla
print(language.upper()) #todas mayusuclas
print(language.count()) #cuenta las letras 
print(language.isnumeric()) #
print("1".isnumeric())
print(language.lower()) #todas minusculas
print(language.lower().isupper())
print(language.startswith("Py")) #imprimir si inicia con las letras en parentesis
print("Py" == "py") #Diferentes
