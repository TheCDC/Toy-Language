from pprint import pprint
import re


def is_definition_line(s):
    return not(s.startswith("#") or len(s.strip()) == 0)


def parse_line(s):
    s = s.strip()
    idx = s.find("=")
    name = s[:idx].strip()
    definition = '(?P<{}>{})'.format(name, s[idx + 1:].strip())
    return {name: definition}


def parse_file(fname):
    definition_pairs = {}
    with open(fname) as f:
        for line in f:
            if is_definition_line(line):
                definition_pairs.update(parse_line(line))
            else:
                continue
    return definition_pairs

definitions = parse_file("specification.txt")
