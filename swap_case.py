# SWAP CASE 
"""
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2 

"""



def swap_case(s):
    result = ""
    for ch in s:
        if ch.islower():
            result = result + ch.upper()

        else:
            result = result + ch.lower()

    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

