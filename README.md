# 🔢 Visualizador de Matrices con Estilo

Una librería elegante para mostrar matrices matemáticas con formato visual atractivo en Python, perfecta para uso educativo y presentaciones académicas.

## ✨ Características

- **Visualización estilizada**: Matrices con bordes decorativos personalizados (`⎡ ⎤`, `⎢ ⎥`, `⎣ ⎦`)
- **Soporte completo para múltiples tipos de datos**:
  - Números enteros
  - Números decimales
  - Símbolos matemáticos (usando `sympy.symbols`)
  - Números aleatorios con semilla reproducible
- **Integración perfecta** con notebooks de Jupyter y Google Colab
- **Interfaz simple y intuitiva** para uso educativo

## 📦 Instalación y Requisitos

### Dependencias necesarias
- `sympy` - Para manipulación simbólica y matrices
- `numpy` - Para operaciones numéricas eficientes

### Instalación
```bash
pip install sympy numpy
```

## 🔧 API - Funciones Principales

### `mostrar_matriz_formato(matriz, nombre="Matriz")`
Renderiza una matriz de SymPy con formato visual decorativo y etiqueta personalizada.

**Parámetros:**
- `matriz` (Matrix): Matriz de SymPy a mostrar
- `nombre` (str): Etiqueta descriptiva para la matriz

**Ejemplo:**
```python
from sympy import Matrix
mostrar_matriz_formato(Matrix([[1, 2], [3, 4]]), "Matriz A")
```

### `crear_matriz_ejemplo(filas, columnas, tipo="enteros")`
Genera matrices de prueba con diferentes tipos de contenido para experimentación.

**Parámetros:**
- `filas` (int): Número de filas
- `columnas` (int): Número de columnas  
- `tipo` (str): Tipo de contenido
  - `'enteros'` - Números enteros secuenciales
  - `'decimales'` - Números decimales
  - `'simbolos'` - Variables simbólicas (a₁₁, a₁₂, etc.)
  - `'aleatorios'` - Números aleatorios reproducibles

**Ejemplo:**
```python
# Crear matriz 3x3 con símbolos
matriz_simbolica = crear_matriz_ejemplo(3, 3, 'simbolos')
mostrar_matriz_formato(matriz_simbolica, "Matriz Simbólica")

# Crear matriz 2x4 con números aleatorios
matriz_aleatoria = crear_matriz_ejemplo(2, 4, 'aleatorios')
mostrar_matriz_formato(matriz_aleatoria, "Números Aleatorios")
```

### `matriz_desde_lista(lista, nombre="Matriz")`
Convierte una lista de listas Python en una matriz SymPy y la muestra con formato.

**Parámetros:**
- `lista` (list): Lista de listas representando la matriz
- `nombre` (str): Etiqueta para la matriz

**Ejemplo:**
```python
datos = [[7, 8, 9], [10, 11, 12]]
matriz_desde_lista(datos, "Datos de Entrada")
```

## 📘 Ejemplos de Uso Completos

### Ejemplo Básico
```python
from sympy import Matrix, symbols

# Crear y mostrar una matriz numérica simple
matriz_nums = Matrix([[1, 2, 3], [4, 5, 6]])
mostrar_matriz_formato(matriz_nums, "Matriz Numérica")

# Crear matriz con símbolos personalizados
x, y, z = symbols('x y z')
matriz_simbolos = Matrix([[x, y], [z, x+y]])
mostrar_matriz_formato(matriz_simbolos, "Ecuaciones")
```

### Ejemplo Educativo Completo
```python
# Demostración para clase de álgebra lineal
print("=== DEMOSTRACIÓN DE MATRICES ===\n")

# 1. Matriz identidad
identidad = crear_matriz_ejemplo(3, 3, 'enteros')
mostrar_matriz_formato(identidad, "Matriz Ejemplo")

# 2. Matriz con variables
variables = crear_matriz_ejemplo(2, 3, 'simbolos') 
mostrar_matriz_formato(variables, "Sistema de Ecuaciones")

# 3. Datos experimentales
datos_lab = [[2.5, 3.7, 1.2], [4.1, 5.9, 2.8]]
matriz_desde_lista(datos_lab, "Resultados Experimentales")
```

## 🎯 Casos de Uso Ideales

- **📚 Educación**: Clases de álgebra lineal y matemáticas avanzadas
- **📊 Presentaciones**: Visualización clara de sistemas de ecuaciones
- **🔬 Investigación**: Representación de datos matriciales
- **💻 Notebooks**: Integración perfecta con Jupyter/Colab
- **📖 Documentación**: Ejemplos visuales en documentación técnica

## 🚀 Ventajas

- **Legibilidad mejorada**: Formato visual profesional
- **Flexibilidad**: Soporte para múltiples tipos de datos
- **Simplicidad**: API intuitiva con pocas funciones
- **Reproducibilidad**: Matrices aleatorias con semilla fija
- **Compatibilidad**: Funciona en cualquier entorno Python

## 📋 Requisitos del Sistema

- Python 3.6+
- SymPy 1.0+
- NumPy 1.15+

## 📜 Licencia

Este proyecto está disponible bajo licencia libre para uso educativo y personal.

**Autor**: Julián Gómez Brizuela

---

> 💡 **Consejo**: Para mejores resultados en notebooks, ejecuta las celdas en orden y asegúrate de que las dependencias estén correctamente instaladas.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, mantén el enfoque en simplicidad y uso educativo.

---
*Creado con ❤️ para la comunidad educativa*
