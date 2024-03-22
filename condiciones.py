# DE LAS ESTRUCTURAS MAS IMPORTANTES EN PYTHON SON LAS CONDICIONALES
# IF
if False:
    print("La condición es verdadera")  

edad = 18
teorico = True

if edad >= 18 and teorico:
    print("Puedes sacar licecnia de conducir")
else:
    print("No puedes sacar licencia de conducir")

# IF-ELIF-ELSE

nota = 98   

if nota >= 70 and nota <= 100:
    print("Aprobado")
elif nota >= 60 and nota < 70:    
    print("A recuperatorio")
elif nota >= 0 and nota < 60:
    print("Desaprobado")
else:
    print("Nota incorrecta no sea caballo")
