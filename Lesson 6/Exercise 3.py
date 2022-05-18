art_1 = input()
art_2 = input()
art_3 = input()

if (len(art_1) > len(art_2)) and (len(art_1) > len(art_3)):
    print(art_1)
elif (len(art_2) > len(art_1)) and (len(art_2) > len(art_3)):
    print(art_2)
else:
    print(art_3)
