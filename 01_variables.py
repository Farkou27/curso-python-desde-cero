# 📌 CLASE 1: VARIABLES EN PYTHON

# En Python NO necesitas poner int, float, string o bool. 
# El lenguaje detecta el tipo automáticamente.
nombre = "Franco"       # Esto es un String (texto)
edad = 20               # Esto es un Integer (entero)
altura = 1.75           # Esto es un Float (decimal)
le_gusta_cpp = True     # Esto es un Boolean (True o False con mayúscula)

# Para imprimir valores y texto juntos, no usas "cout <<". Usas una f-string (la forma más moderna):
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# Puedes comprobar qué tipo de dato le asignó Python usando type():
print(type(edad))      # Te mostrará <class 'int'>
print(type(altura))    # Te mostrará <class 'float'>
