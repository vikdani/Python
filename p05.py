class Rectangle:
    def __init__(self,lenght,breadth):
        self.lenght = lenght
        self.breadth = breadth

    def print_area(self,lenght,breadth):
        area = lenght * breadth
        return area
    def print_perimeter(self,lenght,breadth):
        perimeter = 2*(lenght+breadth)
        return perimeter

class Square(Rectangle):
    def __init__(self,s,lenght,breadth):
        self.s =  s
        super(). __init__(lenght,breadth)
    def area_square(self,s):
        area = s*s
        return area
def main():
    sq = Square(5,6,7)
    one = sq.print_area(5,6)
    print("the of rectangle is :",one)

    two = sq.print_perimeter(5,6)
    print("the perimeter of rectangle is :",two)

    three = sq.area_square(5)
    print("the area of aquare is :",three)
main()            