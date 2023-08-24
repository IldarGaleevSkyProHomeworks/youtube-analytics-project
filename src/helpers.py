import json


def printj(dict_to_print: dict) -> None:
    """printing Human-friendly json"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
