def composition(S, C):
    dic = {}
    C = "@{}.com".format(C)

    for key, value in enumerate(S):
        index = len(value)
        space = value.count(" ")
        acc = value.split(" ")
        val = "_".join(acc[-1:] + acc[:-1]).replace("-", "").lower()
        if space > 1:
            index = -(val[::-1].index("_")) + 1

        if val[:index] not in dic:
            dic[val[:index]] = 1
        else:
            dic[val[:index]] += 1

    ans = []
    for k, v in dic.items():
        if v > 1:
            for num in range(v):
                ans.append(k + str(num + 1) + C)
        else:
            ans.append(k + C)
    return ans


print(composition(["aa bb cc", "xx yy z-z", "aa bb", "aa bx cc"], "test"))
