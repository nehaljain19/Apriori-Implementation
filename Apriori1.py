
# coding: utf-8

# In[4]:


import itertools

def rSubset(arr, r): #Calculate subsets of size r from list arr
    return list(itertools.combinations(arr, r))
def confidence(num,den): #Calculate confidence
    return num/den
def lift(num,d1,d2): #Calculate lift
    return num/(d1*d2)

data=[[1,2,5],[2,4],[2,3],[1,2,4],[1,3],[2,3],[1,3],[1,2,3,5],[1,2,3]] #Dataset
k=1
l=0
count = [0]*(pow(2,5)-1) #Array to track support count of sets
minSup = 2 #minimum Support count
sets=[]
frequency = {}
#Finding subsets of size 1 and comparing their support count
for i in rSubset([1,2,3,4,5],1):
    for j in data:
        if set(i) <= set(j):
            count[l]+=1
    if count[l]>=minSup:
        frequency[i[0]] = count[l]
        sets.append(list(i))
        flat_list = [item for sublist in sets for item in sublist]
    l+=1
#Finding subsets of size 2 to 6 and comparing their support count
for k in range(2,6):
    for i in rSubset(flat_list,k):
        for j in data:
            if set(i) <=set(j):
                count[l]+=1
        if count[l]>=minSup:
            frequency[tuple(i)] = count[l]
        l+=1
            
print("Frequent Itemsets:")
print(frequency)
conf={}
liftdict={}

for key in frequency:
    if isinstance(key,tuple):
        num = frequency[key] #Frequency of the itemset
        for var in key:
            temp1 = (var)
            den = frequency[var] #LHS for denominator
            listtup = []
            for var2 in key:
                if var2!=var:
                    listtup.append(var2)
            if len(listtup)>1:
                temp2 = tuple(listtup)
            else:
                temp2=listtup[0]
            c = confidence(num,den)
            if c>=0.5: #Checking if confidence is greater than threshold
                conf[(temp1,temp2)] = c
                liftdict[(temp1,temp2)] = lift(num,den,frequency[temp2])
            c2 = confidence(num,frequency[temp2])
            if c2>=0.5:
                conf[(temp2,temp1)] = c2
                liftdict[(temp2,temp1)] = lift(num,den,frequency[temp2])
print("\n\nAssociation Rules:CONFIDENCE")
for key in conf:
    print(key[0], "-->",key[1] ,"=",conf[key])
    
print("\n\nLIFT CONFIDENCE")
for key in liftdict:
    print(key[0], "-->",key[1] ,"=",liftdict[key])

