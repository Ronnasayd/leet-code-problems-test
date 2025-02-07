import requests
from decouple import config
import json
from time import sleep
from pprint import pprint
import argparse


parser = argparse.ArgumentParser(
    prog="generate-testes",
    description="generate tests from leetcode",
)
parser.add_argument("-l", "--language", default="py")
args = parser.parse_args()


cookies = {
    "csrftoken": config("CSRF_TOKEN"),
    "LEETCODE_SESSION": config("JWT_TOKEN"),
}

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "dnt": "1",
    "origin": "https://leetcode.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": config("URL"),
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-arch": '"x86"',
    "sec-ch-ua-bitness": '"64"',
    "sec-ch-ua-full-version": '"131.0.6778.139"',
    "sec-ch-ua-full-version-list": '"Google Chrome";v="131.0.6778.139", "Chromium";v="131.0.6778.139", "Not_A Brand";v="24.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Linux"',
    "sec-ch-ua-platform-version": '"6.8.0"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-csrftoken": config("CSRF_TOKEN"),
}

with open("online-input.txt") as file:
    data_input = file.read()
    data_input = data_input[: len(data_input) - 1]

if args.language == "cpp":
    with open("cpp/source.cpp") as file:
        typed_code = file.read().replace("class", "**class").split("**")[1]
        lang = "cpp"
else:
    with open("source.py") as file:
        typed_code = file.read().replace("class", "**class").split("**")[1]
        lang = "python3"

json_data = {
    "lang": lang,
    "question_id": config("QUESTION_ID"),
    "typed_code": typed_code,
    "data_input": data_input,
}

response = requests.post(
    f"{config("URL")}/interpret_solution/",
    cookies=cookies,
    headers=headers,
    json=json_data,
    allow_redirects=True,
)
data = json.loads(response.text)
if "error" in data:
    print(f'❌ {data["error"]}')
    exit(1)
test_cases = data["test_case"].split("\n")
interpret_id = data["interpret_id"]
flag = True
while flag:
    sleep(2)
    response = requests.get(
        f"https://leetcode.com/submissions/detail/{interpret_id}/check/",
        cookies=cookies,
        headers=headers,
        allow_redirects=True,
    )
    data = json.loads(response.text)
    if data["state"] == "SUCCESS":
        flag = False

if "runtime_error" in data:
    print(f'❌ {data["runtime_error"]}')
    exit(1)
total_testcases = int(data["total_testcases"])
step = len(test_cases) // total_testcases
aux = []
for i in range(0, len(test_cases), step):
    aux.append(test_cases[i : i + step])
test_cases = aux
stdout = [line for line in data["std_output_list"] if line != ""]
if len(stdout):
    test_cases = zip(
        test_cases, data["expected_code_answer"], data["code_answer"], stdout
    )
else:
    test_cases = zip(test_cases, data["expected_code_answer"], data["code_answer"])
for test_case in test_cases:
    if len(stdout):
        x, y, z, line = test_case
        print("Stdout:")
        print(line)
    else:
        x, y, z = test_case
    if y == "" and z == "":
        continue
    print(f"Input:{';'.join(x)}")
    print(f"Output:{y}")
