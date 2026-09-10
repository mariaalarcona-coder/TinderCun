def registrarPersonas():
    individuo={}
    nombre=input("Ingresa tu nombre: ")
    individuo["Nombre"]=nombre
    #Validar edad
    edad=int(input("Ingresa tu edad: "))
    edadValida=False
    while edadValida!=True:
        if(edad<18):
            print("No aceptamos menores de edad")
            edad=int(input("Ingresa tu edad: "))
        elif (edad>=18):
            edadValida=True       
            individuo["Edad"]=edad
    ciudad=input("Ingresa tu ciudad: ")
    individuo["Ciudad"]=ciudad
    generos=["Masculino","Femenino","No binario"]
    generoValido=False
    while generoValido!=True:
        print(generos)
        genero=input("Ingresa tu género: ")
        if genero in generos:
            generoValido=True
    generoInteres=input("Ingresa el género de interés: ")
    individuo["Genero Interesado"]=generoInteres
    edadMinima=int(input("Ingresa la edad mínima: "))
    individuo["Edad Minima"]=edadMinima
    edadMaxima=int(input("Ingresa la edad máxima: "))
    individuo["Edad Máxima"]=edadMaxima
    intereses=input("Ingresa tus interese(Hoobies): ")
    individuo["Hooby"]=intereses.split()
    distanciaMaxima=int(input("Ingresa una distancia máxima: "))
    individuo["Distancia Máxima"]=distanciaMaxima
    print(individuo)
    return individuo

def mostrarPersonas(personas):
    print(personas)

def buscarCoincidenciasBy Persona(personas, individuoABuscar):
    

def main():
    opciones="1. Regitrar Persona \n2. Mostrar las personas \n3. Buscar coincidencias   \n9. Salir"
    print(opciones)
    opcion=int(input("Digite la opción que necesitas: "))
    while opcion!=9:
        if opcion==1:
            registrarPersonas()
        
            cuantasPersonas=int(input("Ingresa cuantas personas vas a registrar"))
            #Registrando Personas
            personas={}
            for i in range (0,cuantasPersonas):
                print("i",i)
                print(personas)
                personas[i]= registrarPersonas()
        elif opcion==2:
            #Mostrar Personas
            mostrarPersonas(personas)
        elif opcion==3:
            #Buscar Coincidencias
            buscarCoincidencias(personas)
        elif opcion==9:
            print("Gracias")
            break
        print(opciones)
        opcion=int(input("Digite la opcion que necesita"))
        
main()
