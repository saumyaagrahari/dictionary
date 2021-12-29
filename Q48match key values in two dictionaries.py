dic1={'key1': 1,'key2': 3,'key3': 2}
dic2={'key1': 1, 'key2': 2,'key3':2}
for i in dic1:
    for j in dic2:
        if i==j:
            if dic1[i]==dic2[j]:
                print(i,":",dic1[i]) 