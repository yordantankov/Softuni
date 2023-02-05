lenght = int (input())
wide = int (input())
height = int (input())
percent = float (input())

volume = lenght * wide * height

liters = volume / 1000

needed_liters = liters * (1 - (percent / 100))

print (needed_liters)