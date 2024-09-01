

def readFile(file, formulas):
    with open(file, "r", encoding="utf-8") as f:
        for x in f:
            exp = x.replace("\n", "")
            exp = exp.replace(" ", "")
            formulas.append(exp)

def formulaStringToList(formulaString):

    formulaString = formulaString[1 : -1]
    lastChar = ""
    formulaList = []

    for char in formulaString:

        if char == "{":
            formulaList.append([])

        elif lastChar == "¬":
            formulaList[-1].append(f"¬{char}")

        elif char != "}" and char != "," and char != "¬":
            formulaList[-1].append(char)

        lastChar = char

    return formulaList

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

    if option < cantFormulas:
        list = formulaStringToList(formulas[option - 1])

        print(list)

print(formulas)

