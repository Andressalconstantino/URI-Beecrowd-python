n = int(input())

for i in range(n):
    word = input()
    if len(word)==3:
        if ( word[0]=='o' and word[1]=='n') or (word[0]=='o' and word[2]=='e') or (word[1]=='n' and word[2]=='e'):
            print(1)
        else:
            print(2)
    else:
        print(3)
