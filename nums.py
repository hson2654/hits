a=[]

for i in range(1000,9999):
    a.append(i)
f = open("nums.txt","a")
for i in a:
    f.write(str(i)+'\n')
f.close()
    