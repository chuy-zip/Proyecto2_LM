# Representacion de literales, el simbolo una variable booleana e is_positive para determinar si es la negacion
class Literal:
    def __init__(self, symbol, is_positive=True):
        self.symbol = symbol
        self.is_positive = is_positive
    
    def __eq__(self, other):
        return self.symbol == other.symbol and self.is_positive == other.is_positive
    
    def __hash__(self):
        return hash((self.symbol, self.is_positive))
    
    def __repr__(self):
        return f"{'' if self.is_positive else '-'}{self.symbol}"
    
# Representacion de clausulas, una disyuncion (OR) de literales
class Clause:
    def __init__(self, literals=None):
        self.literals = set(literals) if literals else set()

    def add_literal(self, literal):
        self.literals.add(literal)

    def remove_literal(self, literal):
        self.literals.discard(literal)
    
    def is_empty(self):
        return len(self.literals) == 0
    
    def __repr__(self):
        return " ∨ ".join(map(str, self.literals))
    
# Representacion de formulas, una conjuncion (AND) de clausulas
class Formula:
    def __init__(self, clauses=None):
        self.clauses = clauses if clauses else []

    def add_clause(self, clause):
        self.clauses.append(clause)

    def is_empty(self):
        return  len(self.clauses) == 0
    
    def has_empty_clause(self):
        return any(clause.is_empty() for clause in self.clauses)
    
    def choose_symbol(self):
        for clause in self.clauses:
            for literal in clause.literals:
                return str(literal.symbol)
    
    def __repr__(self):
        return " ∧ ".join(f"({clause})" for clause in self.clauses)

def parse_formula_line(line):
    formula = Formula()
    clause_texts = line.strip()[1:-1].split("},{")
    for clause_text in clause_texts:
        literals = clause_text.replace("{", "").replace("}", "").split(",")
        clause = Clause()
        for literal in literals:
            if literal.startswith("-"):
                clause.add_literal(Literal(literal[1:], is_positive=False))
            else:
                clause.add_literal(Literal(literal, is_positive=True))
        formula.add_clause(clause)
    return formula

def parse_file(filename):
    formulas = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                formula = parse_formula_line(line)
                formulas.append(formula)
    return formulas

