#this is homework 1: movie ticket software
calculate=0

print('''Available movies today:
A)12 Strong:  1)2:30   2)4:40   3)7:50   4)10:50
B)Coco:       1)12:40  2)3:45
C)The Post:   1)12:45  2)3:35   3)7:05   4)9:55''')

#input for movie and showtime
movie=input("Movie choice: ")
time=int(input("Showtime: "))

#checking whether or not a valid movie was chosen after showtime
if not (movie=="A" or movie=="B" or movie=="C"):
    print("Invalid option; please restart app...")

#variables for whether a ticket is purchased before 2pm or after 2pm, which will play a part into the final cost
before2adult=0
after2adult=0
before2kid=0
after2kid=0

#checking whether or not a valid showtime is chosen for the movie
if movie=="A":
    if (time>=1 and time <5):
        adult = int(input("Adult tickets: "))
        kid = int(input("Kid tickets: "))
    else:
        print("Invalid option; please restart app...")

if movie=="B":
    if (time>=1 and time <3):
        adult = int(input("Adult tickets: "))
        kid = int(input("Kid tickets: "))
    else:
        print("Invalid option; please restart app...")

if movie=="C":
    if (time>=1 and time <5):
        adult = int(input("Adult tickets: "))
        kid = int(input("Kid tickets: "))
    else:
        print("Invalid option; please restart app...")

#price calculations for before 2 and after 2 tickets
if movie=="A" and (time>=1 and time<5):
    after2adult=adult
    after2kid=kid
    calculate=1

if movie=="B" and time==1:
    before2adult=adult
    before2kid=kid
    calculate=1
if movie=="B" and time==2:
    after2adult=adult
    after2kid=kid
    calculate=1

if movie=="C" and time==1:
    before2adult=adult
    before2kid=kid
    calculate=1
if movie=="C" and (time>=2 and time<5):
    after2adult=adult
    after2kid=kid
    calculate=1

#final cost
cost=(before2adult*11.17)+(before2kid*8.00)+(after2adult*12.45)+(after2kid*9.68)
cost=round(cost,2)

#final printed product, based on whether or not final ticket count is less or equal to 30
if calculate==1:
    total=adult+kid
    if total <= 30:
        print("Total cost: $",cost)
    else:
        print("Invalid option; please restart app...")