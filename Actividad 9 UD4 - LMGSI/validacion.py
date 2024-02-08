import json
from jsonschema import validate

# Definir el esquema
schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "nombre": {
      "type": "string"
    },
    "marca": {
      "type": "string"
    },
    "precio": {
      "type": "number",
      "minimum": 0
    },
    "descripcion": {
      "type": "string"
    },
    "disponible": {
      "type": "boolean"
    },
    "dimensiones": {
      "type": "object",
      "properties": {
        "alto": {
          "type": "number",
          "minimum": 0
        },
        "ancho": {
          "type": "number",
          "minimum": 0
        },
        "profundidad": {
          "type": "number",
          "minimum": 0
        }
      },
      "required": ["alto", "ancho", "profundidad"]
    },
    "caracteristicas": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": ["nombre", "marca", "precio", "descripcion", "disponible", "dimensiones", "caracteristicas"]
}


# Archivo JSON a validar
archivo_json = '''
{
  "nombre": "Robot aspiradora",
  "marca": "CleanTech",
  "precio": 249.99,
  "descripcion": "Robot aspiradora inteligente con mapeo de habitaciones y control remoto.",
  "disponible": true,
  "dimensiones": {
    "alto": 30,
    "ancho": 30,
    "profundidad": 10
  },
  "caracteristicas": ["Mapeo inteligente", "Succión potente", "Control remoto"]
}

'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.