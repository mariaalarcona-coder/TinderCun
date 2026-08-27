def registrarPersonas():
    individuo={}
    nombre=input("Ingresa tu nombre: ")
    individuo["Nombre"]=nombre
    edad=int(input("Ingresa tu edad: "))
    individuo["Edad"]=edad
    ciudad=input("Ingresa tu ciudad: ")
    individuo["Ciudad"]=ciudad
    genero=input("Ingresa tu género: ")
    individuo["Genero"]=genero
    generoInteres=input("Ingresa el género de interés: ")
    individuo["Genero Interesado"]=generoInteres
    edadMinima=int(input("Ingresa la edad mínima: "))
    individuo["Edad Minima"]=edadMinima
    edadMaxima=int(input("Ingresa la edad máxima: "))
    individuo["Edad Máxima"]=edadMaxima
    intereses=input("Ingresa tus interese(Hoobies): ")
    individuo["Hooby"]=intereses
    distanciaMaxima=int(input("Ingresa una distancia máxima: "))
    individuo["Distancia Máxima"]=distanciaMaxima
    print(individuo)
    return individuo

def mostrarPersonas(personas):
    print(personas)

def main():
    cuantasPersonas=int(input("Ingresa cuantas personas vas a registrar"))
    #Registrando Personas
    personas={}
    for i in range (0,cuantasPersonas):
        print("i",i)
        print(personas)
        personas[i]= registrarPersonas()
    #Mostrar Personas
    mostrarPersonas(personas)

    print()

main()
