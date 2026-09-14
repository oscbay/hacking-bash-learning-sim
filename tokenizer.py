def tokenize(command):

    quotes = False
    temp_token = ''
    tokens = []
    for char in command:
        if char == '"' or char == "'":
            quotes = not quotes
            temp_token += "'"
            continue

        if char == ' ' and quotes == False:
            tokens.append(temp_token)
            temp_token = ''
            #need to make this triger at the end of the string as well, so that the last token is added to the list

        else:
            temp_token += char

    tokens.append(temp_token)
    return tokens