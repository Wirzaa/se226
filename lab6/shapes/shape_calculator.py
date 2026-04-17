import geometry_utils

def main():
    
    shape_functions = {
        "circle" :  geometry_utils.circle_area,
        "rectangle" : geometry_utils.rectangle_area,
        "triangle" : geometry_utils.triangle_area
        }
    
    shape = input("Enter your shape: ").lower()

    if shape == "circle":
        radius = int(input("Enter radius: "))
        print(shape_functions[shape](radius))

    elif shape == "rectangle":
        width = int(input("Enter width: "))
        height = int(input("Enter height"))
        print(shape_functions[shape](width, height))

    elif shape == "triangle":
        base = int(input("Enter base: "))
        height = int(input("Enter height:"))
        print(shape_functions[shape](base, height))
    
main()



    
