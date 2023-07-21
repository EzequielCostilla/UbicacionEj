import json


class Ubicacion:
    """ Ubicación de los destinos culinarios. """

    def __init__(self, id, direccion, coordenadas):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas

    def a_json(self):
        return {
            "id" : self.id,
            "direccion" : self.direccion,
            "coordenadas" : self.coordenadas
        }



ubicacion1 = Ubicacion(1, "Balcarce España", "-24.788625613902056, -65.41216688133615")

def convert_json_ubicacion(ubicacion):
    ubicacion_json = json.dumps(ubicacion.a_json())
    print(ubicacion_json)

convert_json_ubicacion(ubicacion1)