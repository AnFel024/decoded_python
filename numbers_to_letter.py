def number_to_letter(i):
    str_response=""
    if i<10:
        str_response=str(i)

    else:
        import string 
        if (i<93):
            str_response= string.printable[i]
        elif (i>93) and (i<175):
            str_response= string.printable[93] + string.printable[i-82]
            """  ~ ª  """
        else:
            str_response= string.printable[92] + string.printable[i-165]
    
    return str_response
