import math

class ShapeCalculator:
    def area(self, a=None, b=None):
        if a is not None and b is None:
            return math.pi * a * a  # Circle
        elif a is not None and b is not None:
            return a * b  # Rectangle
        else:
            return 0

# Demo
calc = ShapeCalculator()
print("Area of circle (r=5):", calc.area(5))
print("Area of rectangle (4x6):", calc.area(4, 6))
