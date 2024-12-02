#!/usr/bin/python3

class Vehiculo():
    """Clase para crear un Vehiculo"""
    def __init__(self, matricula, marca, modelo, año):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def to_dict(self):
        dict = {
                "matricula": self.matricula,
                "marca": self.marca,
                "modelo": self.modelo,
                "año": self.año
        }

        return dict

    @staticmethod
    def from_dict(data):
        #instance de un Vehiculo y le paso la data, key por key
        vehiculo = Vehiculo(data['matricula'], data['marca'], data['modelo'], data['año'])
        return vehiculo