import math

from numbers_to_letter import number_to_letter



def convert_bin_to_list(encoded_string, base, is_image, return_16):
    string_list = list(encoded_string)

    base_2= int(math.log(base, 2))
    
    #Se genera un diccionario para almacenar los valores de los caracteres en sus distintas bases.   
    if not return_16:
        print('*'*20)
        print('Diccionario')
    base_32={}
    for i in range(0,base):
        key= str(bin(i))[2:]
        if len(key) < base_2:
            zeros= ''
            for j in range(0, base_2-len(key)):
                zeros+= '0'
            key= zeros + key
        if not return_16:
            print(str(i)+" : " + number_to_letter(i))
        
        base_32[key]= number_to_letter(i)
    
    inverted_dict = dict((y,x) for x,y in base_32.items())
    #print(inverted_dict)
    bin_response= ""
    if not return_16:
        print('*'*20)
        #print(string_list)
        print('*'*20)
        print('Grupo de binario')
    anterior=0
    for i in range(0, len(string_list)):
        
        if(string_list[i] == '}' or string_list[i] == '~'):
            anterior=1
        else:
            if (anterior ==1 ):
                key= string_list[i-1] + string_list[i]
                anterior=0
            else:
                key=string_list[i]
            #print(inverted_dict[key])
            bin_response+= inverted_dict[key]

        #try:
        #    if string_list[i-1] == '~':
        #        pass
        #    key= string_list[i]
        #    if string_list[i] == '~':
        #        key= string_list[i] + string_list[i +1]
        #    print(inverted_dict[key])
        #    bin_response+= inverted_dict[key]
        #except:
        #    pass
        
        #print(inverted_dict[word])

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

    return convert_list