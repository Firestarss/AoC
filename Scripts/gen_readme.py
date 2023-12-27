import requests
import re


def progressBar(iteration, total, length=25, fill="█", empty="-"):
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + empty * (length - filledLength)
    return bar


def progress_percent(iteration, total, decimals=1):
    percent = 100 * (iteration / float(total))
    if round(percent, 2).is_integer():
        percent = round(percent)
    else:
        percent = round(percent, decimals)

    return f"{percent}%".ljust(12)


if __name__ == "__main__":
    with open("secrets.txt", "r") as infile:
        session_id = infile.read().strip()

    cookies = {"session": session_id}

    response = requests.get(
        "https://adventofcode.com/events", cookies=cookies, headers={}
    )

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

    total_stars = []
    finished_years = []
    unfinished_years = []

    md_txt = "# Years #"
    md_txt += "\n\n| Year         | Stars | Progress Bar                                       | Percent Done |"
    md_txt += "\n|:------------:|:-----:|:---------------------------------------------------|:-------------|"

    for line in stars:
        if len(line) == 1:
            line.append("0")

        total_stars.append(int(line[1]))
        if int(line[1]) == 50:
            finished_years.append(line[0])
        else:
            unfinished_years.append((line[0], 50 - int(line[1])))

        md_txt += f"\n| [{line[0]}]({line[0]}) | {line[1].zfill(2):5} | {progressBar(int(line[1]), 50, 50, '*', ' ')} | {progress_percent(int(line[1]),50)} |"

    total_sum = sum(total_stars)
    md_txt += f"\n| {'Total'.ljust(12)} | {str(total_sum).ljust(5)} | {progressBar(total_sum, 50 * len(stars), 50, '*', ' ')} | {progress_percent(total_sum, 50 * len(stars))} |"

    progress_star_count = progressBar(total_sum, 50 * len(stars), 50, "*", " ").count(
        "*"
    )

    md_txt += f"\n\nEach star in the Total row represents roughly {round(total_sum / progress_star_count, 1)} stars"
    md_txt += "\n\n"


    md_txt += f"### Unfinished Years (Sorted by Remaining Stars) ###\n"
    md_txt += "\n| Year | Stars Needed |"
    md_txt += "\n|:----:|:-------------|"

    unfinished_years.sort(key=lambda a: a[1])
    unfinished_years.reverse()
    for year in unfinished_years:
        md_txt += f"\n| {year[0]} | {str(year[1]).ljust(12)} |"

    md_txt += "\n\n"

    md_txt += "### Finished Years ###\n\n"
    md_txt += ", ".join([str(x) for x in finished_years])

    md_txt += "\n"

    print(md_txt)

    with open("../Years/README.md", "w") as outfile:
        outfile.write(md_txt)
