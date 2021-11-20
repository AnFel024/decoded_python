import math

import os
import json
import PIL.Image as Image

from numbers_to_letter import number_to_letter

def encode_text(a_string, base, is_image):
    if is_image:
        with open("img.png", "rb") as image:
            image = image.read()
            a_byte_array = bytearray(image)
            #print(a_byte_array)
    else:
        a_byte_array = bytearray(a_string, "utf8")
    byte_list = ''
    #Obtiene los valores binarios despues de convertir la cadena de texto a una representacion en python.
    for byte in a_byte_array:
        binary_representation = str(bin(byte))[2:]
        if len(binary_representation) < 8:
            zeros= ''
            for j in range(0, 8-len(binary_representation)):
                zeros+= '0'
            binary_representation= zeros + binary_representation
        byte_list+=binary_representation
    
    print(binary_representation)
    print('*'*20)


    #Agrupa los resultados en un array del tamaño del exponente de la base.
    cont=0
    convert_list= []
    str_append= ''
    for i in range(0,len(byte_list)):
        cont+=1
        str_append+= byte_list[i]
        if (cont==math.log(int(base), 2)):
            convert_list.append(str_append)
            cont=0
            str_append= ''

    if str_append != '':
        convert_list.append(str_append)

    print(convert_list)

    #Se genera un diccionario para almacenar los valores de los caracteres en sus distintas bases.   
    base_32={}
    for i in range(0,int(base)):
        key=str(bin(i)).replace('0b','')
        base_32[key]= number_to_letter(i)
    
    print(base_32)
    print('*'*20)

    #Se enlaza la clave binaria con el valor correspondiente para obtener el mensaje.
    str_res= ''
    for i in convert_list:
            str_res+= base_32[str(int(i))]

    #Se muestran los resultados.
    print('*'*20)
    print(f"{'Imagen' if is_image else 'Texto'} ", a_string)
    print('*'*20)
    print('Codificado en base: ', base)
    print('*'*20)
    print(f"{'Imagen' if is_image else 'Texto'} codificado: ", str_res)
    print('*'*20)

    with open("./response.txt", "w") as outfile: 
        json.dump(str_res, outfile)

    return str_res
