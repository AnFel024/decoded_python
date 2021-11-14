from encoder_text import encode_text


base= int(input('Ingrese la base con la que trabajara (16/32)'))

ans=True
while ans:
    print ("""
    Gracias por utilizar el programa. 

    * MENU DE OPCIONES: *
    1. Codificar texto
    2. Decodificar texto
    3. Salir
    """)
    ans= input("¿Que le gustaria hacer?\n--> ") 
    if ans=="1": 
        print(f"\n Codificando texto: Ingrese el texto a codificar en base {base}:\n")
        encode_text(input('-->'), base)
    elif ans=="2":
        print(f"\n Decodificando texto: Ingrese el texto a decodificar en base {base}:\n")
        encode_text(input('-->'))
    elif ans=="3":
        print("\n Hasta luego. Happy codding!") 
        ans= False
    elif ans !="":
        print("\n Verifique su entrada") 