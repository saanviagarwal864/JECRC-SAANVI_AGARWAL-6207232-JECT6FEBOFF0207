'''
append

##for append operation,
1. write()->single line
2. writelines()->multiple lines

'''
file=open('jecrc.txt','a+')

#file.write('jecrc is university')
file.write('\njecccrrccc 2.0')
file.writelines([
    '\nHere,food is good\n',
    '\nballe balle'
])
file.seek(0)
print(file.read())

file.close()