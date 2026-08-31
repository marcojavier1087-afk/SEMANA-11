FILAS = 5
COLUMNAS = 5

matriz = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

for fila in range(FILAS):
    for columna in range(COLUMNAS):
        while True:
            entrada = input(f"Ingrese el valor para la posición [{fila}][{columna}]: ")
            try:
                valor = float(entrada)
                if valor.is_integer():
                    valor = int(valor)
                matriz[fila][columna] = valor
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")

print("\nMatriz ingresada:")
for fila in range(FILAS):
    for columna in range(COLUMNAS):
        print(matriz[fila][columna], end="\t")
    print()
    
       