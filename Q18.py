some_dict = {"3":{"g","h","i"},
        "1":{"a","b","c"},
        "2":{"d","e","f"}}
some_dict = {vi: k  for k, v in some_dict.items() for vi in v}
print(some_dict)
