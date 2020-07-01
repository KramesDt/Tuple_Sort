number_of_data= int(input("enter the amount of data to be sorted:\t"))
print("enter the name age and score seperated by comma")
c,rev=[],True
for i in range(number_of_data):
    try:
        c.append(tuple(input().split(",")))
    except:
        print("enter the name age and score seperated by comma")
while True:
    sort_option=int(input("sort by\n1.name\n2.age\n3.score\n9.to exit sorting\n"))
    if sort_option>0 and sort_option<4:
        if sort_option==1:
            rev=False
            intro="sorted by name"
        elif sort_option==2:
            intro="sorted by age"
        else:
            intro="sorted by score"
        print(intro,sorted((c[i] for i,_ in enumerate(c)),key=lambda t: t[sort_option-1],reverse=rev))
    elif sort_option==9:
        break
        print("application closed")
    else:
        print ('invalid input try again')