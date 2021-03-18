print("*********¿Que desea realizar?******")
detener1 = True
menu = input("Para calcular promedios de alumnos por programa ingrese(1), para proceso de admision ingrese(2):")
while detener1:
    if menu == "1" or menu == "2":
        menu = int(menu)
        detener1 = False 
    else:
         print("El valor ingresado debe ser 1 o 2")
         menu = input("Para calcular promedios de almunos por programa ingrese(1), para proceso de admision ingrese(2):")


pacademicor = []

nomalumnos = []
pacademicoa = []
promedio = []
notas = []
sexo = []
sumn = 0

#PROMEDIO GENERAL
pgpa1 = 0
pgpa2 = 0
pgpa3 = 0
pgpa4 = 0
pgpa5 = 0

#CONTADOR PERSONAS
cnhpa1 = 0 
cnmpa1 = 0 
cnhpa2 = 0
cnmpa2 = 0
cnhpa3 = 0
cnmpa3 = 0
cnhpa4 = 0
cnmpa4 = 0
cnhpa5 = 0
cnmpa5 = 0

#VALIDAR NUMERO ESTUDIANTES POR PROGRAMA
vnep1 = 0
vnep2 = 0
vnep3 = 0
vnep4 = 0
vnep5 = 0

def vnestudiantes(nh,nm):
    return nh + nm


