from source import Solution
import json

inputs = []
outputs = []
name = "middleNode"

with open("offline-input.txt") as file:
    data = file.read()
    lines = data.split("\n")
    for line in lines:
        if "input" in line.lower():
            value = line.split(":")[1]
            if "=" in value:
                value = value.split("=")[1]
            inputs.append(json.loads(value))
        if "output" in line.lower():
            value = line.split(":")[1]
            if "=" in value:
                value = value.split("=")[1]
            outputs.append(json.loads(value))
for inp, out in zip(inputs, outputs):
    method = getattr(Solution(), name)
    if method(inp) == out:
        print(f"✅ input:{inp} => (output:{out} |  output:{method(inp)})")
    else:
        print(f"❌  input:{inp} => (output:{out} |  output:{method(inp)})")
