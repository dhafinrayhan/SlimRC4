from tools import ascii_list_to_str, str_to_ascii_list

SIZE = 256


def slimrc4(P, K: str, decrypt=False) -> str:

    # Convert P and K to array of their ascii value representatives
    P = str_to_ascii_list(P)
    K = str_to_ascii_list(K)

    C = []

    # Initialize of S array
    S = [i for i in range(SIZE)]

    # Permute values in S
    j = 0
    k = 0
    len_K = len(K)
    for i in range(SIZE):
        # Cycle S[i], S[j], S[k] instead of only swapping two of them
        # This is what differ from the original RC4
        j = (j + S[i] + K[i % len_K]) % SIZE
        k = (k + S[j] + K[j % len_K]) % SIZE
        S[i], S[j], S[k] = S[j], S[k], S[i]  # cycle S[i], S[j], S[k]

    # PRGA
    i = 0
    j = 0
    for idx in range(len(P)):
        # Also cycle S[i], S[j], S[k] here
        i = (i + 1) % SIZE
        j = (j + S[i]) % SIZE
        k = (k + 2 * S[i] + S[j]) % SIZE
        S[i], S[j], S[k] = S[j], S[k], S[i]  # cycle S[i], S[j], S[k]
        t = (S[i] + S[j] + S[k]) % SIZE
        u = S[t]
        c = u ^ P[idx]
        C.append(c)

    return ascii_list_to_str(C)
