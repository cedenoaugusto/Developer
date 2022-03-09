import doctest
import pytz
import json
import uuid
import random
import requests
import tkinter # para interfaces gráficas
import paramiko # para conectar a un FTP
import pandas as pd
from google.cloud import spanner
from datetime import datetime
from datetime import timedelta, date, datetime
from google.cloud import spanner, bigquery


IST = pytz.timezone('America/Santiago')

def doc_test(p1, p2):
    """"
    >>> doc_test(p1, p2)
    resultado_esperado
    """
    import doctest
    # ..

    # al final de la función se llama a este método para que ejecute la prueba unitaria desde la documentación,
    # y el resultado sea comparado con resultado_esperado
    # se requiere pasar el argumento -v al ejecutar el programa, ejemplo: python myPrograma.py -v
    doctest.testmod()

import unittest
class pruebas(unittest.TestCase):
    def unit_test(self):
        self.assertEqual(doc_test('p1', 'p2'), 'resultado_esperado')

if __name__ == '__main__':
    unittest.main()
    

transport = paramiko.Transport(('host', 'port'))
transport.connect(username = 'user_name', password = 'user_password')
sftp = paramiko.SFTPClient.from_transport(transport)
lst_files = sftp.listdir('ruta_archivos_remotos')
sftp.close()
transport.close()

from datetime import date, timedelta
fe_hasta = date.today()
fe_desde = fe_hasta - timedelta(days=1)
print('\nfe_desde:', fe_desde, '\nfe_hasta:', fe_hasta)


# https://www.onlinegdb.com/online_python_interpreter
df = pd.DataFrame
if isinstance(df['col', pd.Series]) is True:
	print('Esto es similar al is de c#')

# Separador de miles:
print("{:,}".format(12059).replace(',', '.'))

'''
raise Exception('Lanza una excepcion!')
raise ValueError('Lanza una excepcion de tipo ValueError. Es similar al throw new exception de c#()')
raise TypeError('Lanza una excepcion de tipo TypeError. Es similar al throw new exception de c#()')

%%writefile exportar_celda.py
%pwd

para interpolar rapidamente anteponer una f: f'El numero {i} es par'

# --
import json
x = '{"4": 5, "6": 7}'
x = json.loads(x)
print(type(x)) # -> <class 'dict'>
print(x) # -> {'4': 5, '6': 7}


x = '{"4": 5, "6": 7}'
x = json.dumps(x, indent=4)
print(type(x)) # -> <class 'str'>
print(x) # -> "{\"4\": 5, \"6\": 7}"


# --
manejar excepciones:
try:
    ...
except Exception as ex:
    print('An exception has occurred: ' + str(ex))


Las clases están grabadas:
https://vimeo.com/user/22350198/folder/1754914

.isalpha()
.isnumeric()

map
The map() function executes a specified function for each item in a iterable. The item is sent to the function as a parameter.
https://www.w3schools.com/python/ref_func_map.asp
https://www.geeksforgeeks.org/python-map-function/
map	(function, iterable)
desafio latam: "map se usa para transformar"
from functools import reduce
# Se opera sobre "lista", donde uno de los parámetros (x) actúa como acumolador,
# y el otro (y) actúa como iterador
reduce(lambda x, y : x + y, lista)


filter
The filter() method constructs an iterator from elements of an iterable for which a function returns true.
filter(function, iterable)

reduce
The reduce(fun, seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along. This function is defined in “functools” module.
from functools import reduce
https://www.geeksforgeeks.org/reduce-in-python/

DataFrame
df.iterrows() df.iteritems() y df.itertuples()

Numpy es un módulo o librería, que constituye una de las piedras angulares en el desarrollo de la computación numérica en Python.
Numpy presenta un arreglo n-dimensional llamado ndarray. Este es un contenedor muy rápido y flexible para grandes cantidades de datos. Mediante éstos, se pueden generar operaciones entre vectores de manera similar a como se realizan entre escalares.

Los ndarray son contenedores multidimensionales genéricos para datos homogéneos. Esto es muy
relevante, porque para aprovechar la naturaleza del tipeo dinámico de Python, debemos asegurarnos de la homogeneidad de los elementos a ingresar. Mediante esta definición de datos homogéneos, es posible realizar esta serie de operaciones de manera fácil y rápida.

Todo ndarray tiene un shape asociado que se expresa mediante una tupla. La tupla nos entrega
información sobre las dimensiones y tamaño de cada dimensión. También tiene un dtype que nos
entrega información sobre los tipos de datos contenidos en el ndarray.

Contar mas de una columna
print((dfAtletas.groupby(['ID', 'Name'])).size())

lists comprehension
# --
Diccionarios
Para castear dict()
métodos: .items() .values()

Crear una variable vacía de tipo diccionario:
newDictionary = {} #forma 1
newDictionary = dict() #forma 2

Cargar un diccionario en un DataFrame
pd.DataFrame(MyDict)

En algunos casos ocurre este error: If using all scalar values, you must pass an index
pd.DataFrame([MyDict])


*args
https://book.pythontips.com/en/latest/args_and_kwargs.html
def suma(*nros):
    total=0
    for n in nros:
        total += n
    print(total)    
suma(1, 2, 3, 4)
suma(1, 2, 3, 4, 5)
'''
#=======================================================================

