# Uzupełnij very_complex_operation() zdefiniowanym przez siebie wyjątkiem TrainingError
# tak, aby wyświetlone zostały linie: "I want to see you" oraz "I want to see you too".
def very_complex_operation():
    pass

try:
    very_complex_operation()
except ValueError as e:
    print(f"I want to see you")
except Exception as e:
    print(f"I do not want to see you")
finally:
    print(f"I want to see you too")
