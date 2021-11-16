def number_to_letter(i):
    str_response=""
    if i<10:
        str_response=str(i)

    else:
        from string import ascii_letters
        str_response= ascii_letters[i-10]
    
    return str_response