# ============================== API # =========================================
import json
json.loads(stringJson)

import requests
url = "https://jsonplaceholder.typicode.com/posts"
headers = {
	'cache-control': 'no-cache',
	'Postman-Token': '2defb9f3-9b11-499b-be4f-82505a2f8e1a',
}
response = requests.request("GET", url, headers=headers)
# Cuerpo de la respuesta o "body"
print(response.text)
# Código de la respuesta
print(response)

# ---

#Función genérica para invocar un servicio web REST
import json
import requests
def request(requested_url):
	headers = {
		"cache-control": "no-cache",
		"Postman-Token": "2defb9f3-9b11-499b-be4f-82505a2f8e1a",
	}
	response = requests.request("GET", requested_url, headers=headers)
	return json.loads(response.text)
# --
# Crear un archivo y escribir contenido en él
with open("C:\\salida.html", "w") as file:
    file.write("Ingresando Texto")

# ---

import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
payload = "{\n\t\"title\": \"Cambio de post\",\n\t\"body\": \"Actualizando el post\",\n\t\"userId\": 1\n}\n"
#otra manera de cargar el payload
strPayLoad = {
    'title':'Cambio de post',
    'body':'Actualizando el post',
    'userId':'1'
    }
payload = json.dumps(strPayLoad)

headers = {
    "Content-Type" : "application/json",
    "cache-control" : "no-cache",
    "Postman-Token" : "563a09ea-fdff-4a54-be88-7d8ec46bd01c",
    "app_id" : "e51457d3",
    "app_key" : "6cf09f1d0edbefd2381f937f396150a3"
}
response = requests.request("PUT", url, data=payload, headers=headers)
print(response.text)
#En algunos casos nos tocará ingresar la clave en el body. Esto depende de cómo esta construida la API.
#En algunos casos, el token de autenticación cambiará después de cada request y tendremos que usar el último valor para rescatar el siguiente.
#También existen otros modelos más complejos como el de Facebook y el de Twitter que al día de hoy ocupan OAuth2.

# ---

import json
import requests
try:
    url = "https://mcrtlgjr-g-gwpsc952zwcc7q2vy.auth.marketingcloudapis.com/v2/token"

    payload = {
        "grant_type": "client_credentials",
        "client_id": "9kykprksdehkx1ggutmxrmfp",
        "client_secret": "8cApGfA5dvqhq3xGRWKQCV4Q",
        "account_id": "6189516"
    }
    payload = json.dumps(payload)

    cabecera = {}

    respuesta = requests.post(url, data = payload, headers = cabecera)

    if respuesta.status_code != 200:
        respuesta.raise_for_status()

    respuestaJson = respuesta.json()
    
    salida = '{\n\t"access_token" : "{0}"\n}'.replace('{0}', respuestaJson['access_token'])
    #salida = '{\n\t"access_token" : "' + respuestaJson['access_token'] + '"\n}'
    json.loads(salida)
    print(salida)
    
except requests.HTTPError as httpException:
    print(httpException)
