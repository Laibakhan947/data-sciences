#two types of loop
#while loop
#for loop

#while loop
#x=0
#while(x<=5):
     # print(x)
    #  x=x+1

#for loop
#x=0
#for x in range(5,10):
     # print(x)

#array(dataset)

#days=["mon","tue","wed","thu","fri","sat","sund"]
#for days in days:
   # print(days)
 #continue and break                                                           
days=['mon','tue','wed','thu','fri','sat','sund']
for day in days:
        if(day=='sund'):
          print("sunday is funday")
          break #loop break
        print(day)

#continue
days=['mon','tue','wed','thu','fri','sat','sund']
for day in days:
     if(day=='fri'):
        print("firiday is prayer day")
        continue #skip friday
     print(day)

     print(day[2:-2])
     print(days[2])