
import json

from numbers_to_letter import number_to_letter
from convert_to_bin import convert_to_list

from datetime import datetime

def encode_text(a_string, input_base, is_image=False, return_16=False):
    base= int(input_base)
    if is_image and not return_16:
        with open("img.png", "rb") as image:
            image = image.read()
            a_byte_array = bytearray(image)
            #print(a_byte_array)
    else:
        a_byte_array = bytearray(a_string, "latin1")
    
    if not return_16:
        byte_list = ''
        #Obtiene los valores binarios despues de convertir la cadena de texto a una representacion en python.
        for byte in a_byte_array:
            #print(byte)
            binary_representation = str(bin(byte))[2:]
            if len(binary_representation) < 8:
                zeros= ''
                for j in range(0, 8-len(binary_representation)):
                    zeros+= '0'
                binary_representation= zeros + binary_representation
            byte_list+=binary_representation
    else:
        byte_list= a_string
    
    convert_list= convert_to_list(byte_list, base, is_image)
    
    if not return_16:
        print('*'*20)
        print('Binario Agrupados')    
        print(convert_list)
        #Se genera un diccionario para almacenar los valores de los caracteres en sus distintas bases.   
        print('*'*20)
        print('Dicionario:')
    
    base_32={}
    for i in range(0,int(base)):
        key=str(bin(i)).replace('0b','')
        print((str(i)+" : "+number_to_letter(i)) if not return_16 else '')
        base_32[key]= number_to_letter(i)
    
    if not return_16:
        print('*'*20)
        print('Dicionario agrupado:')
        print(base_32)
        print('*'*20)

    #Se enlaza la clave binaria con el valor correspondiente para obtener el mensaje.
    str_res= ''
    for i in convert_list:
            str_res+= base_32[str(int(i))]

    #if is_image and not return_16:
    #Se muestran los resultados.
    print('*'*20)
    print(f"{'Imagen' if is_image else 'Texto'} ", a_string)
    print('*'*20)
    print('Codificado en base: ', base)
    print('*'*20)
    print(f"{'Imagen' if is_image else 'Texto'} codificado: ", str_res)
    print('*'*20)

    with open("./response.txt", "w") as myfile: 
        myfile.seek(0)
        myfile.write(str(datetime.now())+': '+str_res)
        myfile.truncate()

    return str_res
