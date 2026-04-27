class PuestoTrabajo:
    def __init__(self, codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo):
        self.codigo = codigo
        self.descripcion = descripcion
        self.areaSolicitante = areaSolicitante
        self.plazasRequeridas = plazasRequeridas
        self.sueldo = sueldo

    def mostrar(self):
        print("Codigo:", self.codigo)
        print("Descripcion:", self.descripcion)
        print("Area solicitante:", self.areaSolicitante)
        print("Plazas requeridas:", self.plazasRequeridas)
        print("Sueldo:", self.sueldo)
        print("Total requerido:", self.plazasRequeridas * self.sueldo)
        print("--------------------------------")


def validarTexto(mensaje):
    texto = input(mensaje)
    while len(texto) < 3:
        print("El texto debe tener por lo menos 3 letras.")
        texto = input(mensaje)
    return texto


def validarEntero(mensaje):
    numero = int(input(mensaje))
    while numero <= 0:
        print("El numero debe ser mayor a cero.")
        numero = int(input(mensaje))
    return numero


def validarFloat(mensaje):
    numero = float(input(mensaje))
    while numero <= 0:
        print("El numero debe ser mayor a cero.")
        numero = float(input(mensaje))
    return numero


def existeRepetido(lista, codigo, descripcion, areaSolicitante):
    for puesto in lista:
        if puesto.codigo == codigo or puesto.descripcion == descripcion or puesto.areaSolicitante == areaSolicitante:
            return True
    return False


def AgregaPuesto(lista):
    print("\nAgregar puesto de trabajo")

    codigo = validarEntero("Ingrese codigo: ")
    descripcion = validarTexto("Ingrese descripcion: ")
    areaSolicitante = validarTexto("Ingrese area solicitante: ")
    plazasRequeridas = validarEntero("Ingrese plazas requeridas: ")
    sueldo = validarFloat("Ingrese sueldo: ")

    if existeRepetido(lista, codigo, descripcion, areaSolicitante):
        print("No se puede agregar. Ya existe un puesto con el mismo codigo, descripcion o area solicitante.")
    else:
        nuevo = PuestoTrabajo(codigo, descripcion, areaSolicitante, plazasRequeridas, sueldo)
        lista.append(nuevo)
        print("Puesto agregado correctamente.")


def MostrarTodo(lista):
    print("\nLista de puestos de trabajo")

    if len(lista) == 0:
        print("No hay puestos registrados.")
    else:
        for puesto in lista:
            puesto.mostrar()


def ordenarBurbujaCodigo(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j].codigo > lista[j + 1].codigo:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux


def BorraPuesto(lista):
    print("\nBorrar puesto de trabajo")

    if len(lista) == 0:
        print("No hay puestos para borrar.")
    else:
        ordenarBurbujaCodigo(lista)

        codigoBuscar = int(input("Ingrese el codigo a borrar: "))
        encontrado = False

        i = 0
        while i < len(lista):
            if lista[i].codigo == codigoBuscar:
                encontrado = True
                print("Se elimino el siguiente puesto:")
                lista[i].mostrar()
                lista.pop(i)
            else:
                i = i + 1

        if encontrado == False:
            print("No se encontro ningun puesto con ese codigo.")


def ordenarInsercionSueldo(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1

        while j >= 0 and lista[j].sueldo < actual.sueldo:
            lista[j + 1] = lista[j]
            j = j - 1

        lista[j + 1] = actual


def busquedaBinariaSueldo(lista, sueldoBuscar):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio].sueldo == sueldoBuscar:
            return medio
        elif sueldoBuscar > lista[medio].sueldo:
            fin = medio - 1
        else:
            inicio = medio + 1

    return -1


def BuscaSueldo(lista):
    print("\nBuscar puesto por sueldo")

    if len(lista) == 0:
        print("No hay puestos registrados.")
    else:
        ordenarInsercionSueldo(lista)

        sueldoBuscar = float(input("Ingrese el sueldo a buscar: "))
        posicion = busquedaBinariaSueldo(lista, sueldoBuscar)

        if posicion == -1:
            print("No se encontraron puestos con ese sueldo.")
        else:
            print("Puestos encontrados con sueldo", sueldoBuscar)

            izquierda = posicion
            while izquierda - 1 >= 0 and lista[izquierda - 1].sueldo == sueldoBuscar:
                izquierda = izquierda - 1

            derecha = posicion
            while derecha + 1 < len(lista) and lista[derecha + 1].sueldo == sueldoBuscar:
                derecha = derecha + 1

            for i in range(izquierda, derecha + 1):
                lista[i].mostrar()


def totalRequerido(puesto):
    return puesto.plazasRequeridas * puesto.sueldo


def ordenarSeleccionTotal(lista):
    n = len(lista)

    for i in range(n - 1):
        mayor = i

        for j in range(i + 1, n):
            if totalRequerido(lista[j]) > totalRequerido(lista[mayor]):
                mayor = j

        aux = lista[i]
        lista[i] = lista[mayor]
        lista[mayor] = aux


def PuestosAContratar(lista):
    print("\nPuestos a contratar")

    if len(lista) == 0:
        print("No hay puestos registrados.")
    else:
        monto = validarFloat("Ingrese el monto total a invertir en salarios: ")

        ordenarSeleccionTotal(lista)

        acumulado = 0
        encontrados = False

        print("\nPuestos que se pueden cubrir:")

        for puesto in lista:
            total = totalRequerido(puesto)

            if acumulado + total <= monto:
                puesto.mostrar()
                acumulado = acumulado + total
                encontrados = True

        if encontrados == False:
            print("No se puede cubrir ningun puesto con ese monto.")
        else:
            print("Monto total utilizado:", acumulado)
            print("Monto restante:", monto - acumulado)


def menu():
    puestos = []
    opcion = 0

    while opcion != 6:
        print("\nMENU")
        print("1 - AgregaPuesto")
        print("2 - MostrarTodo")
        print("3 - BorraPuesto")
        print("4 - BuscaSueldo")
        print("5 - PuestosAContratar")
        print("6 - Salir")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            AgregaPuesto(puestos)
        elif opcion == 2:
            MostrarTodo(puestos)
        elif opcion == 3:
            BorraPuesto(puestos)
        elif opcion == 4:
            BuscaSueldo(puestos)
        elif opcion == 5:
            PuestosAContratar(puestos)
        elif opcion == 6:
            print("Programa terminado.")
        else:
            print("Opcion incorrecta.")


menu()
