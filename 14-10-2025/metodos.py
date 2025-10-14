# Pide una frase al usuario
# Quite los espacios del principio y del final
# Muestre cuantos caracteres tiene antes y despues de limpiar
# Reemplace todas las comas por puntos
# Separe la frase en palabras y muestre la lista
# Una las palabras con guiones y muestr el nuevo texto
# Compruebe si la frase final es alfanumerica, solo letras o solo numeros




frase = input("Escriba una frase: ")
frase_limpia = frase.strip()
frase_sustituida = frase.replace(",", ".")
frase_separada = frase.split()
frase_numeros = frase.isalnum()
frase_letras = frase.isalpha()

print(frase_limpia)
print(len(frase))
print(len(frase_limpia)) #Funcion por eso se escribe con la variable entre parentesis
print(frase_separada)
print(frase_sustituida)
print(frase_separada)
print(frase_letras)
print(frase_numeros)




# METODO DEL CHATGPT 


# Pide una frase al usuario
# frase = input("Escriba una frase: ")

# Quita los espacios del principio y del final
# frase_limpia = frase.strip()

# Reemplaza las comas por puntos
# frase_sustituida = frase_limpia.replace(",", ".")

# Separa la frase en palabras (lista)
# frase_separada = frase_sustituida.split()

# Une las palabras con guiones
# frase_guionada = "-".join(frase_separada)

# Comprueba tipo de contenido
# solo_numeros = frase_guionada.isdigit()
# solo_letras = frase_guionada.isalpha()
# alfanumerico = frase_guionada.isalnum()

#  Muestra resultados
# print("Frase limpia:", frase_limpia)
# print("Longitud original:", len(frase))
# print("Longitud limpia:", len(frase_limpia))
# print("Frase con puntos:", frase_sustituida)
# print("Lista de palabras:", frase_separada)
# print("Frase guionada:", frase_guionada)
# print("¿Solo números?:", solo_numeros)
# print("¿Solo letras?:", solo_letras)
# print("¿Alfanumérica?:", alfanumerico)

