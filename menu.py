from encoder_text import encode_text
from decoder_text import decode_text

correct_base= False
while not correct_base:
    base= int(input('Ingrese una base para la codificación (16/32) '))
    if (base== 16) or (base==32):
        correct_base= True

ans=True
while ans:
    print (f"""
    Gracias por utilizar el programa. 

    * MENU DE OPCIONES: *
    1. Codificar texto
    2. Decodificar texto
    3. Cambiar base (actual: {base})
    4. Salir
    """)
    ans= input("¿Que le gustaria hacer?\n--> ") 
    if ans=="1": 
        print(f"\n Codificando texto: Ingrese el texto a codificar en base {base}:\n")
        encode_text(input('--> '), base)
    elif ans=="2":
        print(f"\n Decodificando texto: Ingrese el texto a decodificar en base {base}:\n")
        decode_text(input('--> '), base)
    elif ans=="3":
        base= input('Nueva base--> ')
    elif ans=="4":
        print("\n Hasta luego. Happy codding!") 
        ans= False
    elif ans !="":
        print("\n Verifique su entrada") 