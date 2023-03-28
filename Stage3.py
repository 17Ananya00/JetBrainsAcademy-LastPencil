print("How many pencils would you like to use:");
pencils = int(input());
print("Who will be the first (John, Jack):");
names = ["John", "Jack"];
first = input();
names.remove(first);
second = names[0];
newNames = [first, second];
print("|"*pencils)
while pencils>0:
    for i in newNames:
        print(i + " 's turn:")
        remove = int(input());
        pencils -= remove;
        print("|"*pencils);
        if pencils == 0:
            break;
