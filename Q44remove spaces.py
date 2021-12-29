dictionary={'S 001': ['Math', 'Science'], 'S  002': ['Math','English']}
# # creating a dictionary of type string
# # removing space from keys
# # storing them in same dictionary
# dictionary={a.translate ({32:None}):
#     b for a,b in dictionary.items()}
# # printing new dictionary
# print("new dictionary:",dictionary)
n={}
for i in dictionary:
    for x in i:
        # print(x)
        if x is ' ':
            k= i.replace(' ','')
            for i,x in dictionary.items():
                n.update({k:x})
                
print(n)