from source import *
import json
from time import time
import os, psutil
from utils import *
import sys

args = sys.argv

inputs = []
outputs = []
method_name = [attr for attr in dir(Solution) if not attr.startswith("__")][0]

process_input = []
process_output = []

# process_input = [[[0], list2tree, TreeNode]]
# process_output = [[tree2list]]

with open("offline-input.txt", encoding="utf-8") as file:
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
            outputs.append(json.loads(value))
total_time = 0
total_memory = 0
for inp, out in zip(inputs, outputs):
    method = getattr(Solution(), method_name)
    original_inp = str(json.loads(json.dumps(inp)))
    if len(original_inp) > 60:
        original_inp = original_inp[:60] + "..."
    initial_time = time()
    if process_input:
        for process in process_input:
            for index in process[0]:
                inp[index] = process[1](inp[index], *process[2:])
        result = method(*inp)
        if process_output:
            for process in process_output:
                result = process[0](result, *process[1:])
    else:
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
print(f"💾 Memory usage: {total_memory} MB")

if len(args) > 1 and args[1] == "-r":
    with open("offline-input.txt", "w", encoding="utf-8") as file:
        for inp, out in zip(inputs, outputs):
            s = "Input: "
            for i in inp:
                s += f"{i};"
            s += f"\nOutput: {out}\n\n"
            s = s.replace(" ", "", -1).replace(";\n", "\n")
            s = s.replace("'", '"')
            file.write(s)
    s = ""
    with open("online-input.txt", "w", encoding="utf-8") as file:
        for inp in inputs:
            for i in inp:
                s += f"{i}\n"
        s = s.replace(" ", "", -1)
        s = s.replace("'", '"')
        file.write(s)
