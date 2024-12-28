from source import Solution
import json
from time import time
import os, psutil

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
total_time = 0
total_memory = 0
for inp, out in zip(inputs, outputs):
    method = getattr(Solution(), method_name)
    original_inp = str(json.loads(json.dumps(inp)))
    if len(original_inp) > 60:
        original_inp = original_inp[:60] + "..."
    initial_time = time()
    result = method(*inp)
    time_to_process = time() - initial_time
    total_time += time_to_process
    if time_to_process > 10:
        print(f"❌ (Time limit exceded)", end=" ")
    if result == out:
        print(
            f"✅ Input: {original_inp} => ({out}  ==  {result}) | {time_to_process*1000:.5f} ms"
        )
    else:
        print(
            f"❌ Input: {original_inp} => ({out} !=  {result}) | {time_to_process*1000:.5f} ms"
        )
total_memory = psutil.Process(os.getpid()).memory_info().rss / 1024**2
print(f"⌛ Total time: {total_time*1000:.5f} ms")
print(f"⌛ Memory usage: {total_memory} MB")
