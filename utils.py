import json

def load_date(path):
    with open (path, encoding="utf-8") as file:
        data = json.load(file)
    return data

def lates_take(list):
    list_sort = sorted(list, key=lambda x: x.get('date', "0000-00-00T00:00:00.000000"), reverse=True)
    i = 0
    list_work = []
    while i < 5:
        if list_sort[i]["state"] == "EXECUTED":
            list_work.append(list_sort[i])
            i += 1
        else:
            del(list_sort[i])
    return list_work

def print_oper(dict):
    output = ""
    if "date" in dict.keys():
        output += f"{dict['date'][8:10]}.{dict['date'][5:7]}.{dict['date'][:4]} "

    output += dict['description']

    if "from" in dict.keys():
        from_ = dict["from"].split(" ")
        index = 0
        for i in range(len(from_)):
            if from_[i].isdigit():
                index = i
                break
        output += "\n"
        output += f"{' '.join(from_[0:index])}"
        output += f" {from_[index][:4]} {from_[index][5:7]}** {'*' * 4} {from_[index][-4:]} "

    output += f" -> Счет **{dict['to'][-4:]}"

    output += "\n"
    output += f"{dict['operationAmount']['amount']} {dict['operationAmount']['currency']['name']}"
    return output