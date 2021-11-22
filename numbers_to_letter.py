def number_to_letter(i):
    str_response=""
    if i<10:
        str_response=str(i)

    else:
        import string 
        if (i<91):
            str_response= string.printable[i]
        elif (i>=91) and (i<173):
            str_response= string.printable[92] + string.printable[i-81]
            """  } ª  """
        else:
            str_response= string.printable[93] + string.printable[i-164]
            """ ~ """
    return str_response
