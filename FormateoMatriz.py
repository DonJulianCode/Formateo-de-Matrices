"""
Módulo para mostrar matrices con formato visual personalizado
Autor: [Tu nombre]
Versión: 1.0
"""

import sympy as sp
from sympy import Matrix, symbols
import numpy as np

def mostrar_matriz_formato(matriz, nombre="Matriz"):
    """
    Muestra una matriz con formato visual personalizado.
    
    Args:
        matriz (Matrix): Matriz de SymPy a mostrar
        nombre (str): Nombre de la matriz a mostrar
    
    Example:
        >>> matriz = Matrix([[1, 2], [3, 4]])
        >>> mostrar_matriz_formato(matriz, "A")
        A = ⎡1  2⎤
            ⎣3  4⎦
    """
    filas, columnas = matriz.shape
    
    # Convertir elementos a strings para calcular anchos
    elementos_str = [[str(matriz[i, j]) for j in range(columnas)] for i in range(filas)]
    
    # Calcular el ancho máximo de cada columna
    anchos_columnas = []
    for j in range(columnas):
        ancho_max = max(len(elementos_str[i][j]) for i in range(filas))
        anchos_columnas.append(max(ancho_max, 4))  # mínimo 4 caracteres
    
    # Preparar el nombre de la matriz
    nombre_con_igual = f"{nombre} = "
    
    # Construir la representación
    for i in range(filas):
        if i == 0:
            # Primera fila: incluir nombre
            linea = nombre_con_igual + "⎡"
        else:
            # Otras filas: espacios para alinear
            linea = " " * len(nombre_con_igual) + "⎢" if i < filas - 1 else " " * len(nombre_con_igual) + "⎣"
        
        # Agregar elementos de la fila
        for j in range(columnas):
            elemento = elementos_str[i][j]
            linea += elemento.rjust(anchos_columnas[j])
            if j < columnas - 1:
                linea += "  "  # espacios entre columnas
        
        # Cerrar la fila
        if i == 0:
            linea += " ⎤"
        elif i == filas - 1:
            linea += " ⎦"
        else:
            linea += " ⎥"
        
        print(linea)

def crear_matriz_ejemplo(filas, columnas, tipo="enteros"):
    """
    Crea una matriz de ejemplo del tamaño especificado.
    
    Args:
        filas (int): Número de filas
        columnas (int): Número de columnas
        tipo (str): Tipo de elementos ('enteros', 'decimales', 'simbolos', 'aleatorios')
    
    Returns:
        Matrix: Matriz de SymPy con los elementos especificados
    
    Example:
        >>> matriz = crear_matriz_ejemplo(2, 3, 'decimales')
        >>> mostrar_matriz_formato(matriz, "Ejemplo")
    """
    if tipo == "enteros":
        elementos = [[i*columnas + j + 1 for j in range(columnas)] for i in range(filas)]
    elif tipo == "decimales":
        elementos = [[round((i+1)*(j+1)*1.23, 2) for j in range(columnas)] for i in range(filas)]
    elif tipo == "simbolos":
        elementos = [[symbols(f'a_{i+1}{j+1}') for j in range(columnas)] for i in range(filas)]
    elif tipo == "aleatorios":
        np.random.seed(42)  # Para reproducibilidad
        elementos = [[round(np.random.uniform(1, 10), 2) for j in range(columnas)] for i in range(filas)]
    else:
        raise ValueError("Tipo debe ser: 'enteros', 'decimales', 'simbolos', o 'aleatorios'")
    
    return Matrix(elementos)

def matriz_desde_lista(lista, nombre="Matriz"):
    """
    Crea y muestra una matriz desde una lista de listas.
    
    Args:
        lista (list): Lista de listas con los elementos de la matriz
        nombre (str): Nombre de la matriz
    
    Example:
        >>> matriz_desde_lista([[1, 2, 3], [4, 5, 6]], "MiMatriz")
    """
    matriz = Matrix(lista)
    mostrar_matriz_formato(matriz, nombre)
    return matriz
