print("Jan Adrian Sosa Cordero matri: 1317 ")

class empleados1317:
    id_empleados1317=" "
    nom_empleados1317=" "
    curp1317=" "
    telefono1317= " "
    Direccion1317=" "
    Edad1317=" "
    Sexo1317=" "
    
    def mostrar_datos(self):
        print(f"id empleados: {self.id_empleados1317}" )
        print(f"Nombre empleados: {self.nom_empleados1317}" )
        print(f"Curp: {self.curp1317}" )
        print(f"Telefono: {self.telefono1317}" )
        print(f"Direccion: {self.Direccion1317}" )
        print(f"Edad: {self.Edad1317}" )
        print(f"Sexo: {self.Sexo1317}" )

    def lista_idempleados(self):
        id_empleados1317 =["credencial", "ine ","licencia de manejo","ine","ine","ine","ine"]
        print(id_empleados1317)
        for lista in id_empleados1317:
            print(lista)

    def tupla_nombreempleados(self):
        nom_empleados1317 =("jorge","ali","luis","ignacio","raul","beto","pancho")
        print(nom_empleados1317)
        for Tupla in nom_empleados1317:
            print(Tupla)

    def diccionario_curp(self):
        curp1317 = {
        "jorge":"USDIO34IO",
        "ali": "HGUGY67567",
        "luis": "IJSAOIDJ32",
        "ignacio": "DDF23",
        "raul": "FDSFDS3432",
        "beto": "FF3432",
        "pancho": "KJJHUH67564"
    }
        print(curp1317["jorge"])
        for dic in curp1317:
            print(dic)

    def altas1317(self):
        print("La operacion de alta se realizo correctamente para datos del empleado")
    def bajas1317(self):
        print("La operacion de bajas se realizo correctamente para datos del empleado")

empleado = empleados1317()


empleado.id_empleados1317=" INE"
empleado.nom_empleados1317=" ADRIAN"
empleado.curp1317=" IUHDS343 "
empleado.telefono1317= " 656 812 1227"
empleado.Direccion1317=" SAIN JAQUES 2113 "
empleado.Edad1317="23 "
empleado.Sexo1317=" MASCULINO "

empleado.mostrar_datos()

print("\nLista de id empleados")
print(empleado.id_empleados1317)

print("\nTupla Nombre empleados")
print(empleado.nom_empleados1317)

print("\nDiccionario Curp")
print(empleado.curp1317)

empleado.altas1317()
empleado.bajas1317()