except Exception as ex:
    print('Ocurrio una excepcion')
    print(str(ex))


# --
# LEE DE UNA DATA EXTENSION
import json
import requests

rut_filter = "CL0117023268"

if respuesta.status_code != 200:
    respuesta.raise_for_status() # se va automáticamente al except si la respuesta no es 200

access_token = respuesta.json()['access_token']
#print(access_token)

# get de salesforce
cabecera = { "Authorization": "Bearer {}".format(access_token) }
ekdt = '26793B0B-523C-459D-821C-3DC62A2EE0A4' #external_key_data_extension

url_sfmk = 'https://mcrtlgjr-g-gwpsc952zwcc7q2vy.rest.marketingcloudapis.com/data/v1/customobjectdata/key/{}/rowset?$filter=RUT%20eq%20"{}"'.format(ekdt, rut_filter)
respuesta = respuesta = requests.get(url_sfmk, headers=cabecera)
print(respuesta.json())



'''
# --
# --
https://flask.palletsprojects.com/en/1.0.x/api/
return request_object.scheme > http
return request_object.full_path > /?
return request_object.method -> GET, POST, etc.

cuando llamo: https://xxx/cf_crm_api_gateway_sod_servicio_ces_DEV/test
Ojo aunque la llamada fue por HTTPS la respuesta fue de la url fue sin S HTTP
request_object.full_path -> /test?
request_object.url -> http://us-central1-sod-cl-bi-sandbox.cloudfunctions.net/test
'''


# --
# --
#esto es una cloud function de GCP
def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'
#=======================================================================


'''
#=======================================================================
Ventajas de SSL
Cifra el mensaje impidiendo que terceros puedan leerlo.
Asegura que el emisor es quien dice ser, porque si alguien mas cifró el mensaje con una llave distinta,
el mensaje no tendrá sentido al desifrarlo.

Al momento de conectarnos a un sitio web que utilice SSL con un navegador, se establece un acuerdo, llamado en inglés handshake, de forma automática. En este handshake el servidor envía un certificado que tiene el nombre del sitio y la clave pública al cliente.

El cliente ocupa la clave pública que viene en el certificado para cifrar un mensaje y se la devuelve al servidor. Si el servidor puede descifrar el nuevo mensaje significa que el servidor tiene la clave privada correcta.

Dentro del proceso, cliente y servidor crearon una clave secreta especial utilizando los números que se enviaron durante el handshake. Durante el resto del proceso, se ocupa un sistema de cifrado simétrico utilizando esta única clave que nunca fue transmitida pero que ambos servidores tienen.

print(type(response)) # <class 'requests.models.Response'>
print(type(response.text)) # <class 'str'>
print(json.loads(response.text)) # retorna un tipo diccionario


export HADOOP_HOME_WARN_SUPPRESS=1
export HADOOP_ROOT_LOGGER="WARN,DRFA"
#=======================================================================


#=======================================================================
https://googleapis.dev/python/bigquery/latest/index.html
from google.cloud import bigquery

client = bigquery.Client()

# Perform a query.
sql_query = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(sql_query)  # API request
result = query_job.result() # Waits for query to finish
for row in result:
    print(row)
    print(row[0])
    print(row.nombre_de_la_columna)
    
--
ROW COUNTS EN UN SELECT
client = bigquery.Client()
query_job = client.query(sql_query)  # API request - starts the query
result = query_job.result()  # Wait for query to complete.
print("Total Rows {}.".format(result.total_rows))

ROW COUNTS EN UN INSERT / UPDATE
client = bigquery.Client()
query_job = client.query(sql_query) # Make an API request.
_ = query_job.result() # Wait for the job to complete.
print("Rows {} affected.".format(query_job.num_dml_affected_rows))

https://cloud.google.com/bigquery/docs/reference/libraries

https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.job.QueryJob.html
#=======================================================================
'''


#=======================================================================
#Convertir columna categorica en numerica
x=df['y']

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(x)
y=le.transform(x)

#Particionamiento del conjunto en 5 folds
from sklearn.model_selection import KFold

# Imprimir los contenidos de los conjuntos de entrenamiento y test
print('{:^61} {}'.format('Ejemplos entrenamiento', 'Ejemplos test'))

