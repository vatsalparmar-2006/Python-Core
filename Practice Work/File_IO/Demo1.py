fp = open('MyData.txt', 'r')
print(type(fp))  # '_io.TextIOWrapper'

print('-----')

for i in fp:            # Hello
    print(i)
                        # World                                       

print('-----')


for i in fp:            # Hello
    print(i, end='')    # World

print('-----')

print(fp.name)          # MyData.txt
print(fp.mode)          # r
print(fp.closed)        # False
fp.close()
print('-----')

fp = open('MyData.txt')
data = fp.read()
print(type(data))
fp.close()         # class=str

print('-----')

fp = open('MyData.txt')
data = fp.readlines()
print(data)
print(type(data))     # class=list
fp.close()    

print('-----')

fp = open('MyData1.txt', 'w')   # create new file
data = 'Hello Students'
fp.write(data) 
fp.close()  

print('-----')

fp = open('MyData1.txt', 'w')    # overwrite data
data = 'Hii Python'             
fp.write(data) 
fp.close()  

print('-----')

fp = open('MyData1.txt', 'a')    # append data
data = ' How are you ??'             
fp.write(data) 
fp.close()  

print('-----')

fp = open('MyData1.txt', 'w')    # writeslines only for set,suple,list 
li = [10,20,30]             
fp.writelines(li)    # error  write() argument must be str, not int
fp.close()  

print('-----')

fp = open('MyData1.txt', 'w')    # writeslines only for set,suple,list 
li = [10,20,30]
ansli = [str(i) for i in li]             
fp.writelines(ansli)    # error  write() argument must be str, not int
fp.close()  

print('-----')

fp = open('img1.png', 'rb')       # rb(read byte) for any file
data = fp.read()
fp1 = open('img1COPY.png', 'wb')
fp1.write(data)
fp.close()