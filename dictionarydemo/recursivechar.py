# pattern="ABACCD"
# char_count={}
# for char in pattern:
#     if char in char_count:
#         print("first recursive charachter",char)
#         break
#     else:
#         char_count[char]=1


# pattern="ABACCD"
# char_count={}
# rec_char=[]
# for char in pattern:
#     if char in char_count:
#         rec_char.append(char)
#     else:
#         char_count[char]=1
#
# print(rec_char[1],"second recursive character")


word_count={"a":2,"b":1,"c":3,"d":4,"e":2}
wc_list=word_count.items()
print(sorted(wc_list, key=lambda item:item[1],reverse=True))
print(max(wc_list,key=lambda item:item[1]))
print(min(wc_list,key=lambda item:item[1]))

