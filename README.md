# etl-py
Se prevee de un servicio(`service.py`) que soporta un proceso de etl básico:
 
### Extract 
Se genera una dataframe con datos aleatorios haciendo uso de la libreria faker.

### Transform 
Prepara el dataframe y lo modela antes de realizar la ingesta. Se realiza una validación básica para determinar si no existen valores nulos antes de continuar.

### Load 
Se realiza la ingesta hacia el almacen de datos, por defecto hacia una instancia de PostgreSql desplegada en Azure. Se puede modificar en `db.py`.

## Tests
Las pruebas se centralizan en `tests\service.py` y validan:
* Conexión con el almacen de datos.
* Existencia del esquema, si no existe se crea.
* Inserción de un elemento en el almacen de datos. El rollback se encuentra desactivado por defecto en el fixture  db_session que engloba la sesion donde se ejecutan las transicciones de pruebas `tests\service.py:58`. 

Para ejecución de pruebas: `py -m pytest -v tests/service.py`

## App
Puede visualizar el almacen de datos ejecutando `app.py` y accediendo a http://127.0.0.1:8050


## Author
* Name: **Paulo H**
* Email: **paulo.ahll@gmail.com**



