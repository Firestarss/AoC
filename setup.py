import requests
from datetime import datetime, timedelta
import subprocess
import json

if __name__ == "__main__":
    day = datetime.today().day + 1
    pwd = subprocess.check_output(["pwd"]).decode().strip()

    with open("secrets.json", "r") as secret_file:
        secrets = json.load(secret_file)
    
    subprocess.run("cp -r " + pwd + "/Base " + pwd + "/Day" + str(day).zfill(2), shell=True)

    print("Running...")
    file_written = False
    start = datetime.now()
    while not file_written:
        now = datetime.now()
        if (now-start).seconds > 10:
            print("Still Running...")
            start = now
        if now.hour == 0 and now.second > 5:
            input_page = "https://adventofcode.com/%s/day/%s/input" %(str(now.year), str(now.day))
            response = requests.get(input_page, cookies={"session":secrets["session_cookie"]})
    
            with open(pwd + "/Day" + str(now.day).zfill(2) + "/input.txt", "w") as output_file:
                output_file.write(response.text.strip())

            
            print(response.text)
            file_written = True