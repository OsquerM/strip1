#Variables Globales
stext = ""
#Funciones
def run(text: str) -> str:
    # TODO
    global stext
    #Variables locales
    
    stext = text[1:-1]
    return stext

#Codigo Principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(stext)