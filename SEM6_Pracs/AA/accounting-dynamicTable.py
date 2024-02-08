def accounting(n):
    size=1
    total=0
    dcost=0
    icost=0
    bank=0
    totalfinal=0
    print('Elements\tDoublingCost\tInsertion Cost\tTotal Cost\t\tBank')

    for i in range(1,n+1):
        icost=1
        if i>size:
            size*=2
            dcost=i-1
        total=icost+dcost
        totalfinal=total+totalfinal
        bank+=(3-total)
        print(i,'\t\t',dcost,'\t\t',icost,'\t\t',total,'\t\t\t',bank)
        icost=0
        dcost=0
    return totalfinal/n

n=int(input('Enter number of elements : '))
print('Accounting method')
a=accounting(n)
print('Accounting cost =',a)