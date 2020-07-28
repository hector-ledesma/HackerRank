def groupAnagrams(strs: [str]) -> [[str]]:
    lists = {}

    for word in strs:
        srt = ''.join(sorted(word))
        if srt in lists:
            lists[srt].append(word)
        else:
            lists[srt] = [word]

    res = []
    for result in lists.values():
        res.append(result)
    print(res)


groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])