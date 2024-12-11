# ⬜ Suma de los primeros n números naturales: Calcula la suma de los números
# desde 1 hasta n utilizando un ciclo for. Itera sobre los números en el rango de 1
# a n y acumula su suma.


# n = int(input("Introduce un número entero positivo: "))

# suma = 0

# for i in range(1, n + 1):
#     suma += i  

# print(f"La suma de los primeros {n} números naturales es: {suma}")

#________________________________________________________________________________________

# ⬜  Factorial de un número dado: Encuentra el factorial de un número
# multiplicando todos los números desde 1 hasta ese número con un ciclo for.
# Asegúrate de inicializar la variable acumuladora en 1.


# n = int(input("Ingresa un número y encuentra el factorial: "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i  

# print(f"El factorial de {n} es: {factorial}")


#________________________________________________________________________________________

# ⬜  Números pares del 1 al 100: Usa un ciclo for para recorrer los números del 1
# al 100 e imprime solo aquellos que sean divisibles entre 2 (números pares).


# contador = 0
# pares = []


# for numero in range (1, 101):
#     if numero % 2 == 0:
#         contador += 1
#         pares.append(numero) 
# print(f"La cantidad de número pares {contador}")
# print(f"Los números pares son: {pares}")

#________________________________________________________________________________________

# ⬜  Suma de los dígitos de un número: Recorre cada dígito de un número
# (convirtiéndolo en una cadena de texto) y suma sus valores utilizando un
# ciclo for.

# numero = input("Introduce un número entero positivo: ")

# suma_digitos = 0

# for digito in numero:
#     suma_digitos += int(digito)  

# print(f"La suma de los dígitos de {numero} es: {suma_digitos}")

#________________________________________________________________________________________


# ⬜  Tabla de multiplicar de un número: Genera la tabla de multiplicar de un
# número dado del 1 al 10 utilizando un ciclo for. Por cada iteración, calcula el
# producto y muéstralo

# numero = int(input("ingresa el número del que quieras averiguar su tabla de multiplicar: "))

# print(f"Tabla de multiplicar del {numero}:")
# for i in range(1, 11): 
#     producto = numero * i
#     print(f"{numero} x {i} = {producto}")
    
#________________________________________________________________________________________

# ⬜ Verificación de número primo: Usa un ciclo for para verificar si un número es
# divisible por algún número entre 2 y su raíz cuadrada. Si no tiene divisores, es
# primo.


# numero = int(input("Ingresa el número del que quieras averiguar si es primo: "))

# if numero < 2:
#     print("No es un número primo")
# else:
#     es_primo = True
#     for i in range(2, numero):  
#         if numero % i == 0:
#             es_primo = False
#             break  

 
#     if es_primo:
#         print("Es un número primo")
#     else:
#         print("No es un número primo")


#________________________________________________________________________________________

        
# ⬜ Potencia de un número: Calcula la potencia de un número multiplicando la
# base por sí misma tantas veces como indique el exponente, utilizando un
# ciclo for.

# base = 2
# potencia = 7


# resultado = 1


# for i in range(potencia):
#     resultado = resultado * base 
# print(f"El resultado es: {resultado}")

#________________________________________________________________________________________


# ⬜Media de una lista de números: Recorre cada elemento de una lista con un
# ciclo for, acumula su suma y divide entre el número total de elementos para
# calcular la media.

# numeros = [1,2,3,4,5,6,7,8,9,10]

# suma = 0

# for i in numeros: 
#     suma += i
#     media = suma / i
    
# print(f"la suma es: {suma}")
# print(f"la media es: {media}")  

#________________________________________________________________________________________


# ⬜ Máximo común divisor (MCD): Encuentra el MCD de dos números utilizando
# el algoritmo de Euclides con un ciclo while, que repite el cálculo del residuo
# hasta que uno de los números sea cero.

#________________________________________________________________________________________


# ⬜ Cantidad de dígitos de un número: Usa un ciclo for para recorrer los
# caracteres de un número convertido a cadena de texto y cuenta cuántos tiene.

# numeros = 12934

# counter = 0

# for i in (str(numeros)):
#     counter += 1
    
# print(counter)
    
#________________________________________________________________________________________


# ⬜ Invertir un número: Recorre los dígitos de un número desde el principio hasta
# el final utilizando un ciclo for y constrúyelo en orden inverso.

# numeros = 123456

# resultado = ""

# for i in (str(numeros)):
#     resultado =  i + resultado 

# print(int(resultado))

#________________________________________________________________________________________


# ⬜ Número más grande en una lista: Compara los números de una lista uno por
# uno utilizando un ciclo for para encontrar el mayor de ellos.

# numeros = [-10,-2,-25]
# mayor = numeros[0]

# for i in numeros:
#     if i > mayor: 
#         mayor = i

# print(mayor)

#________________________________________________________________________________________


# ⬜ Verificar si un número es palíndromo: Usa un ciclo for para comparar los
# dígitos de un número desde los extremos hacia el centro y verifica si son
# iguales.

# numeros = 12334321
# numeros = str(numeros)
# resultado = ""

# OPCIÓN #1

# for i in numeros:
#     resultado = i + resultado
    
# if resultado == numeros:
#     print("es palíndromo")
# else:
#     print("no es palíndromo")

# OPCIÓN #2

# palindromo = True
# for i in range(len(numeros)//2): 
#     print(i)
#     if numeros[i] != numeros[-(i+1)]:
#         palindromo = False
#         break
# print(palindromo)

#________________________________________________________________________________________

# ⬜ Área de un triángulo: Calcula el área de un triángulo dada su base y altura con
# la fórmula (base * altura) / 2. Este ejercicio no requiere un ciclo for.

# base = 10
# altura = 20

# area = base * altura /2 

# print(area)
    
#________________________________________________________________________________________


# ⬜ Cantidad de vocales en una cadena: Recorre cada carácter de una cadena
# de texto con un ciclo for y cuenta cuántos de ellos son vocales.

# texto = "hola mundo"
# vocales = ["a", "e", "i", "o", "u"]

# counter = 0

# for i in texto:
#     if i in vocales:
#         counter += 1 
    
# print(counter)

#________________________________________________________________________________________

# Promedio ponderado: Calcula el promedio ponderado de una lista de
# calificaciones. Multiplica cada calificación por su peso en un ciclo for y divide
# entre el total de pesos.

# notas = [4.5, 4.0, 5.0, 4.3, 4.1]
# porcentajes = [0.25, 0.15, 0.30, 0.20, 0.10]  
# promedio = 0

# if sum(porcentajes) != 1:
#     print("Error: Los porcentajes no suman 1.")
# else:
#     for i in range(len(notas)): 
#         promedio += notas[i] * porcentajes[i]  
    
#     print("Promedio ponderado:", promedio)
#________________________________________________________________________________________

