mobiles=[
    [1000,"samsungA52","4g","AMOLED",27000,"samsung",12],
    [1001, "samsungA52s", "5g", "AMOLED", 32000, "samsung",20],
    [1002, "redminote10", "4g", "led", 17000, "redmi",50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi",70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung",1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung",34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung",7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung",89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung",0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple",0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus",67]

]
# #q1 print total number of mobiles
# print(f"total number of mobiles {len(mobiles)}")
#
# # q1 total number of out_of_stock mobiles
# out_of_stock=[mobile for mobile in mobiles if mobile[-1]==0]
# print(len(out_of_stock))
# print(f"total number of out of stock mobiles are: {out_of_stock}")
#
# # q2 total stock
# total_stock=[mobile[-1] for mobile in mobiles ]
# total=sum(total_stock)
# print(f"total number of stocks are: {total}")
#
# # q3 pritn mobiles available in range 20k to 30k
# price_range=[mobile for mobile in mobiles if mobile[4]>=20000 and mobile[4]<=30000]
# print(f"mobiles available in range 20k to 30k are: {price_range}")
#
# # q4 print all 5g phone
# five_g=[mobile for mobile in mobiles if mobile[2]=="5g"]
# print(f"all 5g phone are: {five_g}")
#
# # q5 print samsung mobiles
# samsung=[mobile for mobile in mobiles if mobile[-2]=="samsung"]
# print(f"all samsung mobiles are: {samsung}")
#
# # q6 print costly mobile
# max_price=max([mobile[4] for mobile in mobiles])
# costly_mob=[mobile for mobile in mobiles if mobile[4]==max_price]
# print(f"costly mobile: {costly_mob}")
#
#

#
# avl_max=max(mobiles,key=lambda mobile:mobile[4])
# print(avl_max)

# q7 prin low cost mobiles
#
# avl_min=min(mobiles,key=lambda mobile:mobile[4])
# print(avl_min)
#
# # q8 print all mobiles having stock >10
# stock=[mobile for mobile in mobiles if mobile[-1]>10]
# print(f"mobiles having stock greater than 10 are: {stock}")
#
# # q9 count of mobiles having dispaly amoled
# count=[mobile for mobile in mobiles if mobile[3]=="AMOLED"]
# print(f"count of mobiles having dispay amoled are: {count}")
#
# # q10 sort mobiles based on price oredr by desc
# price=[mobile[4] for mobile in mobiles ]
# price.sort(reverse=True)
# print(f"sorted mobile prices:{price}")
# mobiles.sort(reverse=True,key=lambda mobile:mobile[4])
# print(mobiles)

# q11 sort mobiles based on avl stock oredr by desc
# stock=[mobile[-1] for mobile in mobiles ]
# stock.sort(reverse=True)
# print(f"sorted mobile stocks:{stock}")
mobiles.sort(reverse=True,key=lambda mobile:mobile[-1])
print(mobiles)

# q12 is there any mobile available at rs 10000 ?
# mob=[mobile for mobile in mobiles ]
# mob2=[mob if mob[4]==10000 else "no mobiles available at rs 10000"]
# print(f"mobiles available in rs 10000 are: {mob2} ")
#
# mob_ten=[mob[4]==10000 for mob in mobiles]
# print("available" if True in mob_ten else "na")

# q12 list all mobiles having same price

