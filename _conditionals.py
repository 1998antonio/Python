

### Conditionals ###

#if

my_condition = True

if my_condition: #Es lo mismo que if my_condition == True:
    print("Se ejecuta la condicion del if")
    
my_condition = 5 * 5

if my_condition == 10:
 print("Se ejecuta la condicion del segundo if")
    
    #********************
    #if, else, elif 
    
if my_condition > 10 and my_condition < 30:
        print("Es mayor que 10 y menos que 20")
elif my_condition == 25:
        print("Es igual a 25")
else:
        print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")
print("la ejecucion continua")
        
    #Condicional con inspeccion de valor
    
my_string = ""
my2_string = "Mi cadena de textoooo"

if not my_string:
    print("Mi cadena de texto es vacia")
        
if my2_string == "Mi cadena de textoooo":
    print("Estas cadenas de texto coinciden")