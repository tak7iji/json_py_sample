import json
import sys

args = sys.argv

with open(args[1]) as f1:
    ob = json.load(f1)

    n_ob = {}
    ob.pop("g")
    n_ob["p"] = ob

    print(n_ob)
    with open(args[2],'w') as f2:
        json.dump(n_ob, f2, indent=2)