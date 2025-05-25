print(' Name: Rahul G \n USN: 1AY24AI088 \n Section: O\n')
row=int(input("Enter a number:"))
col=int(input("Enter a number:"))
for i in  range (1,row+1):
    print('Table for ',+i)
    for j in range(1,col+1):
        k=i*j
        print(str(i),'*',str(j),str('='),str(k))
    print('\n')
