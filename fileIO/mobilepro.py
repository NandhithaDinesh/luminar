fread=open("mobiles.txt","r")
all_mobiles=[mobile.rstrip("\n").split(",") for mobile in fread]
# for line in fread:
#     mobile=line.rstrip("\n").split(",")
#     all_mobiles.append(mobile)
# print(all_mobiles)

costly_mob=max(all_mobiles,key=lambda mob:int(mob[2]))
print(costly_mob)
fiveg=[mobile for mobile in all_mobiles if mobile[3]=="5g"]
print(fiveg)