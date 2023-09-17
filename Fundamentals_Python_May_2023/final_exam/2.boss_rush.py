import re

def main():
    n = int(input())
    pattern = r'^\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#$'

    for _ in range(n):
        input_line = input().strip()
        if re.match(pattern, input_line):
            boss_name, boss_title = re.findall(pattern, input_line)[0]
            print(f"{boss_name}, The {boss_title}")
            print(f">> Strength: {len(boss_name)}")
            print(f">> Armor: {len(boss_title)}")
        else:
            print("Access denied!")

if __name__ == "__main__":
    main()