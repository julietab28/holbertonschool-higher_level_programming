from ejercicio_1 import Vehiculo
from ejercicio_3 import Taller

vehicle1 = Vehiculo("ABC123", "Juli", "Pepe", 2000)
vehicle2 = Vehiculo("ABX123", "Juli", "Pepe", 2001)

taller = Taller()

filename = "vehicles.json"
#taller.cargar_datos(filename)

taller.agregar_vehiculo(vehicle1)

taller.agregar_vehiculo(vehicle2)

taller.listar_vehiculos()

#taller.guardar_datos(filename)