for i in range(40):
    kf = KFold(n_splits=5, shuffle=False)
    kf.get_n_splits(x)
    for train_index, test_index in kf.split(x):
         print("TRAIN:", train_index, "TEST:", test_index)
#=======================================================================


# ========================== pandas # ======================================
#para leer 10 registros
df = pd.read_csv('worldcup2014.csv')[:10]

np.median(df['mi_columna']) #con numpy
df['mi_columna'].median() # con pandas

df['ha_ganado'] = df['juegos_ganados'].apply(lambda x : 1 if x > 0 else 0)

df.groupby('continent').clasificado.value_counts('%')
df.groupby('continent')['clasificado'].value_counts('%')
#=======================================================================


# =========================== PY # =====================================
# cast string json a object JSON
import json
s = '{"success": "true", "status": 200, "message": "Hello"}'
d = json.loads(s)
print(d["success"], d["status"])
# true 200

# --

# cast object JSON a string json
dict_object = {"first_key": "first_value", "second_key": "second_value"}
json_string = json.dumps(dict_object)
print(json_string)

# --
# Para usar requests en la cloud function se debe declarar en el requirements.txt esto: requests==2.25.1

# =========================== Inicio Spanner # =====================================
def SELECT(sql_query, database_id='sbx_crm_whatsapp_ces', instance_id='sod-cl-bi-sandbox'):
    '''Ejecuta consultas SQL en la BBDD Spanner'''
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(sql_query)
        return results


def execute_select(sql_query, database_id='sbx_crm_whatsapp_ces', instance_id='sod-cl-bi-sandbox'):
    '''Ejecuta consultas SQL en la BBDD Spanner'''
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(sql_query)
        return results


def INSERT(rut_encriptado, otp, fe_vigencia_otp):
    spanner_client = spanner.Client()
    instance = spanner_client.instance('sod-cl-bi-sandbox')
    database = instance.database('sbx_crm_whatsapp_ces')

    def insertar(transaction):
        sql_query = f"INSERT INTO tbl_otp (rut_hashed, otp, vigencia_otp) VALUES ('{rut_encriptado}', '{otp}', '{fe_vigencia_otp}')"
        row_ct = transaction.execute_update(sql_query)
        print(f'{row_ct} filas insertadas.')
            
    database.run_in_transaction(insertar)

		
def INSERT_BATCH(funcion = "", descripcion = ""):
    """Es mas eficiente para insertar grandes cantidades"""
    aplicacion = "cf_crm_sod_servicio_ces_envio_otp"

    id_log = str(uuid.uuid4())
    spanner_client = spanner.Client()
    instance = spanner_client.instance('sod-cl-bi-sandbox')
    database = instance.database('sbx_crm')

    fecha = datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S')
    fecha = cast_str_to_datetime(fecha)
    def insert_log(transaction):
        sql_query = f"INSERT INTO tbl_log_errores (id_log, aplicacion, funcion, descripcion, fecha) VALUES ('{id_log}', '{aplicacion}', '{funcion}', '{descripcion}', '{fecha}')"
        _ = transaction.execute_update(sql_query)

    database.run_in_transaction(insert_log)

    # with database.batch() as batch:
    #     batch.insert(
    #         table='tbl_log_errores',
    #         columns=('id_log', 'aplicacion', 'funcion', 'descripcion', 'fecha'),
    #         values=[(id_log, aplicacion, funcion, descripcion, fecha)]
    #     )

def INSERT_UPDATE(rut_encriptado, otp, fe_vigencia_otp):
    spanner_client = spanner.Client()
    instance = spanner_client.instance('sod-cl-bi-sandbox')
    database = instance.database('sbx_crm_whatsapp_ces')

    def update_otp(transaction):
        sql_query = f"UPDATE tbl_otp SET otp='{otp}', vigencia_otp='{fe_vigencia_otp}' WHERE rut_hashed='{rut_encriptado}'"
        _ = transaction.execute_update(sql_query)

    def insert_otp(transaction):
        sql_query = f"INSERT INTO tbl_otp (rut_hashed, otp, vigencia_otp) VALUES ('{rut_encriptado}', '{otp}', '{fe_vigencia_otp}')"
        _ = transaction.execute_update(sql_query)
        
    results = execute_select(f"SELECT 1 FROM tbl_otp WHERE rut_hashed = '{rut_encriptado}'", 'sbx_crm_whatsapp_ces')
    b_actualizar = False
    for row in results:
        b_actualizar = True
            
    if b_actualizar == True:
        database.run_in_transaction(update_otp)
    else:
        database.run_in_transaction(insert_otp)

