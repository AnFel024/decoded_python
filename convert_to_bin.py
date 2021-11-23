import math

def convert_to_list(byte_list, base, is_image):
    
    #Agrupa los resultados en un array del tamaño del exponente de la base.
    cont=0
    convert_list= []
    str_append= ''
    for i in range(0,len(byte_list)):
        cont+=1
        zeros= ''
        str_append+= byte_list[i]
        if (cont==math.log(int(base), 2)):
            convert_list.append(str_append)
            #if not is_image:
            #    print(str_append)
            cont=0
            str_append= ''

    if str_append != '':
        zeros+= ''
        i= math.log(int(base), 2)-len(str_append)
        #print(str(i))
        #print (len(str_append))
        if (i != 0):
            for j in range(int(i)):
                zeros+= '0'
        str_append+= zeros
        convert_list.append(str_append)
        #print(str_append)

    return convert_list