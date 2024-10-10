traduccion={
    "JUICIOSO":"persona responsable o que cumple con sus deberes",
    "CANGUIL":"maiz pira o palomita de maiz",
    "AGUACATE":"es una fruta también conocida como palta"
}

palabra=input("Ingresa una palabra en mayusculas, que quieras traducir:")

if palabra in traduccion.keys():
    print("su significado es:",traduccion[palabra])
else:
    print("la palabra no existe")
