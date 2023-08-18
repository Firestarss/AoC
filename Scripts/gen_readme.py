import requests
import re

def progressBar (iteration, total, decimals = 0, length = 25, fill = '█', empty = '-', show_percent = True):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total))).rjust(4)
    if iteration == total: percent = "100".rjust(4)
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + empty * (length - filledLength)
    output = bar
    if show_percent: output += f" {percent}%"
    return output

if __name__ == "__main__":

    with open("secrets.txt", "r") as infile:
        session_id = infile.read().strip()

    cookies = {
        "session": session_id
    }

    response = requests.get("https://adventofcode.com/events", cookies=cookies, headers={})

    if response.status_code != 200:
        print(f"ERROR: {response.status_code}")
        print(response.reason)
        print(response.text)
        exit()

    stars = response.text[response.text.find("<main>") : response.text.find("</main>")]
    stars = stars[stars.find("</p>") + 5 : -1]
    stars = stars.replace('<div class="eventlist-event">', "")
    stars = re.sub("<.*?>|\(.*?\)|\s\s+|\*", "", stars)
    stars = [re.findall("\d+", line) for line in stars.splitlines()][:-1]

    total_sum = 0

    md_txt = "# AoC\n\nThis Repo contains my code for completing the Advent of Code challenges. "
    md_txt += "It is not clean or polished and is probably incomplete. Have fun exploring if you like."
    md_txt += "\n\n| Year         | Stars | Percentage Complete                                      |"
    md_txt +=   "\n|--------------|:-----:|----------------------------------------------------------|"

    for line in stars:
        if len(line) == 1:
            line.append("0")

        total_sum += int(line[1])

        md_txt += f"\n| [{line[0]}]({line[0]}) | {line[1].zfill(2):5} | {progressBar(int(line[1]), 50, 0, 50, '*', ' ')} |"

    md_txt += f"\n| {'Total'.ljust(12)} | {str(total_sum).ljust(5)} | {progressBar(total_sum, 50 * len(stars), 1, 50, '█', ' ')} |"
    md_txt += "\n"

    with open("../README.md", "w") as outfile:
        print(outfile.write(md_txt))