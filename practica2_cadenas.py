Frase   = input("Ingresa una frase: ")# pide la frase
lista = Frase.split()# las separa
print("Lista de palabras:", lista)
for palabra in lista:
    print(palabra.upper())# convierte a mayusculas
search = input("¿Qué palabra quieres contar?: ")
cantidad = Frase.split().count(search)
print(f"La palabra '{search}' aparece {cantidad} veces.")
pal_replace = input("Escribe la palabra que quieres reemplazar: ")
nueva_pal = input("Escribe la nueva palabra: ")
frase_mod = Frase.replace(pal_replace, nueva_pal)# reemplaza la palabra
print("Frase modificada:", frase_mod)