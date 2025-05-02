class CalculatorController:
    """
    Classe contrôleur qui fait le lien entre view et model.
    Permet de générer les controles de l'utilisateur.
    """
    def __init__(self, model):
        self.model = model
    
    def on_number_press(self, number):
        """
        Gère l'expression du bouton numérique ou opérateur
        """
        return self.model.add_to_expression(number)
    
    def on_equal_press(self):
        """
        Gère l'expression du bouton égal
        """
        return self.model.calculate()
    
    def on_clear(self):
        """
        Gère l'expression du bouton clear
        """
        return self.model.clear()