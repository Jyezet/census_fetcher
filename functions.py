from time import sleep
from requests import get
from json import dumps, loads
from xmltodict import parse
from collections import OrderedDict

def form_useragent(ua):
    ua = ua.lower()
    return f"Automatic census data fetching script (Which requests influence census data), created by: nation=jyezet and in use by: nation={ua}"

def sanitize_dict(arg: dict):
    arg = dumps(arg)
    arg = loads(arg)
    return arg

def clean_dict(arg: dict):
    return_data = []
    temp_list = []
    for x in arg:
        temp_list.append(x["REGION"]["CENSUSRANKS"]["NATIONS"]["NATION"])
    for packed_list in temp_list:
        for individual_nation in packed_list:
            return_data.append(individual_nation)
    return return_data

def calc_num(reg_num, /, *, useragent):
    sleep(0.7)
    url_num = f"https://www.nationstates.net/cgi-bin/api.cgi?region={reg_num}&q=numnations"
    req = get(url_num, headers={"User-Agent": useragent})
    if "404 Not Found" in req.text:
        raise ValueError(f"'{reg_num}' Region not found, you nerd.")
    return int(sanitize_dict(parse(req.text))["REGION"]["NUMNATIONS"])