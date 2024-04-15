#module 6A

#question 1
'''templist=[]
for i in range(0,7):
    temperature=input("Enter Temperature: ")
    templist.append(int(temperature))
print("\nTemperatures: ",templist)
average=0
for i in templist:
    average+=i
average/=len(templist)
average=round(average,2)
print("Average Temperature: ",average,"°C",sep="")
templist.sort()
print("Highest Temperature: ",templist[-1],"°C",sep="")
print("Lowest Temperature: ",templist[0],"°C",sep="")
if average<15:
    print("It's quite cold. Consider indoor activities.")
elif average>25:
    print("It's warm. A good time for swimming or beach visits.")
else:
    print("Perfect weather for outdoor activities like hiking.")'''

#question 2:
'''def find_mountains(mountain_list,min_height):
    valid=[]
    for i in mountain_list:
        if i>=min_height:
            valid.append(i)
    return valid'''

#question 3:
'''def remove_four(numbers):
    iteration=0
    for num in numbers:
        for char in str(num):
            if char=="4":
                numbers[iteration]="replaced"
        iteration+=1
    return numbers

print(remove_four([94]))'''

#module 6B

#question 2:
'''def dupe_letter(word):
   newset=set()
   string=""
   wordlist=list(word)
   for i in wordlist:
       if i in newset:
           string+=""
       else:
           newset.add(i)
           string+=i
   return string

print(dupe_letter("killlingggghhh"))'''

#question 3:
'''def member_attendance(event_attendance):
    dict={}
    for i in event_attendance:
        name=i[0:i.index(":")]
        if name in dict:
            dict[name]+=1
        else:
            dict[name]=1
    return dict'''

#question 4:
'''def find_unique(nums):
    setlist=set()
    biglist=[]
    iteration=0
    for i in nums:
        for a in nums[iteration]:
            biglist.append(a)
        iteration+=1
    for c in biglist:
        if biglist.count(c)==1:
            setlist.add(c)
    return setlist'''

'''def update_contact(contacts,name,number):
    for i in contacts:
        if i==name:
            contacts[i]=number
            return contacts
        contacts[name]=number
        return contacts

contacts={"Alice": "123-456-7890","Bob": "987-654-3210"}
print(update_contact(contacts,"Charlie","555-666-7777"))'''

#EXAM 2 OFFICIAL REVIEW DOC

#question 1:
'''def num_in_sequence(sequences):
    list=[]
    count = 1
    previousnum=sequences[0]
    for i in sequences[1:]:
        if i==previousnum:
            count+=1
        else:
            list.append(count)
            count=1
        previousnum=i
    list.append(count)
    return list

print(num_in_sequence([2,2,4,4,4,2,2,1,3,5,5]))'''

#question 2:
'''def most_skittles_in_bags(bags_of_skittles):
    greencount=0
    redcount=0
    orangecount=0
    yellowcount=0
    purplecount=0
    for i in bags_of_skittles:
        if "G" in i:
            greencount+=1
        if "R" in i:
            redcount+=1
        if "O" in i:
            orangecount+=1
        if "Y" in i:
            yellowcount+=1
        if "P" in i:
            purplecount+=1
    countlist=[]
    countlist.extend([greencount,redcount,orangecount,yellowcount,purplecount])
    countlist.sort()
    skittleslist=[]
    if greencount==countlist[-1]:
        skittleslist.append("G")
    if redcount==countlist[-1]:
        skittleslist.append("R")
    if orangecount==countlist[-1]:
        skittleslist.append("O")
    if yellowcount==countlist[-1]:
        skittleslist.append("Y")
    if purplecount==countlist[-1]:
        skittleslist.append("P")

    return skittleslist

print(most_skittles_in_bags(["RPYOR", "PGYGO", "YYPRY", "OPOPY", "RYPYR"]))'''


