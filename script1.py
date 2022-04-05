l=list(map(str,input().split()))
l2=[]
l3=['A','B','C']
l2.append(l[0][1])
l2.append(l[2][1])
l2.append(l[4][1])
for i in l3:
    if i not in l2:
        print(i,"is missing")
print("OK")
