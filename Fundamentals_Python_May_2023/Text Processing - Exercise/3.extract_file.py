file_path = input().split(chr(92))

for subfile in file_path:
    last_file = file_path[-1].split('.')
    name = last_file[0]
    ext = last_file[1]
    print(f'File name: {name}')
    print(f'File extension: {ext}')
    break