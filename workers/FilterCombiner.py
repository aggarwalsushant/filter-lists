import os

# os.chdir("C:\\Users\\su003ag\\Sushant\\Learn\\filter-lists")
# cwd = os.getcwd()
# print("current working dir: ", cwd)
print('Starting filter merging...')

result= open("result.txt","w+")

for dirpath, dirnames, files in os.walk('./filters'):
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension == '.txt':
            with open(dirpath+'\\'+file, 'r') as f:
                for line in f:
                    result.write(line)
                        
result.close()
print('Filter merging complete.')