import os

print('Starting filter merging...')

result= open("CustomFiltersSA.txt","w+")

for dirpath, dirnames, files in os.walk('./filters'):
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension == '.txt':
            with open(dirpath+'\\'+file, 'r') as f:
                for line in f:
                    result.write(line)
                        
result.close()
print('Filter merging complete.')