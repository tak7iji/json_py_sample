import json
import sys

args = sys.argv

with open(args[1]) as f1:
    ob = json.load(f1)

    n_ob = {"p":{}}
    n_ob["p"]["a"] = ob["a"]
    n_ob["p"]["d"] = ob["d"]

    print(n_ob)
    with open(args[2],'w') as f2:
        json.dump(n_ob, f2, indent=2)