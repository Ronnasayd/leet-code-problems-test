from source import Solution
import json

inputs = []
outputs = []
name = "canPlaceFlowers"

with open("offline-input.txt") as file:
    data = file.read()
    lines = data.split("\n")
    for line in lines:
        if "input" in line.lower() and not line.startswith("#"):
            values = line.split(":")[1].split(";")
            v = []
            for value in values:
                if "=" in value:
                    value = value.split("=")[1]
                v.append(json.loads(value))
            inputs.append(v)
        if "output" in line.lower() and not line.startswith("#"):
            value = line.split(":")[1]
            outputs.append(json.loads(value))
for inp, out in zip(inputs, outputs):
    method = getattr(Solution(), name)
    original_inp = json.loads(json.dumps(inp))
    result = method(*inp)
    if result == out:
        print(f"✅ Input: {original_inp} => ({out}  ==  {result})")
    else:
        print(f"❌ Input: {original_inp} => ({out} !=  {result})")
