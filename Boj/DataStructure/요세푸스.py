lst = [1,2,3,4,5,6,7]
i=1
while (len(lst)!=0):
    if (i >=7):
        i = i % 6
    if(i%3==0&i<=6):
       # print(lst[i-1])
        print(lst.pop(i-1))
        #print(i)


    i+=1