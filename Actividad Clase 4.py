gestionar_tareas = []


gestionar_tareas.insert(0, {"nombre": "estudiar", "descripcion": "Descripción de la Tarea 1", "estado": "lista"})
gestionar_tareas.insert(1, {"nombre": "comer", "descripcion": "Descripción de la Tarea 2", "estado": "ya comi"})
gestionar_tareas.insert(2, {"nombre": "dormir", "descripcion": "Descripción de la Tarea 3", "estado": "pendiente la siesta"})


tarea_eliminada = gestionar_tareas.pop(1)  

for i, gestionar_tareas in enumerate(gestionar_tareas):
    print(f"Tarea {i+1}:")
    print(f"  Nombre: {gestionar_tareas['nombre']}")
    print(f"  Descripción: {gestionar_tareas['descripcion']}")
    print(f"  Estado: {gestionar_tareas['estado']}")
    print() 
