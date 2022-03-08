`sklearn.cluster` para implementar KMeans. ASí sucesivamente.

from sklearn.cluster import KMeans

# son equivalentes 
# contar nulos / perdidos
print('\nContar los nulos:')
display(df.isnull().sum())

# valores perdidos / nulos
print('\nValores los valores pérdidos:')
display(df.isna().sum())


Autocompletar con Tab
Leer documentación Shift + Tab
Ejecutar celda Shift + Enter
Ejecutar celda y permanecer Shift + Enter
Paleta de comandos Shift + cmd + P
En jupyter notebook, al ejecutar una celda ?print() arroja la ayuda del método

medidas de tendencia central:
Las medidas de tendencia central son medidas estadísticas que pretenden resumir en un solo valor a un conjunto de valores.
- media -> es el promedio
- moda -> valor que mas se repite
- mediana -> es el valor que ocupa el lugar central de todos los datos cuando éstos están ordenados de menor a mayor. el objetivo es identificar el punto equidistante de una variable.

Mediana
La mediana de un conjunto de números es el número medio en el conjunto.

la varianza: La varianza es una medida de dispersión que representa la variabilidad de una serie de datos respecto a su media. 
Formalmente se calcula como la suma de los residuos al cuadrado divididos entre el total de observaciones.

se puede calcular la moda con: scipy o con numpy
from scipy import stats
stats.mode(df['col'])


Desviacion Standar STD
Es una medida que se utiliza para cuantificar la variación o la dispersión de un conjunto de datos numéricos.
Una desviación estándar baja indica que la mayor parte de los datos de una muestra tienden a estar agrupados cerca de su media.
desviacion estandar = raiz cuadrada de la varianza
np.sqrt(np.var(df['mi_columna']))

Puntuacion Z
En estadística, la puntuación Z (o puntuación estándar) de una observación es el número de desviaciones estándar que hay por encima o por debajo de la media de población.

Si la variable objetivo es continua se debe usar Regresion?

# generamos un array de 1000000 observaciones con `np.arange`
demo_array = np.arange(10)
demo_array

para visualizar un dataframe correctamente en lugar de usar un print lo mejor es usar la funcion display.

el error cuadrático medio es el promedio de la diferencia cuadrática entre cada punto predicho y el punto real.

import pandas as pd
import numpy as py
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Credit.csv')


print(f'Mi variable es: {mi_variable}') 
#es similar a 
print('{}'.format(mi_variable)) 

for i in df['col'].index:
	print(i)
	
# ver tipos
df.dtypes


for colnames, datos in df.iteritems():
	print(colnames)
	print(datos)

for indice, serie_fila in df.iterrows():
	print(indice)
	print(serie_fila)

# Especificar el tipo de dato al momento de la carga de los datos.
pd.read_csv('mi_bbdd.csv', dtype = {'year' : np.int32})


# Boolean Subset
df[df['edad'] > 18]


# 
Eventos Independientes y Dependientes

Para usar comparaciones de vectores en pandas usar preferentemente & y |
(buscar mascaras booleanas para aclarar dudas)

# if corto
a1 = lambda x : 1 if x > 2 else 0

# contar elementos en una lista


# estoy creando una columna con los valores 1 ó 0
df['ha_ganado'] = df['juegos_ganados'].apply(lambda x : 1 if x > 0 else 0)

#remover valores NaN del DataFrame
pd.DataFrame.dropna( df.where( df['ha_ganado'] == 0 ) )
que seria equivalente a 
df[ df['ha_ganado'] == 0 ]

# filtrar en una lista (list filter)
numbers = [1, 2, 3, 4]
filtered_numbers = [number for number in numbers if number < 3]
# con un lamda sería:
an_iterator = filter(lambda number: number < 3, numbers)

#aleatorios
rango = 1 # genera numeros debajos del rango
np.random.randint(rango, size=10)


// list comprehension
https://www.programiz.com/python-programming/list-comprehension


Variable aleatoria: 
Discretas: seria cuando el espacio muestral es finito.
Podríamos definirla como cualquier variable que pueda tomar un número finito de valores entre dos valores.

Continuas: puede tomar infinitos valores.  un ejemplo: la temperatura.
https://estadisticamente.com/variables-discretas-y-variables-continuas/


Calcular el puntaje Z
Z = ( Xi − promedio(X) ) / σ (X),  
σ es la desviación estándar para la serie


Eliminar datos NaN en un DataFrame en columnas especificas:
df_ordenado.dropna(subset=['mi_colunma'])

plt.style.use('seaborn')
plt.style.use("Solarize_Light2")

plt.rcParams['figure.figsize'] = (8, 6)


Semana 5
~ significa se ve afectado por
smf.ols('Income ~ Limit', df)

Machine Learning 
Aprendizaje Automático:
Variable Objetivo: V.O. se denota como y griega en minuscula.
y = columnas de entrenamiento
X será el Data Set que analiza.
X = columnas de datos
 
sumarize se detalle en Evaluación de coeficientes de regresión


linestyle -> solid, dotted, dashed, dashdot
https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html


Videos de clase:
https://vimeo.com/user/22350198/folder/2970924

Correlacion de variables:
import seaboron as sns
sns.heatmap(df.corr(), cmap='Blues', annot=True)

sns.joinplot(df['col1'], df['col2'])

grid = sns.PairGrid(df)
grid = grid.map_diag(sns.displot)

forma de expresarlo: "se rechaza la hipotesis"

la hipótesis nula va de la mano de lo que se quiere probar
