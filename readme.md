## Obtención de AGEBs de México

Antes que nada, recuerda crear un entorno virtual de python e instalar los modulos de python `pip install -r requirements.txt` y tener instalado MongoDB porque se usará para guardar los geojson y posteriormente se usará su modulo optimizado para localización geográfica.

Correr el script en consola `sh 00_get_Mexico_ageb.sh` obtendrá los datos en formato geojson de AGEBs a partir de los datos de la UNAM actualizados hasta 2010 para todo México. El archivo pesa aproximadamente 164 M.

## Guardar los AGEBs a Mongodb

`01_save_ageb_mongo.py` Guarda los archivos geojson en mongodb. Se debe cambiar la ruta de mongo ya sea local o que viva en linea.

## Obtiene ageb de una coordenada

`02_get_ageb_sample.py` dadas la geolocalización de un dato, después de buscar el ageb dentro de mongodb, devuelve el indicador de estado, municipio y AGEB en consola

## Siguientes pasos:

- Dada una dirección: colonia, calle y número, usar geopy para obtener su lat y long
- Pasar una muestra csv de lat y long, pegarle su AGEB
- Pegarle datos de rezago social del inegi u otros datos de interes a nivel AGEB
