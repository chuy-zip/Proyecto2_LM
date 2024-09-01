import itertools

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

def get_variables(formula_list):
    variables = set()
    for clause in formula_list:
        for literal in clause:
            variable = literal.replace('¬', '')  # Quita la negación para obtener la variable
            variables.add(variable)
    return list(variables)

import itertools

def generate_assignments(variables):
    return list(itertools.product([False, True], repeat=len(variables)))

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

        formula_list = formulaStringToList(formulas[option - 1])
        print(formula_list)
        
        variables = get_variables(formula_list)

        print(f"Variables identificadas en la expresion: {variables}")

        assignments = generate_assignments(variables)
        print(f"Total de combinaciones posibles: {len(assignments)}")

        for assignment in assignments:  # Mostrar solo las primeras 5 combinaciones
            print(dict(zip(variables, assignment)))
        
        print()
        
        

print(formulas)

