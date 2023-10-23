def rectangle(lengt, widht):
    if not isinstance(lengt, int) or not isinstance(widht, int):
        return "Enter valid values!"

    def area():
        return lengt * widht

    def perimeter():
        return 2 * (lengt + widht)

    result = f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    return result


print(rectangle(2, 10))
print(rectangle('2', 10))
