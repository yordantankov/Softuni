tabs_qty = int(input())
salary = int(input())

for i in range (0, tabs_qty):
    tab_name = input()
    if tab_name == "Facebook":
        salary -= 150
    elif tab_name == "Instagram":
        salary -= 100
    elif tab_name == "Reddit":
        salary -= 50

    if salary <= 0 :
        print(f'You have lost your salary.')
        exit()

print(salary)