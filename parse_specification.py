from pprint import pprint


def parse_file(fname):
    definitions = {}
    with open(fname) as f:
        for line in f:
            s = line.strip()
            if s.startswith("#") or len(s.strip()) == 0:
                continue
            else:
                # print(line)
                idx = s.find("=")
                name = s[:idx].strip()
                # wrap each definition with parens for nesting
                definition = "(" + s[idx + 1:].strip() + ")"
                print(name, definition)
                definitions.update({name: definition})
    return definitions


definitions = parse_file("specification.txt")
pprint(definitions)

print(definitions["body"].format(**definitions))


def test_parse_file():
    cases = [
    """x = 10

    """,
    ]