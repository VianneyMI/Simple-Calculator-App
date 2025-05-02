from tkinter import StringVar, Button, Entry, Tk, Frame

class CalculatorView:
    """
    Classe qui gère l'interface utilisateur de la calculatrice.
    Permet de gérer les éléments d'interface.
    """
    def __init__(self, controller):
        self.controller = controller
        self.gui = Tk()
        self.gui.configure(background="light green")
        self.gui.title("Simple Calculator")
        self.gui.geometry("270x150")
        
        # Variable pour afficher l'expression
        self.equation = StringVar()
        self.equation.set('Enter your expression')
        
        self._create_ui()
    
    def _create_ui(self):
        """
        Crée les éléments d'interface de l'utilisateur
        """
        # Champ d'affichage de l'expression
        expression_field = Entry(self.gui, textvariable=self.equation)
        expression_field.grid(columnspan=4, ipadx=70)
        
        # Création des boutons numériques
        self._create_numeric_buttons()
        
        # Création des boutons d'opération
        self._create_operation_buttons()
    
    def _create_numeric_buttons(self):
        """
        Crée les boutons de manière numérique (0-9)
        """
        # Boucle qui génère les boutons de 1 à 9
        # Utilisation de la POO pour la création des boutons
        # Méthode grid afin de placer les boutons sous forme de grille
        for i in range(1, 10):
            row = 1 + (i-1) // 3
            col = (i-1) % 3
            Button(
                self.gui, 
                text=f' {i} ', 
                fg='black', 
                bg='red',
                command=lambda i=i: self.equation.set(self.controller.on_number_press(i)),
                height=1, 
                width=7
            ).grid(row=row+1, column=col)
       
        Button(
            self.gui,
            text=' 0 ',
            fg='black',
            bg='red',
            command=lambda: self.equation.set(self.controller.on_number_press(0)),
            height=1,
            width=7
        ).grid(row=5, column=0)
        
        Button(
            self.gui,
            text='.',
            fg='black',
            bg='red',
            command=lambda: self.equation.set(self.controller.on_number_press('.')),
            height=1,
            width=7
        ).grid(row=6, column=0)
    
    def _create_operation_buttons(self):
        """
        Crée les boutons des opérations (+, -, *, /, =, Clear)
        """
        Button(
            self.gui,
            text=' + ',
            fg='black',
            bg='red',
            command=lambda: self.equation.set(self.controller.on_number_press("+")),
            height=1,
            width=7
        ).grid(row=2, column=3)
        
        Button(
            self.gui,
            text=' - ',
            fg='black',
            bg='red',
            command=lambda: self.equation.set(self.controller.on_number_press("-")),
            height=1,
            width=7
        ).grid(row=3, column=3)
        
        Button(
            self.gui,
            text=' * ',
            fg='black',
            bg='red',
            command=lambda: self.equation.set(self.controller.on_number_press("*")),
            height=1,
            width=7
        ).grid(row=4, column=3)
        
        Button(
            self.gui,
            text=' / ',
            fg='black',
            bg='red',
            command=lambda: self.equation.set(self.controller.on_number_press("/")),
            height=1,
            width=7
        ).grid(row=5, column=3)
        
        Button(
            self.gui,
            text=' = ',
            fg='black',
            bg='red',
            command=lambda: self.equation.set(self.controller.on_equal_press()),
            height=1,
            width=7
        ).grid(row=5, column=2)
        
        Button(
            self.gui,
            text='Clear',
            fg='black',
            bg='red',
            command=lambda: self.equation.set(self.controller.on_clear()),
            height=1,
            width=7
        ).grid(row=5, column=1)
    
    def start(self):
        """
        Démarre la boucle principale de l'interface
        """
        self.gui.mainloop()