from ast import Return

def identifier(data):
    if  data[0].isalpha() and len(data) >= 1 and len(data) <= 6 and data.isalnum():
        return("Entrada valida")
    else:
        return("Entrada invalida")

