

def readFile(file, formulas):
    with open(file, "r", encoding="utf-8") as f:
        for x in f:
            exp = x.replace("\n", "")
            exp = exp.replace(" ", "")
            formulas.append(exp)



# Inicio del programa

formulas = []

readFile("expressions.txt", formulas)
formulas.append("Salir")

cantFormulas = len(formulas) 

option = -1 

while option != cantFormulas:

    print("Selecciona una opcion para verificar si la expresion booleana es satisfacible")

    for idx, form in enumerate(formulas):
        print(f"{idx + 1}. {form}")

    option = int(input())

print(formulas)

