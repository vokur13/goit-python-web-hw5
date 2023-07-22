import pprint


def pretty_view(data):
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False, depth=None, compact=True)
    pp.pprint(data)
