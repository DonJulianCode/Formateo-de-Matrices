✨ Características
Visualización de matrices con estilo personalizado (⎡ ⎤, ⎢ ⎥, ⎣ ⎦)

Soporte para:

Números enteros

Decimales

Símbolos (usando sympy.symbols)

Números aleatorios reproducibles

Fácil integración en notebooks de Colab o Jupyter

📦 Requisitos
sympy

numpy

Puedes instalar los paquetes necesarios con:

bash
Copiar
Editar
pip install sympy numpy
🔧 Funciones Principales
mostrar_matriz_formato(matriz, nombre="Matriz")
Muestra una matriz de SymPy con formato visual decorado.

python
Copiar
Editar
from sympy import Matrix
mostrar_matriz_formato(Matrix([[1, 2], [3, 4]]), "A")
crear_matriz_ejemplo(filas, columnas, tipo="enteros")
Genera una matriz de prueba según el tipo especificado:

'enteros'

'decimales'

'simbolos'

'aleatorios'

python
Copiar
Editar
matriz = crear_matriz_ejemplo(3, 3, 'simbolos')
mostrar_matriz_formato(matriz, "Símbolos")
matriz_desde_lista(lista, nombre="Matriz")
Crea y muestra una matriz a partir de una lista de listas.

python
Copiar
Editar
matriz_desde_lista([[7, 8], [9, 10]], "MiMatriz")
📘 Ejemplo Completo
python
Copiar
Editar
from sympy import Matrix
from sympy import symbols

# Crear una matriz simbólica 2x3
matriz = crear_matriz_ejemplo(2, 3, "simbolos")

# Mostrarla con nombre personalizado
mostrar_matriz_formato(matriz, "Ejemplo")
🤓 Ideal para
Clases de álgebra lineal

Presentaciones educativas

Proyectos de aprendizaje visual

Representación simbólica y numérica clara

📜 Licencia
Este módulo es de uso libre para fines educativos y personales.
Créditos a Julián Gómez Brizuela como autor original.
