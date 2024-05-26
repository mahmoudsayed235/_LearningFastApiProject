my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
index=0
while index<3:
    for x in my_list:
        if x == 'Monday':
            continue
        print(x)
    index+=1

