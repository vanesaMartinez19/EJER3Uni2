from ClaseRegistro import Registro
def DefinirLista(archi, Reader):
    Dia = 30
    Horas = 24
    Lista = []
    Band = True
    for i in range(Dia):
        Lista.append([0]*Horas)
    for fila in Reader:
        if Band==True:
            Band=False
        else:
            Dia=int(fila[0])
            Horas=int(fila[1])
            Temperatura=float(fila[2])
            Humedad=int(fila[3])
            Presion=int(fila[4])
            NuevoRegistro=Registro(Temperatura,Humedad,Presion)
            Lista[Dia-1][Horas-1]=NuevoRegistro
    for i in range(Dia):
        for j in range(Horas):
            Lista[i][j].MostrarDatos()


