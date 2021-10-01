def str_to_ascii_list(S: str) -> list:
    return [ord(c) for c in S]

def ascii_list_to_str(L: list) -> str:
    return ''.join([chr(x) for x in L])