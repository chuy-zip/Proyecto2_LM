from sat_lib import *

from copy import deepcopy

def dpll(formula, assignment):
    print(f'Formula Actual: {formula}')
    # Si la formula es vacia, es satisfacible
    if formula.is_empty():
        print(f'Formula Vacia')
        return True, assignment
    
    # Si hay una clausula vacia dentro de la formula, no es satisfacible
    if formula.has_empty_clause():
        print(f'La formula tiene una clausula vacia')
        return False, None
    
    # Se selecciona el primer simbolo para asignarle un valor
    symbol = formula.choose_symbol()

    # Se actualiza la formula pasandole como parametro el simbolo en verdadero
    print(f'Asignado Simbolo: {symbol} a Verdadero')
    new_assignment = deepcopy(assignment)
    new_assignment[symbol] = True
    print(f'Asignaciones Actuales: \n{new_assignment}')
    new_formula = update_formula(formula, Literal(symbol, True))
    satisfiable, result = dpll(new_formula, new_assignment)
    if satisfiable:
        return True, result

    # Si no hay una solucion posible con un valor verdadero, se prueba con un valor falso
    print(f'Asignado Simbolo: {symbol} a Falso')
    new_assignment = deepcopy(assignment)
    new_assignment[symbol] = False
    print(f'Asignaciones Actuales: \n{new_assignment}')
    new_formula = update_formula(formula, Literal(symbol, False))
    satisfiable, result = dpll(new_formula, new_assignment)
    
    # Si es satisfacible regresa True y el resultado
    if satisfiable:
        return True, result
    
    # Si ambos valores True y False no son satisfacibles, retorna False y None
    return False, None

# Actualiza una formula con la asignacion de valor a una variable
def update_formula(formula, literal):
    # Crea un literal con la negacion de la asignacion
    neg_literal = literal.negate()
    # Crea una nueva formula simplificada con la asignacion
    new_formula = Formula()
    # Revisa todas las clausulas en la formula
    for clause in formula.clauses:
        # Si el literal se encuentra en los literales de la clausua se continua (sin agregar)
        if literal in clause.literals:
            print(f'Encontrado literal: {literal}, en clausula: {clause}. Removida de la formula')
            continue
        else:
            # Si se encuentra la negacion del literal se remueve el literal y se agrega la clausula a la formula
            if neg_literal in clause.literals:
                print(f'Encontrado literal: {neg_literal}, en clausula: {clause}. Removido de la clausula')
                new_clause = Clause(clause.literals.copy())
                new_clause.remove_literal(neg_literal)
                print(f'Clausula resultante: {new_clause}')
                new_formula.add_clause(new_clause)
            # De lo contrario
            else:
                new_formula.add_clause(clause)
    return new_formula

formulas = parse_file("input.txt")
value, assignment = dpll(formulas[5], {})
print(f'Satisfacible: {value}, Asignaciones: {assignment}')

# Actualiza una formula con la asignacion de valor a una variable
def update_formula(formula, literal):
    # Crea un literal con la negacion de la asignacion
    neg_literal = literal.negate()
    # Crea una nueva formula simplificada con la asignacion
    new_formula = Formula()
    # Revisa todas las clausulas en la formula
    for clause in formula.clauses:
        # Si el literal se encuentra en los literales de la clausua se continua (sin agregar)
        if literal in clause.literals:
            print(f'Encontrado literal: {literal}, en clausula: {clause}. Removida de la formula')
            continue
        else:
            # Si se encuentra la negacion del literal se remueve el literal y se agrega la clausula a la formula
            if neg_literal in clause.literals:
                print(f'Encontrado literal: {neg_literal}, en clausula: {clause}. Removido de la clausula')
                new_clause = Clause(clause.literals.copy())
                new_clause.remove_literal(neg_literal)
                print(f'Clausula resultante: {new_clause}')
                new_formula.add_clause(new_clause)
            # De lo contrario
            else:
                new_formula.add_clause(clause)
    return new_formula

formulas = parse_file("input.txt")
value, assignment = dpll(formulas[5], {})
print(f'Satisfacible: {value}, Asignaciones: {assignment}')