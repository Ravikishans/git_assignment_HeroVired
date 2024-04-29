import math
class GeometryCalculator:
<<<<<<< HEAD
    def calculate_circle_area(self, radius):

        return math.pi * radius ** 2
    def calculate_rectangle_area(self,length,width):

        return length*width
if __name__=="__main__":
    calculator = GeometryCalculator()
    radius = 5
    print(f"area of the circle with radius {radius}")

    calculator = GeometryCalculator()
    length = 10
    width = 6
    print(f"the area of rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length,width)}")



