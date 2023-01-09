def odd_even_str(input_str : str):
    """
        Task:
            Given a string, S, of length N that is indexed from 0 to N-1,
            print its even-indexed and odd-indexed characters as 2 space-separated
            strings on a single line.

        Notes: 0 is considered to be an even index.
    """
    even_str, odd_str = str(), str()
    for i in range(0, len(input_str)):
        if i % 2 == 0:
            even_str += input_str[i]
        else:
            odd_str += input_str[i]
    print(even_str, odd_str)

if __name__ == '__main__':
    input_int = int(input().strip())
    i = 0
    while i < input_int:
        input_str = str(input().strip())
        odd_even_str(input_str)
        i += 1