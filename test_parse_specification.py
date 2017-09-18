import parse_specification
import re


# def test_parse_statements():
#     cases = [
#         """x = 10;""",
#         """y = 10;""",
#     ]

#     for c in cases:
#         assert len(re.findall(
#             parse_specification.definitions['statement'], c)) == 1


def test_parse_identifiers():
    cases = [
        "xyz = 0897522345;",
        "abcdefg = -9876787654323;",
        "foo = 98765678;",
        "bar = 345678765;",
    ]
    for c in cases:
        found = re.findall(parse_specification.definitions['identifier'], c)
        assert found[0] == c.split('=')[0].strip()


def test_parse_literals():
    # first round sanity check, does parse bare numbers as numbers?
    cases = [
        "10",
        "-10",
        "1234567890",
        "-100",
        "-1000",
        "-1000099999999",
    ]
    for c in cases:
        found = re.findall(parse_specification.definitions[
            "literal"], c)
        assert found[0] == c
    # now try numbers on rhs of expr
    cases = [
        "x = 10;",
        "x =14;",
        "wiuefbkwnjr = 10;",
        "owi9876efn98765__ = -9876;",
        "x = 0;",
        "x= 0;",
        "weghrtjrfds=0;",
    ]
    for c in cases:
        assert re.findall(parse_specification.definitions[
                          "literal"], c)[0] == c.split('=')[1].split(';')[0].strip()
