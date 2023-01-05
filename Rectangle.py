class  Square:
    def CalculatorArea(self):
        print("Enter Side:")
        self.s=float(input())
        area=self.s*self.s
        print("Area of rectangle is=",(area))

    def CalculatorPerimeter(self):
        perimeter=4*self.s
        print("Perimeter of rectangle is=",(perimeter))

c=Square()
x=c.CalculatorArea()
y=c.CalculatorPerimeter()
