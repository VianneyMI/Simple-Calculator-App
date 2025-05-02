class CalculatorModel:
    """
    Classe responsable du model de la calculatrice.
    Gère l'expression mathématique pour les calculs.
    """
    def __init__(self):
        self.expression = ""
    
    def add_to_expression(self, value):
        """
        Ajoute une valeur à l'expression courante
        """
        self.expression += str(value)
        return self.expression
    
    def calculate(self):
        """
        Évalue l'expression mathématique
        """
        try:
            total = str(eval(self.expression))
            self.expression = ""
            return total
        except:
            self.expression = ""
            return "error"
    
    def clear(self):
        """
        Efface l'expression courante
        """
        self.expression = ""
        return self.expression