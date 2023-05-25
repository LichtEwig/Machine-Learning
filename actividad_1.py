# ACTIVIDAD 1: EJERCICIOS DE PROGRAMACIÓN BÁSICA EN PYTHON
# **ADVERTENCIA**: No borrar los comentarios que se encuentran en el código, ya que son necesarios para la evaluación de la actividad.
# **ADVERTENCIA**: No cambiar el nombre del archivo, de lo contrario no se considerará entregado.
# **ADVERTENCIA**: El programa debe ejecutarse una vez y realizar todos los puntos de manera secuencial. No se evaluarán programas que ejecuten solo una parte.
# **ADVERTENCIA**: El código de cada actividad debe escribirse debajo de cada comentario correspondiente.

## ACTIVIDADES
# 1. Imprimir "¡Hola, mundo!" en la consola usando print().
print("¡Hola, mundo!")

# 2. Pedir al usuario que ingrese su nombre usando input() e imprimir un saludo en consola usando print().
nombre = input("Ingrese su nombre:")
print("hola", nombre)

# 3. Sumar dos números ingresados por el usuario mediante input() y luego mostrar el resultado en consola usando print().
num1 = input("por favor ingrese un numero: ")
num2 = input("por favor ingrese otro numero: ")

num1=int(num1)
num2=int(num2)

print("el resultado de la suma es: ",num1+num2)


# 4. Calcular el área de un triángulo a partir de la base y la altura ingresadas por el usuario mediante input() y luego mostrar el resultado en consola.
base=float(input('ingrese base del triangulo: '))
altura=float(input("ingrese altura del triangulo: "))

area=base*altura/2

print("el area del triangulo es: {}.".format(area))


# 5. Calcular el promedio de tres números ingresados por el usuario mediante input() y luego mostrar el resultado en consola.
alumno1=float(input('ingrese la primera nota: '))
alumno2=float(input('ingrese la segunda nota: '))
alumno3=float(input('ingrese la tercera nota: '))

promedio=(alumno1+alumno2+alumno3)/3

print("el promedio de las tres notas es: {}.".format(promedio))
# 6. Crear una lista con los siguientes números enteros: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] y mostrar por pantalla el resultado de sumar todos los números de la lista.
lista =[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def sumar(lista):

    suma = 0

    for num in lista:
        suma += num
    return suma


print(sumar(lista))

# 7. Crear una función que reciba un número entero como parámetro y retorne el resultado de multiplicarlo por 2. Imprimir el resultado de invocarla pasándole como argumento un 5.
def multiplicar(a,b):
    return a*b

a=int(input('por favor ingrese el numero 5: '))
b=2

print("el resultado de 5 multiplicado por 2 es: ",multiplicar(a,b))
 

# 8. Crear una función que reciba una cadena de texto como parámetro y retorne la cantidad de caracteres que tiene.
def contar_caracteres(cadena):
    return len(cadena)

texto = "Hola, mundo!"
cantidad_caracteres = contar_caracteres(texto)
print("La cantidad de caracteres es:", cantidad_caracteres)


# 9. Crear una función que reciba una lista de números enteros como parámetro y retorne el número más grande de la lista.

def encontrar_maximo(lista):
    if len(lista) == 0:
        return None
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo

numeros = [5, 10, 2, 8, 3]
maximo_numero = encontrar_maximo(numeros)
print("El número más grande es:", maximo_numero)


# 10. Crear una función que reciba una lista de cadenas de texto como parámetro y retorne la cantidad de cadenas que tienen más de 5 caracteres.

def contar_cadenas_largas(lista):
    contador = 0
    for cadena in lista:
        if len(cadena) > 5:
            contador += 1
    return contador

cadenas = ["Hola", "Mundo", "Python", "Programación", "Lenguaje"]
cantidad_cadenas_largas = contar_cadenas_largas(cadenas)
print("La cantidad de cadenas con más de 5 caracteres es:", cantidad_cadenas_largas)