array1=[10,7,6,80,50,90]
array2=[9,8,5,89]
intersection=[]
for i in range(len(array1)):
    intersection.append(array1[i])
    for j in range(len(array2)):
        intersection.append(array2[j])
print(intersection)
print("intersection point=",array2[0])        