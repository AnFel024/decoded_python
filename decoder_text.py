from encoder_text import encode_text
from list_bin import convert_bin_to_list

from datetime import datetime

import io
import PIL.Image as Image
Image.LOAD_TRUNCATED_IMAGES = True

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])

def decode_text(encoded_string, input_base, is_image):
    if is_image:
        response_list= convert_bin_to_list(encoded_string, input_base, is_image, False)
        response_string= ''.join(response_list)
        string_byte_array= encode_text(response_string, 16, False, True)
        
        hex_string= bytearray.fromhex(str(string_byte_array))
        image = Image.open(io.BytesIO(hex_string))
        image.save('./decoded_image_bx_'+str(input_base)+'_hour_'+str(datetime.now().hour)+':'+str(datetime.now().minute)+'.png')

        print("Imagen guardada")

    else:
        base= int(input_base)
        convert_list= convert_bin_to_list(encoded_string, base, is_image, True)
        response= ""
        for binary_item in convert_list:
            response+= chr(int(binary_item, 2))
        if not is_image:
            print('*'*20)
            #Se muestran los resultados.
            print('*'*20)
            print("Texto: ", encoded_string)
            print('*'*20)
            print('Decodificado en base: ', base)
            print('*'*20)
            print("Texto decifrado: ", response)
            print('*'*20)

        return response