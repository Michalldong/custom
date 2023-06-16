import os

directory_test = 'data/test/labels/'
directory_train = 'data/train/labels/'
directory_valid ='data/valid/labels/'

for filename in os.listdir(directory_valid):
    if filename.endswith('.txt'):
        filename = directory_valid + filename
        with open(filename, 'r') as f:
            lines = f.readlines()
            filtered_lines = [line for line in lines if line.startswith(('1', '2'))]
            for i in range(len(filtered_lines)):
                if filtered_lines[i].startswith('2'):
                    filtered_lines[i] = '0' + filtered_lines[i][1:]
            with open(filename, 'w') as out:
                for line in filtered_lines:
                    out.write(line + '\n')
