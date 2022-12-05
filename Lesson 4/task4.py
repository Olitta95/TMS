f = {
            "key1": "John",
            "key2": {
                "key3": "Alex",
                "key4": {
                "key5": ["Kate", "Mar"],
                    "key6": {
                        "key7": ["Bob", "Duke",
                                 {
                                     "key8": {
                                         "key9": [
                                             "Liza",
                                             {
                                              "key10": ["Mark"]
                                             }
                                         ]
                                     }
                                 }
                             ]
                    },
                },
                "key8":"Robert"
            }
        }
def get_files(path,depth=0):
    for f in path:
        print(" ", + depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth+1)
        else:
            print(" ", +(depth+1), " ".join(path[f]))
get_files(f)

