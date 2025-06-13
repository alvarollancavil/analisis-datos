datos={"nombre":"","edad":"","direccion":"","telefono":""}

datos["nombre"]=input("¿Nombre?: ")
datos["edad"]=input("edad?: ")
datos["direccion"]=input("direccion?: ")
datos["telefono"]=input("telefono?: ")

print(f"%s tiene %s años, vive en %s y su numero de telefono es %s"
      %(datos["nombre"],datos["edad"],datos["direccion"],datos["telefono"]))