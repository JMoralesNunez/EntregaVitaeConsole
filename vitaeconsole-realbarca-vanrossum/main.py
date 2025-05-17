import re
from datetime import datetime
import json

# Diccionario de usuarios
usuarios = {
    "1": {
        "datosPersonales": {
            "nombre": "J",
            "identificadores": ("1000456789", "12/88/2005"),
            "contacto": "31359450559",
            "dirección": "Cra12 #34 A 45",
            "correo": "miguelarias@gmail.com",
        },
        "formacionAcademica": [{"Universidad": "ECCI", "Titulo": "Profesional lenguas modernas", "añoGraduación": "2024"}],
        "experienciaProfesional": [{"Empresa": "Teleperformance", "Cargo": "Asesor Bilingüe", "Duración": "10"}, {"Empresa": "Concentrix", "Cargo": "Asesor Bilingüe", "Duración": "4 meses"}],
        "referenciasPersonales": [{"nombre": "miguel angel arias marin II", "relación": "vecino", "telefono": "3205118016"}],
        "habilidadesAdicionales": ["HTML", "CSS", "Python", "Inglés B2", "Diploma Pedagogía"]
    }
}

serial = len(usuarios)

# Funciones proporcionadas
def generar_hoja_de_vida(usuario, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("========== HOJA DE VIDA ==========\n\n")
        dp = usuario["datosPersonales"]
        archivo.write(">> DATOS PERSONALES\n")
        archivo.write(f"Nombre: {dp['nombre']}\n")
        archivo.write(f"Número de Identificación: {dp['identificadores'][0]}\n")
        archivo.write(f"Fecha de Nacimiento: {dp['identificadores'][1]}\n")
        archivo.write(f"Celular: {dp['contacto']}\n")
        archivo.write(f"Dirección: {dp['dirección']}\n")
        archivo.write(f"Correo Electrónico: {dp['correo']}\n\n")
        archivo.write(">> FORMACIÓN ACADÉMICA\n")
        for fa in usuario["formacionAcademica"]:
            archivo.write(f"- Universidad: {fa['Universidad']}\n")
            archivo.write(f"  Título: {fa['Titulo']}\n")
            archivo.write(f"  Año de Graduación: {fa['añoGraduación']}\n")
        archivo.write("\n")
        archivo.write(">> EXPERIENCIA PROFESIONAL\n")
        if usuario["experienciaProfesional"]:
            for exp in usuario["experienciaProfesional"]:
                archivo.write(f"- Empresa: {exp['Empresa']}\n")
                archivo.write(f"  Cargo: {exp['Cargo']}\n")
                archivo.write(f"  Duración: {exp['Duración']}\n")
        else:
            archivo.write("Sin experiencia laboral registrada.\n")
        archivo.write("\n")
        archivo.write(">> REFERENCIAS PERSONALES\n")
        for ref in usuario["referenciasPersonales"]:
            archivo.write(f"- Nombre: {ref['nombre']}\n")
            archivo.write(f"  Relación: {ref['relación']}\n")
            archivo.write(f"  Teléfono: {ref['telefono']}\n")
        archivo.write("\n")
        archivo.write(">> HABILIDADES ADICIONALES\n")
        if usuario["habilidadesAdicionales"]:
            for hab in usuario["habilidadesAdicionales"]:
                archivo.write(f"- {hab}\n")
        else:
            archivo.write("Sin habilidades adicionales registradas.\n")
        archivo.write("\n")
        archivo.write("==================================\n")

def generarJsonCompleto(datos):
    path = "datos.json"
    with open(path, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
        print("json creado exitosamente")

def filtrarHojasAños(datos, limite):
    filtro = dict()
    for user, value in datos.items():
        for item in value["experienciaProfesional"]:
            try:
                duracion = int(re.match(r'^\d+', item["Duración"]).group())
                if duracion >= limite:
                    filtro[user] = value
                    break
            except (AttributeError, ValueError):
                continue
    return filtro

def generarJsonAños(datos):
    pathAños = "filtroAños.json"
    with open(pathAños, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
        print("json creado exitosamente")

def filtrarFormación(datos, formación):
    filtro = dict()
    for user, value in datos.items():
        for item in value["formacionAcademica"]:
            if item["Titulo"] == formación:
                filtro[user] = value
                break
    return filtro

def generarJsonFormacion(datos):
    pathFormación = "formación.json"
    with open(pathFormación, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
        print("json creado exitosamente")

def filtrarHabilidades(datos, habilidad):
    filtro = dict()
    for user, value in datos.items():
        for item in value["habilidadesAdicionales"]:
            if item == habilidad:
                filtro[user] = value
                break
    return filtro

def generarJsonHabilidades(datos):
    pathHabilidades = "habilidades.json"
    with open(pathHabilidades, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)
        print("json creado exitosamente")

def datosPersonalesDict(nombre, identificacion, fecha, contacto, direccion, correo):
    lista = [identificacion, fecha]
    tupla = tuple(lista)
    diccionario = {"nombre": nombre, "identificadores": tupla, "contacto": contacto, "dirección": direccion, "correo": correo}
    return diccionario

def formaciónDict(universidad, titulo, año):
    diccionario = {"Universidad": universidad, "Titulo": titulo, "añoGraduación": año}
    return diccionario

def referenciasDict(nombre, relación, telefono):
    diccionario = {"nombre": nombre, "relación": relación, "telefono": telefono}
    return diccionario

# Añadir nuevo usuario
def añadir_usuario():
    global usuarios, serial
    serial += 1
    usuarios[str(serial)] = {}
    listaFormaciones = []
    listaReferencias = []
    experiencias = []
    habilidades = []

    # Datos personales
    print("A continuacion se le pediran sus datos personales")
    while True:
        nombre = input("Ingresa tu nombre: ")
        if nombre.isalpha():
            break
        else:
            print("Ingresa un nombre valido.")
    while True:
        identificacion = input("Agrega tu numero de identidad: ")
        if identificacion.isdigit() and 8 <= len(identificacion) <= 10:
            break
        else:
            print("La identificacion no es válida: ")
    while True:
        fecha_nacimiento = input("Ingresa tu fecha de nacimiento (DD/MM/AA): ")
        try:
            fecha = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            hoy = datetime.now()
            if fecha >= hoy:
                print("La fecha no puede ser el dia actual")
            else:
                print("Fecha válida:", fecha.strftime("%d/%m/%Y"))
                break
        except ValueError:
            print("Error: Formato de fecha inválido. Usa DD/MM/YYYY (ej: 15/05/2000).")
    while True:
        celular_numero = input("Ingresa tu numero de celular: ")
        if celular_numero.isdigit() and len(celular_numero) == 10:
            break
        else:
            print("El numero de celular no es válido")
    while True:
        direccion = input("Ingresa la direccion de tu vivienda: ")
        if re.match(r'^[a-zA-Z0-9\sáéíóúñÁÉÍÓÚÑ#\-/.,()]+$', direccion):
            if len(direccion) >= 5:
                print("Direccion valida ")
                break
            else:
                print("La direccion debe de contener al menos 5 caracteres (Debe ser real)")
        else:
            print("Error: La dirección solo puede contener letras, números, espacios, #, -, /, ., ,, () y acentos.")
    while True:
        correo_elect = input("Ingresa tu correo electronico: ")
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo_elect):
            if len(correo_elect) <= 100:
                print("El correo ha sido agregado")
                break
            else:
                print("El correo debe tener minimo 100 caracteres")
        else:
            print("El correo debe de tener los siguientes caracteres(ej. ejemplo@dominio.com)")
    datosPersonales = datosPersonalesDict(nombre, identificacion, fecha_nacimiento, celular_numero, direccion, correo_elect)
    usuarios[str(serial)]["datosPersonales"] = datosPersonales

    # Formación académica
    print("A continuacion se le pediran su información académica")
    while True:
        while True:
            universidad = input("Ingresa el nombre de la universidad: ")
            if universidad.replace(" ", "").isalpha():
                break
            else:
                print("Ingresa un nombre válido")
        while True:
            titulo = input("Ingresa el nombre del título: ")
            if titulo.replace(" ", "").isalpha():
                break
            else:
                print("Ingresa un nombre válido")
        while True:
            año = input("Ingresa el año de graduación: ")
            if año.isdigit():
                break
            else:
                print("Ingresa un año válido")
        formacion = formaciónDict(universidad, titulo, año)
        listaFormaciones.append(formacion)
        while True:
            reset = input("¿Quieres añadir más formación profesional? 1.Si/2.No: ")
            if reset.isdigit() == False:
                print("Ingresa una opción válida (1/2)")
            elif int(reset) != 1 and int(reset) != 2:
                print("Ingresa una opción válida (1/2)")
            else:
                break
        if int(reset) == 2:
            break
    usuarios[str(serial)]["formacionAcademica"] = listaFormaciones

    # Experiencias
    print("A continuacion se le pedirá su experiencia laboral")
    while True:
        experiencia = input("¿Tienes experiencia laboral? 1.Si/2.No: ")
        if experiencia in ["1", "2"]:
            break
        print("Ingresa una opción válida (1/2)")
    if experiencia == "1":
        while True:
            while True:
                empresa = input("Empresa donde trabajo: ")
                if empresa.replace(" ", "").isalpha():
                    break
                else:
                    print("Ingrese un nombre valido\n")
            while True:
                cargo = input("¿Que cargo ejercias?: ")
                if cargo.replace(" ", "").isalpha():
                    break
                else:
                    print("Ingrese un nombre valido\n")
            while True:
                duracion = input("¿Tiempo de duracion (cantidad en años)?: ")
                if duracion.isdigit():
                    break
                else:
                    print("Ingrese un nombre valido\n")
            informacion = {"Empresa": empresa, "Cargo": cargo, "Duración": duracion}
            experiencias.append(informacion)
            while True:
                salir = input("¿Quieres ingresar mas expreciencias laborales? 1.Si/2.No: ")
                if salir in ["1", "2"]:
                    break
                print("Ingresa una opción válida (1/2)")
            if salir == "2":
                break
    usuarios[str(serial)]["experienciaProfesional"] = experiencias

    # Referencias personales
    print("A continuacion se le pedirán sus referencias personales")
    while True:
        while True:
            nombreRef = input("Ingresa el nombre de tu referencia : ")
            if nombreRef.replace(" ", "").isalpha():
                break
            else:
                print("Ingresa un nombre válido")
        while True:
            relacion = input("Ingresa tu relación con esta persona: ")
            if relacion.replace(" ", "").isalpha():
                break
            else:
                print("Ingresa un dato válido")
        while True:
            telefonoRef = input("Ingresa el teléfono de tu referencia: ")
            if telefonoRef.isdigit() and len(telefonoRef) == 10:
                break
            else:
                print("Ingresa un teléfono válido")
        referencias = referenciasDict(nombreRef, relacion, telefonoRef)
        listaReferencias.append(referencias)
        while True:
            reset = input("¿Quieres añadir más referencias 1.Si/2.No: ")
            if reset.isdigit() == False:
                print("Ingresa una opción válida (1/2)")
            elif int(reset) != 1 and int(reset) != 2:
                print("Ingresa una opción válida (1/2)")
            else:
                break
        if int(reset) == 2:
            break
    usuarios[str(serial)]["referenciasPersonales"] = listaReferencias

    # Habilidades adicionales
    while True:
        habilidadesAdicionales = input("¿Tienes habilidades adicionales? 1.Si/2.No: ")
        if habilidadesAdicionales in ["1", "2"]:
            break
        print("Ingresa una opción válida (1/2)")
    if habilidadesAdicionales == "1":
        while True:
            while True:
                habilidad = input("Digite una habilidad: ")
                if  habilidad.isdigit():
                    print("Ingrese texto válido\n")
                else:
                    break
            habilidades.append(habilidad)
            while True:
                salir = input("¿Quieres ingresar otra habilidad? 1.Si/2.No: ")
                if salir in ["1", "2"]:
                    break
                print("Ingresa una opción válida (1/2)")
            if salir == "2":
                break
    usuarios[str(serial)]["habilidadesAdicionales"] = habilidades

    # Generar hoja de vida y JSON
    generar_hoja_de_vida(usuarios[str(serial)], f"{nombre}.txt")
    print("Hoja de vida generada:", f"{nombre}.txt")

# Actualizar usuario
def actualizar_usuario(usuario_id):
    if usuario_id not in usuarios:
        print("Error: ID de usuario no encontrado.")
        return

    while True:
        print("\nOpciones de actualización para el usuario", usuario_id)
        print("1. Añadir nueva experiencia o formación")
        print("2. Editar datos personales o de contacto")
        print("3. Agregar habilidades y referencias")
        print("4. Volver al menú principal")

        try:
            seleccione_act = int(input("Selecciona una opción (1-4): "))
        except ValueError:
            print("Error: Ingresa un número válido.")
            continue

        if seleccione_act == 1:
            tipo = input("¿Deseas añadir experiencia (1) o formación (2)? Ingresa 1 o 2: ")
            if tipo == "1":
                while True:
                    empresa = input("Ingresa el nombre de la empresa: ")
                    if empresa.replace(" ", "").isalpha():
                        break
                    print("Ingrese un nombre valido\n")
                while True:
                    cargo = input("Ingresa el cargo: ")
                    if cargo.replace(" ", "").isalpha():
                        break
                    print("Ingrese un nombre valido\n")
                while True:
                    duracion = input("Ingresa la duración (cantidad en años): ")
                    if duracion.isdigit():
                        break
                    print("Ingrese un número valido\n")
                informacion = {"Empresa": empresa, "Cargo": cargo, "Duración": duracion}
                usuarios[usuario_id]["experienciaProfesional"].append(informacion)
                print("Experiencia añadida.")
            elif tipo == "2":
                while True:
                    universidad = input("Ingresa el nombre de la universidad: ")
                    if universidad.replace(" ", "").isalpha():
                        break
                    print("Ingresa un nombre válido")
                while True:
                    titulo = input("Ingresa el nombre del título: ")
                    if titulo.replace(" ", "").isalpha():
                        break
                    print("Ingresa un nombre válido")
                while True:
                    año = input("Ingresa el año de graduación: ")
                    if año.isdigit():
                        break
                    print("Ingresa un año válido")
                formacion = formaciónDict(universidad, titulo, año)
                usuarios[usuario_id]["formacionAcademica"].append(formacion)
                print("Formación añadida.")
            else:
                print("Opción inválida.")

        elif seleccione_act == 2:
            print("\nDatos actuales:", usuarios[usuario_id]["datosPersonales"])
            tipo = input("¿Deseas cambiar dirección (1) o número (2)? Ingresa 1 o 2: ")
            if tipo == "1":
                while True:
                    direccion = input("Ingresa la nueva dirección: ")
                    if re.match(r'^[a-zA-Z0-9\sáéíóúñÁÉÍÓÚÑ#\-/.,()]+$', direccion):
                        if len(direccion) >= 5:
                            print("Dirección valida ")
                            usuarios[usuario_id]["datosPersonales"]["dirección"] = direccion
                            print("Dirección actualizada.")
                            break
                        else:
                            print("La dirección debe contener al menos 5 caracteres")
                    else:
                        print("Error: La dirección solo puede contener letras, números, espacios, #, -, /, ., ,, () y acentos.")
            elif tipo == "2":
                while True:
                    celular_numero = input("Ingresa el nuevo número de celular: ")
                    if celular_numero.isdigit() and len(celular_numero) == 10:
                        usuarios[usuario_id]["datosPersonales"]["contacto"] = celular_numero
                        print("Número actualizado.")
                        break
                    else:
                        print("El número de celular no es válido")
            else:
                print("Opción inválida.")

        elif seleccione_act == 3:
            tipo = input("¿Deseas añadir habilidad (1) o referencia (2)? Ingresa 1 o 2: ")
            if tipo == "1":
                while True:
                    habilidad = input("Ingresa una habilidad: ")
                    if habilidad.replace(" ", "").isalpha():
                        if habilidad not in usuarios[usuario_id]["habilidadesAdicionales"]:
                            usuarios[usuario_id]["habilidadesAdicionales"].append(habilidad)
                            print("Habilidad añadida.")
                            break
                        else:
                            print("Error: La habilidad ya existe.")
                    else:
                        print("Ingrese texto valido\n")
            elif tipo == "2":
                while True:
                    nombreRef = input("Ingresa el nombre de la referencia: ")
                    if nombreRef.replace(" ", "").isalpha():
                        break
                    print("Ingresa un nombre válido")
                while True:
                    relacion = input("Ingresa la relación con esta persona: ")
                    if relacion.replace(" ", "").isalpha():
                        break
                    print("Ingresa un dato válido")
                while True:
                    telefonoRef = input("Ingresa el teléfono de la referencia: ")
                    if telefonoRef.isdigit() and len(telefonoRef) == 10:
                        break
                    print("Ingresa un teléfono válido")
                referencias = referenciasDict(nombreRef, relacion, telefonoRef)
                usuarios[usuario_id]["referenciasPersonales"].append(referencias)
                print("Referencia añadida.")
            else:
                print("Opción inválida.")

        elif seleccione_act == 4:
            break

        else:
            print("Opción inválida.")

        # Actualizar hoja de vida y JSON
        generar_hoja_de_vida(usuarios[usuario_id], f"hoja_vida_{usuario_id}.txt")
        generarJsonCompleto(usuarios)

# Menú principal
def menu_principal():
    global usuarios
    while True:
        print("\n=== Sistema de Gestión de Hojas de Vida ===")
        print("1. Añadir nuevo usuario")
        print("2. Actualizar usuario existente")
        print("3. Filtrar hojas de vida")
        print("4. Exportar hojas de vida")
        print("5. Salir")
        print("=============================================")
        
        try:
            opcion = int(input("Selecciona una opción (1-4): "))
        except ValueError:
            print("Error: Ingresa un número válido.")
            continue
        
        if opcion == 1:
            añadir_usuario()
        
        elif opcion == 2:
            usuario_id = input("Ingresa el ID del usuario a actualizar (ej. 1): ")
            actualizar_usuario(usuario_id)
        
        elif opcion == 3:
            print("Opciones de filtrado:")
            print("1. Por años de experiencia")
            print("2. Por formación específica")
            print("3. Por habilidad específica")
            try:
                filtro_opcion = int(input("Selecciona una opción (1-3): "))
            except ValueError:
                print("Error: Ingresa un número válido.")
                continue
            
            if filtro_opcion == 1:
                try:
                    limite = int(input("Ingresa el número mínimo de años de experiencia: "))
                    filtro = filtrarHojasAños(usuarios, limite)
                    generarJsonAños(filtro)
                    print("Filtro aplicado. Revisa 'filtroAños.json'.")
                except ValueError:
                    print("Error: Ingresa un número válido.")
            
            elif filtro_opcion == 2:
                formacion = input("Ingresa el título de formación (ej. Profesional lenguas modernas): ")
                filtro = filtrarFormación(usuarios, formacion)
                generarJsonFormacion(filtro)
                print("Filtro aplicado. Revisa 'formación.json'.")
            
            elif filtro_opcion == 3:
                habilidad = input("Ingresa la habilidad (ej. Python): ")
                filtro = filtrarHabilidades(usuarios, habilidad)
                generarJsonHabilidades(filtro)
                print("Filtro aplicado. Revisa 'habilidades.json'.")
            
            else:
                print("Opción inválida.")
        
        elif opcion == 4:
            while True:
                tipoExportación=input("¿Qué desea exportar? 1.Hojas de vida con experiencia laboral por encima de un número dado / 2. Exportar candidatos con certificación o formación específica / 3. Exportar todas las hojas de vida: ")
                if tipoExportación.isdigit() and int(tipoExportación) in [1, 2, 3]:
                    if tipoExportación == "1":
                        limite = input("Ingrese el número mínimo de años de experiencia: ")
                        if limite.isdigit():
                            filtrados = filtrarHojasAños(usuarios, int(limite))
                            if len(filtrados) == 0:
                                print("No se encontraron hojas de vida con esa cantidad de experiencia.")
                            else:
                                generarJsonAños(filtrados)
                                print(f"Exportadas hojas de vida con al menos {limite} años de experiencia.")
                        else:
                            print("Por favor ingrese un número válido.")
                    elif tipoExportación == "2":
                        while True:
                            try:
                                select=int(input("Desea filtrar por:  1. Título profesional o por 2. Habilidades específicas: "))
                                if select in [1, 2]:
                                    break
                                else:
                                    print("Ingrese un valor válido (1/2)")
                            except ValueError:
                                print("Ingrese un valor válido (1/2)")
                        if select==1:
                            formacion = input("Ingrese el título o certificación a buscar: ")
                            filtrados = filtrarFormación(usuarios, formacion)
                            if len(filtrados) == 0:
                                print("No se encontraron hojas de vida con esa formación.")
                            else:
                                generarJsonFormacion(filtrados)
                                print(f"Exportadas hojas de vida con formación: {formacion}")
                        elif select==2:
                            habs=input("Ingrese la habilidad específica a buscar: ")
                            filtroHabs= filtrarHabilidades(usuarios, habs)
                            if len(filtroHabs) == 0:
                                print("No se encontraron hojas de vida con esa habilidad.")
                            else:
                                generarJsonHabilidades(filtroHabs)
                                print(f"Exportadas hojas de vida con habilidades: {habs}")
                    elif tipoExportación == "3":
                        generarJsonCompleto(usuarios)
                        print("Exportadas todas las hojas de vida.")
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
        elif opcion == 5:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")


# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()