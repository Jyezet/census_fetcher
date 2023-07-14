from requests import get
from xmltodict import parse
from time import sleep
from json import dumps
from functions import form_useragent, sanitize_dict, calc_num, clean_dict

def main():
    useragent = form_useragent(input("Useragent:\n"))
    region = input("Region to fetch from:\n")
    url_inf = f"https://www.nationstates.net/cgi-bin/api.cgi?region={region}&q=censusranks;scale=65;start="
    influence = []
    nations_per_request = 20
    number_of_nations = calc_num(region, useragent=useragent)

    for x in range(1, number_of_nations, nations_per_request):
        try:
            req = get(url_inf + str(x), headers={"User-Agent": useragent})
            influence.append(parse(req.text))
            print(f"Fetched with start={x}")
            sleep(0.7)
        except Exception as e:
            print(f"Couldn't fetch for {x}, HTTP {req.status_code}, Exception: {repr(e)}")
            sleep(0.7)
            continue

    influence = sanitize_dict(influence)
    influence = clean_dict(influence)
    filename = input("Done! Type the name for the data dump:\n")
    with open(f"{filename}.json", "w+") as f:
        f.write(dumps(influence))

if __name__ == "__main__":
    main()