"""
SISTEMA DE GESTIÓN DE ESTUDIANTES
Autor: [Tu Nombre]
Implementa: Estructuras lógicas y repetitivas
"""

estudiantes = []
calificaciones = {}

def agregar_estudiante():
    # ESTRUCTURA LÓGICA IF
    print("\n=== AGREGAR ESTUDIANTE ===")
    nombre = input("Nombre: ")
    codigo = input("Código: ")
    
    if nombre and codigo:
        estudiantes.append({"nombre": nombre, "codigo": codigo})
        calificaciones[codigo] = []
        print(f"✅ {nombre} agregado!")
    else:
        print("❌ Error: Complete todos los campos")

def agregar_calificacion():
    # ESTRUCTURA REPETITIVA WHILE
    print("\n=== AGREGAR CALIFICACIÓN ===")
    
    if not estudiantes:
        print("❌ No hay estudiantes")
        return
    
    # Mostrar estudiantes
    for i, est in enumerate(estudiantes, 1):
        print(f"{i}. {est['nombre']}")
    
    # Validar con WHILE
    valido = False
    while not valido:
        try:
            opcion = int(input("Seleccione estudiante: ")) - 1
            if 0 <= opcion < len(estudiantes):
                estudiante = estudiantes[opcion]
                valido = True
        except:
            print("❌ Ingrese número válido")
    
    # Otra validación con WHILE
    nota_valida = False
    while not nota_valida:
        try:
            nota = float(input(f"Nota para {estudiante['nombre']} (0-20): "))
            if 0 <= nota <= 20:
                calificaciones[estudiante['codigo']].append(nota)
                print(f"✅ Nota {nota} agregada!")
                nota_valida = True
            else:
                print("❌ Nota debe ser 0-20")
        except:
            print("❌ Ingrese número válido")

def mostrar_promedios():
    # ESTRUCTURA REPETITIVA FOR
    print("\n=== PROMEDIOS ===")
    
    if not estudiantes:
        print("No hay estudiantes")
        return
    
    for estudiante in estudiantes:
        codigo = estudiante['codigo']
        notas = calificaciones[codigo]
        
        print(f"\n{estudiante['nombre']}:")
        if notas:
            promedio = sum(notas) / len(notas)
            print(f"  Notas: {notas}")
            print(f"  Promedio: {promedio:.2f}")
            
            # ESTRUCTURA LÓGICA IF/ELSE
            if promedio >= 10:
                print("  Estado: 🎉 APROBADO")
            else:
                print("  Estado: 😢 REPROBADO")
        else:
            print("  Sin calificaciones")

def menu_principal():
    # ESTRUCTURA REPETITIVA WHILE principal
    while True:
        print("\n" + "="*40)
        print("SISTEMA DE GESTIÓN DE ESTUDIANTES")
        print("="*40)
        print("1. Agregar estudiante")
        print("2. Agregar calificación")
        print("3. Ver promedios")
        print("4. Salir")
        print("="*40)
        
        opcion = input("Opción: ")
        
        # ESTRUCTURA LÓGICA IF/ELIF
        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_calificacion()
        elif opcion == "3":
            mostrar_promedios()
        elif opcion == "4":
            print("\n👋 ¡Gracias por usar el sistema!")
            print(f"Total estudiantes: {len(estudiantes)}")
            break
        else:
            print("❌ Opción inválida")

# Iniciar programa
if __name__ == "__main__":
    print("🚀 SISTEMA INICIADO - By [Tu Nombre]")
    menu_principal()