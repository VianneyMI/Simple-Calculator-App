from calculator_model import CalculatorModel
from calculator_controller import CalculatorController
from calculator_view import CalculatorView
from tkinter import StringVar, Button, Entry, Tk

def main():
    
    model = CalculatorModel()
    controller = CalculatorController(model)
    view = CalculatorView(controller)
    
    view.start()

if __name__ == "__main__":
    main()