def borrar_tablon_spanner():
# OJO Actualmente spanner no admite borrar mas de 20.000 registros en una sola ejecución. 2021-09-01
    '''Borra la tabla tbl_tablon_ces_consolidado de Spanner'''
    spanner_client = spanner.Client()
    instance = spanner_client.instance('sod-cl-bi-sandbox')
    database = instance.database('sbx_crm_whatsapp_ces')

    def borrar(transaction):
        return transaction.execute_update("DELETE FROM tbl_tablon_ces_consolidado WHERE 1 = 1")

    row_ct = database.run_in_transaction(borrar)

    print(f'{row_ct} registros eliminados.')

# =========================== Fin Spanner # =====================================


# ======================== Inicio Funciones frecuentes # =============================
def cast_str_to_datetime(cadena):
    '''Convierte la fecha string en datetime'''
    fecha = cadena.replace('-', ',').replace(':', ',').replace(' ', ',')
    fecha = fecha.split(',')
    longitud = len(fecha)
    
    if longitud == 3:
        fecha = datetime(int(fecha[0]), int(fecha[1]), int(fecha[2]))
    elif longitud == 5:
        fecha = datetime(int(fecha[0]), int(fecha[1]), int(fecha[2]), int(fecha[3]), int(fecha[4]))
    elif longitud == 6:
        fecha = datetime(int(fecha[0]), int(fecha[1]), int(fecha[2]), int(fecha[3]), int(fecha[4]), int(fecha[5]))
    return fecha
		

def get_paypload():
    '''Obtener el payload para solicitar el access token de salesforce'''
    results = execute_select('SELECT valor FROM tbl_parametros WHERE codigo = "PAYLOAD_SF_GET_ACCESS_TOKEN"', 'sbx_crm')
    for r in results:
        return r[0]
    return ''


def get_access_token():
    '''Obtener el access token de salesforce'''
    url_access_token = 'https://mcrtlgjr-g-gwpsc952zwcc7q2vy.auth.marketingcloudapis.com/v2/token'
    payload = get_paypload()

    if len(payload) > 0:
        respuesta = requests.post(url_access_token, data=payload)
        if respuesta.status_code != 200:
            respuesta.raise_for_status() # se va automáticamente al except si la respuesta no es 200
        return respuesta.json()['access_token']
    else:
        return ''
# ======================== Fin Funciones frecuentes # =============================

def temp():
    status_code = 200
    if request.headers.get('key'):
        if request.headers.get('key') == 'dbfae0dde1f1491b8bf2368a38f448f1':
            mensaje = ''
        else:
            mensaje = "API-key no valida"
            status_code = 400
    else:
        mensaje = "Debe enviar la API-key"
        status_code = 400

    return mensaje, status_code


'''
Emulate Emular Flask
https://flask.palletsprojects.com/en/2.0.x/reqcontext/
https://stackoverflow.com/questions/7428124/how-can-i-fake-request-post-and-get-params-for-unit-testing-in-flask
Ejemplos: 
D:\Developer\Python\flask_test.py
D:\Sodimac\Proyectos\GeoPush - MOCA\source\Deploy Cloud Function\cf_crm_moca_geopush_core\unit_test.py
'''


# Fechas
fecha_dt=datetime(2022, 1, 6, 23, 59, 59, 999999)
my_date_aware = pytz.utc.localize(fecha_dt) # le asigna el UTC 0 a la fecha dada

# DocsString
help(temp) #muestra información de la función

class Estudiante:
    def calclularNotas(self, id): #self es un parametro obligatorio por estar dentro de una clase
        None


#Comparar 2 jupyter notebooks .ipynb nbdime #pip install nbdime