if menu == 1:
    detener2 =True
    npacademiscos = input("Ingrese el # de programas academicos a registrar:")
    while detener2:
        if npacademiscos == "1" or npacademiscos == "2" or npacademiscos == "3" or npacademiscos == "4" or npacademiscos == "5":
            npacademiscos = int(npacademiscos)
            detener2 = False
        else:
            print("Debes ingresar minimo un programa academico y maximo 5")
            npacademiscos = input("Ingrese el # de programas academicos a registrar:")    
         
    
    for i in range(npacademiscos):
        pacademicor.append(input(f"Ingrese nombre del programa academico # {i+1}:"))
        
    
    nalumnos = input("Ingrese el # de alumnos:")
    while not nalumnos.isdigit():
        print("El valor debe ser entero:")
        nalumnos = input("Ingrese el # de alumnos:")
       
    nalumnos = int(nalumnos)
        
    
    for i in range(nalumnos):
        nomalumnos.append(input(f"Ingrese nombre del alumno {i+1}:"))
        sexo.append(input("Ingrese sexo del alumno Homebre(H) Mujer(M):"))
        print("PROGRAMAS ACADEMICOS")
        print(f"A cual programa academico pertenece el alumno?:")
        for i in range(len(pacademicor)):
            print(f"{pacademicor[i]}")
        pacademicoa.append(input("Ingrese programa academico del alumno:"))           
        for i in range(1,6):
            notas.append(float(input(f"Ingrese nota {i}:")))
        for i in range(len(notas)):
            sumn += notas[i]
        promedio.append(sumn/5)
        notas.clear()
        sumn = 0


    for i in range(len(sexo)):
        if sexo[i] == "H" and pacademicoa[i] == pacademicor[0]:
            cnhpa1 +=1
        elif sexo[i] == "M" and pacademicoa[i] == pacademicor[0]:
            cnmpa1 +=1
        elif sexo[i] == "H" and pacademicoa[i] == pacademicor[1]:
            cnhpa2 +=1
        elif sexo[i] == "M" and pacademicoa[i] == pacademicor[1]:
            cnmpa2 +=1
        elif sexo[i] == "H" and pacademicoa[i] == pacademicor[2]:
            cnhpa3 +=1
        elif sexo[i] == "M" and pacademicoa[i] == pacademicor[2]:
            cnmpa3 +=1
        elif sexo[i] == "H" and pacademicoa[i] == pacademicor[3]:
            cnhpa4 +=1    
        elif sexo[i] == "M" and pacademicoa[i] == pacademicor[3]:
            cnmpa4 +=1 
        elif sexo[i] == "H" and pacademicoa[i] == pacademicor[4]:
            cnhpa5 +=1        
        elif sexo[i] == "M" and pacademicoa[i] == pacademicor[4]:
            cnmpa5 +=1
    print()
    print()
    if len(pacademicor) == 1:
        print(f"LISTA ALUMNOS DE {pacademicor[0]}")
        print(f"#HOMBRES: {cnhpa1}----#MUJERES: {cnmpa1}")
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[0]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[0]:
                pgpa1 += promedio[i]
        vnep1 = vnestudiantes(cnhpa1,cnmpa1)
        if vnep1 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa1/(cnhpa1 + cnmpa1)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")            
                                       
    elif len(pacademicor) == 2:
        print(f"LISTA ALUMNOS DE {pacademicor[0]}")
        print(f"#HOMBRES: {cnhpa1}----#MUJERES: {cnmpa1}")
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[0]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[0]:
                pgpa1 += promedio[i]
        vnep1 = vnestudiantes(cnhpa1,cnmpa1)        
        if vnep1 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa1/(cnhpa1 + cnmpa1)}")         
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}") 
            
        print(f"LISTA ALUMNOS DE {pacademicor[1]}")
        print(f"#HOMBRES: {cnhpa2}----#MUJERES: {cnmpa2}")        
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[1]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[1]:
                pgpa2 += promedio[i]
        vnep2 = vnestudiantes(cnhpa2,cnmpa2)        
        if vnep2 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa2/(cnhpa2 + cnmpa2)}")  
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}") 
        
    elif len(pacademicor) == 3:
        print(f"LISTA ALUMNOS DE {pacademicor[0]}")
        print(f"#HOMBRES: {cnhpa1}----#MUJERES: {cnmpa1}")
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[0]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[0]:
                pgpa1 += promedio[i]
        vnep1 = vnestudiantes(cnhpa1,cnmpa1)        
        if vnep1 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa1/(cnhpa1 + cnmpa1)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")            
                
        print(f"LISTA ALUMNOS DE {pacademicor[1]}")
        print(f"#HOMBRES: {cnhpa2}----#MUJERES: {cnmpa2}")        
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[1]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[1]:
                pgpa2 += promedio[i]
        vnep2 = vnestudiantes(cnhpa2,cnmpa2)        
        if vnep2 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa2/(cnhpa2 + cnmpa2)}") 
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")             
                
        print(f"LISTA ALUMNOS DE {pacademicor[2]}")
        print(f"#HOMBRES: {cnhpa3}----#MUJERES: {cnmpa3}")        
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[2]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[2]:
                pgpa3 += promedio[i]
        vnep3 = vnestudiantes(cnhpa3,cnmpa3)        
        if vnep3 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa3/(cnhpa3 + cnmpa3)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")            
                
    elif len(pacademicor) == 4:
        print(f"LISTA ALUMNOS DE {pacademicor[0]}")
        print(f"#HOMBRES: {cnhpa1}----#MUJERES: {cnmpa1}")
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[0]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[0]:
                pgpa1 += promedio[i]
        vnep1 = vnestudiantes(cnhpa1,cnmpa1)        
        if vnep1 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa1/(cnhpa1 + cnmpa1)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")            
                
        print(f"LISTA ALUMNOS DE {pacademicor[1]}")
        print(f"#HOMBRES: {cnhpa2}----#MUJERES: {cnmpa2}")        
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[1]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[1]:
                pgpa2 += promedio[i]
        vnep2 = vnestudiantes(cnhpa2,cnmpa2)        
        if vnep2 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa2/(cnhpa2 + cnmpa2)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")            
                
        print(f"LISTA ALUMNOS DE {pacademicor[2]}") 
        print(f"#HOMBRES: {cnhpa3}----#MUJERES: {cnmpa3}")       
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[2]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[2]:
                pgpa3 += promedio[i]
        vnep3 = vnestudiantes(cnhpa3,cnmpa3)        
        if vnep3 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa3/(cnhpa3 + cnmpa3)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")            
                
        print(f"LISTA ALUMNOS DE {pacademicor[3]}") 
        print(f"#HOMBRES: {cnhpa4}----#MUJERES: {cnmpa4}")       
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[3]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[3]:
                pgpa4 += promedio[i]
        vnep4 = vnestudiantes(cnhpa4,cnmpa4)        
        if vnep4 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa4/(cnhpa4 + cnmpa4)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")            
                
    elif len(pacademicor) == 5:
        print(f"LISTA ALUMNOS DE {pacademicor[0]}")
        print(f"#HOMBRES: {cnhpa1}----#MUJERES: {cnmpa1}")
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[0]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[0]:
                pgpa1 += promedio[i]
        vnep1 = vnestudiantes(cnhpa1,cnmpa1)        
        if vnep1 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa1/(cnhpa1 + cnmpa1)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")           
                
        print(f"LISTA ALUMNOS DE {pacademicor[1]}")
        print(f"#HOMBRES: {cnhpa2}----#MUJERES: {cnmpa2}")        
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[1]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[1]:
                pgpa2 += promedio[i]
        vnep2 = vnestudiantes(cnhpa2,cnmpa2)        
        if vnep2 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa2/(cnhpa2 + cnmpa2)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")            
                
        print(f"LISTA ALUMNOS DE {pacademicor[2]}")
        print(f"#HOMBRES: {cnhpa3}----#MUJERES: {cnmpa3}")        
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[2]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[2]:
                pgpa3 += promedio[i]
        vnep3 = vnestudiantes(cnhpa3,cnmpa3)        
        if vnep3 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa3/(cnhpa3 + cnmpa3)}") 
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")             
                
        print(f"LISTA ALUMNOS DE {pacademicor[3]}")
        print(f"#HOMBRES: {cnhpa4}----#MUJERES: {cnmpa4}")        
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[3]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[3]:
                pgpa4 += promedio[i]
        vnep4 = vnestudiantes(cnhpa4,cnmpa4)        
        if vnep4 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa4/(cnhpa4 + cnmpa4)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")            
                
        print(f"LISTA ALUMNOS DE {pacademicor[4]}")
        print(f"#HOMBRES: {cnhpa5}----#MUJERES: {cnmpa5}")        
        for i in range(nalumnos):
            if pacademicoa[i] == pacademicor[4]:
                print(f"Programa: {pacademicoa[i]}----Nombre: {nomalumnos[i]}----Promedio: {promedio[i]}")
        for i in range(len(promedio)):
            if pacademicoa[i] == pacademicor[4]:
                pgpa5 += promedio[i]
        vnep5 = vnestudiantes(cnhpa5,cnmpa5)        
        if vnep5 > 0:
            print(f"PROMEDIO DEL PROGRAMA: {pgpa5/(cnhpa5 + cnmpa5)}")
        else:
            print(f"PROMEDIO DEL PROGRAMA: {0}")

