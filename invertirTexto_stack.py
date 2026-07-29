#Problema: Crea una función que reciba una palabra o frase y devuelva el texto invertido usando una pila.

#Idea: Al meter cada letra en la pila y luego sacarlas una a una, saldrán en orden inverso.


def invertir_texto(word):

    count = 1
    invertido =[]
    stack = []
    palabra = ""

    if len(stack) == 0:
        for l in word:
            stack.append(l) #poner en la pila
   
    while len(stack) >= count:
        
        invertido.append(stack[-count])
        count += 1

    for l in invertido:
        palabra = palabra + stack.pop() # vaciamos el stack en orden invertido


    return f'la palabra invertida {palabra} y el stack ---> {stack}'
 n
print(invertir_texto("Antonio esono"))


        


    