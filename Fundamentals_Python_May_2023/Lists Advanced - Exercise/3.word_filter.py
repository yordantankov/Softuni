some_text = input().split()

filtered_text =[text for text in some_text if len(text) % 2 == 0]

for text in filtered_text:
    print(text)