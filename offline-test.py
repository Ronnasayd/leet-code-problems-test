from source import Solution
import json

inputs = []
outputs = []
method_name = [attr for attr in dir(Solution) if not attr.startswith("__")][0]

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
    method = getattr(Solution(), method_name)
    original_inp = str(json.loads(json.dumps(inp)))
    if len(original_inp) > 60:
        original_inp = original_inp[:60] + "..."
    result = method(*inp)
    if result == out:
        print(f"✅ Input: {original_inp} => ({out}  ==  {result})")
    else:
        print(f"❌ Input: {original_inp} => ({out} !=  {result})")
