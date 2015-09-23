count=1000
total=0
while count > 0:
     if  count %3==0 or count %5==0:
        total=total+count
     count=count-1
print(total)
