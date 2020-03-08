def mergeSort(a):
    n=len(a)
    mid=n//2
    if n<=1:
        return a
    else:
        print(mid)
        left=mergeSort(a[:mid])
        right=mergeSort(a[mid:])
        return merge(left,right)

def merge(l,r):
    ln=len(l)
    rn=len(r)
    temp=[]
    li,ri=0,0
    while(li<ln and ri<rn):
        if l[li]<r[ri]:
            temp.append(l[li])
            li=li+1
            continue
        elif l[li]>r[ri]:
            temp.append(r[ri])
            ri=ri+1
            continue
        elif l[li]==r[ri]:
            temp.append(l[li])
            li=li+1
            ri=ri+1
            continue
        else:
            li=li+1
            ri=ri+1

    print(li,ln, ri,rn)
    if li<ln:
        for i in range(li,ln):
            temp.append(l[i])
    if ri<rn:
        for j in range(ri,rn):
            temp.append(r[j])
    return temp
print (mergeSort([2,1,7,5,4,0,9,2,3,89]))






