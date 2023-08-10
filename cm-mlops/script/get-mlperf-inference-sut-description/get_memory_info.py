import os
import json
from dmiparser import DmiParser

with open("meminfo.out", "r") as f:
    text = f.read()
    parser = DmiParser(text, sort_keys=True, indent=4)

    parsedStr = str(parser)
    parsedObj = json.loads(str(parser))
    memory = []

    ind = 0;
    needed_global_keys = ['Speed', 'Configured Memory Speed', 'Type']
    added_global_keys = []
    needed_keys = ['Size', 'Rank']

    for item in parsedObj:
        if item['name'] == 'Physical Memory Array':
            ecc_value = item['props']['Error Correction Type']['values'][0]
            if not ecc_value or 'None' in ecc_value:
                ecc_value = "No ECC"
            memory.append({"info": ['Error Correction Type: ' +  ecc_value ]})
            ind += 1
            continue
        if item['name'] != 'Memory Device':
            continue
        memory.append({})
        memory[ind]['handle'] = item['handle']
        memory[ind]['info'] = []
        locator = item['props']['Locator']['values'][0]
        bank_locator = item['props']['Bank Locator']['values'][0]

        if not "Not Specified" in locator:
            memory[ind]['info'].append(locator)
        if not "Not Specified" in bank_locator:
            memory[ind]['info'].append(bank_locator)

        if item['props']['Size']['values'][0] == "No Module Installed":
            memory[ind]['populated'] = False
            memory[ind]['info'].append("Unpopulated")
        else:
            memory[ind]['populated'] = True

        for key in item['props']:
            if key in needed_global_keys and key not in added_global_keys:
                memory[0]['info'].append(f'{key}: {";".join(item["props"][key]["values"])}')
                added_global_keys.append(key)
            elif key in needed_keys:
                memory[ind]['info'].append(f'{key}: {";".join(item["props"][key]["values"])}')
        ind+=1

    meminfo = []
    for item in memory:
        meminfo.append( "; ".join(item['info']))
    
    meminfo_string =",   ".join(meminfo)
    with open("tmp-run-env.out", "w") as f:
        f.write(f"CM_HOST_MEM_INFO={meminfo_string}")

