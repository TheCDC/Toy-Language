import parse_specification


def parse_code(s, rules):
    r = '|'.join(rules.values())
    print(r)
    return re.finditer(r, s)


print(definitions)

s = """xyz = 0897522345;"""

pprint(list(i for i in parse_code(s, definitions)))
