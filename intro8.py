file1 = open('m.txt')
for line in file1:
 print(line)
file2 = open('n.txt','w')
line2 = "This is my program!!!! \n"
file2.write(line2)
