def group_infos():
    groupname = input("What is the name of your group?")
    groupsize = input("What is the size of your group?")
    date = input("What is date?")
    venue = input("Where was the place?")
    medal = input("What type of medal did you get?")
    return(groupname, groupsize, date, venue, medal)

group_records = []

for i in range(5):
    details = group_infos()
    group_records.append(details)

for i in group_records:
    print(i)


