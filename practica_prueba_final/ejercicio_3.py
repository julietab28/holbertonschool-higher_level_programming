#!/usr/bin/python3
import json
from ejercicio_1 import Vehiculo

class Taller():
    """Clase para gestionar una lista de Vehiculos"""
    def __init__(self):
        self.list = [] #[{"marca": "owen", "modelo"= "quemado"}, {"marca": "lol", ...}, {...}, {...}]

    def agregar_vehiculo(self, vehiculo):
        self.list.append(vehiculo)

    def listar_vehiculos(self):
        for v in self.list:
            vehiculos = Vehiculo.to_dict(v)
            print(vehiculos)
        
    def guardar_datos(self, filename):
        list_v = []
        for vehiculo in self.list:
            list_v.append(vehiculo.to_dict())

        with open(filename, "w") as file:
            json.dump(list_v, file)
        
    
    def cargar_datos(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for vehiculo in data:
                    Vehiculo.from_dict(vehiculo)
        except ValueError as e:
            return "Error guei", str(e)