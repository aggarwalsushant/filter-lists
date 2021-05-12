import os

os.chdir("C:\\Users\\su003ag\\Sushant\\Learn\\filter-lists\\filters")
cwd = os.getcwd()
print("current working dir: ", cwd)

result= open("result.txt","w+")

for dirpath, dirnames, files in os.walk('.'):
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension == '.txt':
            with open(dirpath+'\\'+file, 'r') as f:
                for line in f:
                    result.write(line)
                        
result.close()