elif menu == 2:
    nestudiantesm = 0  
    edadem = []   
    sexoem = ""
    sumeem = 0
    promeem = 0
    cnmm = 0
    cnhm = 0 
    while True:
        nestudiantesm +=1
        edadem.append(int(input("Ingrese la edad del estudiante:")))
        detenerea = True
        sexoae = input("Ingrese sexo del estudiante Hombre(H) Mujer(M):")
        while detenerea:
            if sexoae == "H":
                cnhm += 1
                detenerea = False
            elif sexoae == "M":
                cnmm += 1
                detenerea = False
            else:
                 sexoae = input("Ingrese sexo del estudiante Hombre(H) Mujer(M):")

        
        exit = int(input("Ingrese (1) para continuar con el proceso, Ingrese (2) para detenerlo:"))
        if exit == 2:
            break

    for i in range(len(edadem)):
        sumeem += edadem[i]
    promeem = sumeem / nestudiantesm
            
    print()
    print()         
    print("*******Resultados Proceso de admision*******")
    print(f"Total estudiantes matriculados:{cnmm + cnhm}")    
    print(f"Promedio edad estudiantes matriculados: {promeem}")
    print(f"#Mujeres matriculadas: {cnmm}---#Hombres matriculados: {cnhm}")

    
        
        
     
   


