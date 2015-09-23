term1=0
term2=1
temp=0

def next_term(term1,term2):
    temp=term1+term2
    term1=term2
    term2=temp
    return(term1,term2)
total = 0
while term1<4000000:

    if term1 %2 ==0:
        total=total+term1
    term1,term2=next_term(term1,term2)
print(total)
