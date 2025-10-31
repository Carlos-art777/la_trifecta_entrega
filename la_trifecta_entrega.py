# La Trifecta

#Consigna 01 - Al iniciar se nos debe pedir ingresar un numero entero, si este es
#distinto a 0 el programa inicia, de lo contrario finaliza (tambien si se
#ingresa otra cosa que no sea un numero entero).

while True:
    while True:
        numero = input("Ingresa un número: ")
    
        if numero.isdigit():
          numero= int (numero)
          if numero > 0:
            print ("Comenzar programa")
            break
          else:
            print("Programa finalizado")
            exit()

        else:
         print("Programa finalizado.")
         exit()
    

    

#Consigna 02 - Se debe poder ingresar una Palabra o Frase y contar cuantos
#caracteres tiene dicha palabra o frase

    frase = input("Ingresá una palabra o frase: ")
    cantidad = len(frase)
    print("Cantidad de caracteres de tu palabra o frase:", cantidad)

#Consigna 03 - Con el valor obtenido en el punto anterior calcular su Factorial, una
#vez hecho esto, decirnos si el resultado es par o impar.


    factorial = 1
    for i in range(1, cantidad + 1):
     factorial *= i
    print("El factorial de", cantidad, "es:", factorial)

    if factorial % 2 == 0:
     print("El factorial es PAR.")
    else:
     print("El factorial es IMPAR.")

#Consigna 04 - Se deben imprimir los resultados por pantalla en cada paso.

#Consigna 05 - Una vez cumplido esto, deberemos volver a pedir el ingreso de un
#número y realizar la verificación del punto 1

    print("_______________________")