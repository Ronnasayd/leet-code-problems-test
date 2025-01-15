import json
from time import time
import os, psutil

inputs = []
answers = []

process_input = []
process_output = []

# process_input = [[[0], list2tree, TreeNode]]
# process_output = [[tree2list]]

with open("../offline-input.txt") as file:
    data = file.read()
    data = data.replace(", ", ";")
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
            answers.append(json.loads(value))
with open("inputs.txt", "w") as file:
    s = ""
    for inp in inputs:
        for i in inp:
            s += f'{str(i) + "\n"}'
    file.write(s[: len(s) - 1])
with open("answers.txt", "w") as file:
    for answer in answers:
        file.write(f'{str(answer) + "\n"}')
os.system("g++ -o main main.cpp")
initial_time = time()
os.system("./main")
time_to_process = time() - initial_time
with open("outputs.txt") as file:
    outputs = file.read().split("\n")
total_time = 0
total_memory = 0
for inp, out, ans in zip(inputs, outputs, answers):
    original_inp = str(json.loads(json.dumps(inp)))
    if len(original_inp) > 60:
        original_inp = original_inp[:60] + "..."

    total_time += time_to_process
    if time_to_process > 10:
        print(f"❌ (Time limit exceded)", end=" ")
    if ans == out:
        print(
            f"✅ Input: {original_inp} => ({out}  ==  {ans}) | {time_to_process*1000:.5f} ms"
        )
    else:
        print(
            f"❌ Input: {original_inp} => ({out} !=  {ans}) | {time_to_process*1000:.5f} ms"
        )
total_memory = psutil.Process(os.getpid()).memory_info().rss / 1024**2
print(f"⌛ Total time: {total_time*1000:.5f} ms")
print(f"💾 Memory usage: {total_memory} MB")
