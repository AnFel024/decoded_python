import math

from numbers_to_letter import number_to_letter

def decode_text(encoded_string, input_base):
    base= int(input_base)
    string_list = list(encoded_string)

    base_2= int(math.log(base, 2))
    
    #Se genera un diccionario para almacenar los valores de los caracteres en sus distintas bases.   
    base_32={}
    for i in range(0,base):
        key= str(bin(i))[2:]
        if len(key) < base_2:
            zeros= ''
            for j in range(0, base_2-len(key)):
                zeros+= '0'
            key= zeros + key
        base_32[key]= number_to_letter(i)
    
    inverted_dict = dict((y,x) for x,y in base_32.items())

    bin_response= ""

    for word in string_list:
        bin_response+= inverted_dict[word]
        print(inverted_dict[word])

    #Agrupa los resultados en un array del tamaño del exponente de la base.
    cont=0
    convert_list= []
    str_append= ''
    for i in range(0,len(bin_response)):
        cont+=1
        str_append+= bin_response[i]
        if (cont==8):
            convert_list.append(str_append)
            cont=0
            str_append= ''

    if str_append != '':
        zeros= ''
        for j in range(0, 8-len(str_append)):
            zeros+= '0'
        str_append+= zeros
        convert_list.append(str_append)
    
    response= ""
    for binary_item in convert_list:
        response+= chr(int(binary_item, 2))

    #Se muestran los resultados.
    print('*'*20)
    print("Texto: ", encoded_string)
    print('*'*20)
    print('Decodificado en base: ', base)
    print('*'*20)
    print("Texto decifrado: ", response)
    print('*'*20)