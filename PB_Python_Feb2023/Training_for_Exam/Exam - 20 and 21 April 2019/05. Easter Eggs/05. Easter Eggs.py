import math
import sys

easter_bread = int(input())
max_use_sugar = -sys.maxsize
max_use_flour = -sys.maxsize
used_sugar = 0
used_flour = 0
for i in range (0, easter_bread):
    sugar_needed = int(input())
    flour_needed = int(input())

    used_sugar += sugar_needed
    used_flour += flour_needed
    if sugar_needed > max_use_sugar:
        max_use_sugar = sugar_needed
    if flour_needed > max_use_flour:
        max_use_flour = flour_needed

package_sugar = math.ceil(used_sugar / 950)
package_flour = math.ceil(used_flour / 750)

print(f'Sugar: {package_sugar}')
print(f'Flour: {package_flour}')
print(f"Max used flour is {max_use_flour} grams, max used sugar is {max_use_sugar} grams.")