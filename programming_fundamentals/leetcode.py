def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    common_letters = []
    for i in range(len(strs)):
        zelfde_letters = 0
        for woorden in strs:
            if len(woorden) > 0:
                if woorden[i] == strs[0][i]:
                    zelfde_letters += 1  
                else:
                    break
                if zelfde_letters == len(strs):
                    common_letters.append(strs[i][i])

    return "".join(common_letters)


strs = ["flower", "fli"]
print(longestCommonPrefix(strs))