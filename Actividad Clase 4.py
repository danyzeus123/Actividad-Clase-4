gestionar_tareas = []

gestionar_tareas.insert(0, {"nombre": "dormir", "descripcion": "Descripción dormir", "estado": "falta siesta"})
gestionar_tareas.insert(1, {"nombre": "comer", "descripcion": "Descripción comer", "estado": "listo"})
gestionar_tareas.insert(2, {"nombre": "estudiar", "descripcion": "Descripción estudiar", "estado": "estoy en eso"})

tarea_eliminada = gestionar_tareas.pop(1)

for i, tarea in enumerate(gestionar_tareas):
    print(f"Tarea {i+1}:")
    print(f"  Nombre: {tarea['nombre']}")
    print(f"  Descripción: {tarea['descripcion']}")
    print(f"  Estado: {tarea['estado']}")
print() 