def max_distance(A, B, C, D):
    # 將四個input儲存在list內
    l = [A, B, C, D]
    # 利用Python內建的Timesort將list排序，時間複雜度為O(nlogn)
    l = sorted(l)
    # 排序後list內第一個與第四個數值相差最大，個別作為兩點的x座標
    # 另外list內第二、三個則個別作為兩點的y座標
    # 這兩點的距離平方就會是最大值
    return (l[0] - l[3]) ** 2 + (l[1] - l[2]) ** 2


def max_subarray(A, K, L):
    # 給定list後，此function負責找出連續win個整數加總起來最大的值
    # 若有找到則return最大值以及該連續整數之起始位置和終止位置
    # 若找不到則return 0以及空陣列
    # 此function有用到Sliding Window之概念
    def max_value(S, win):

        # 如果給定list之長度小於要找的win個連續整數則return 0以及空陣列
        if len(S) < win:
            return 0, []

        # 定義window的起始位置、目前加總值以及最終最大值
        start = max_ending_here = max_so_far = 0
        # window之起始位置和終止位置
        max_index = []

        for k, v in enumerate(S):
            # 依序將元素加總
            max_ending_here += v

            # 如果加總範圍大於window大小，則減去window內最前面的數值
            # 並將起始位置往前挪一格
            if k - start + 1 > win:
                max_ending_here -= S[start]
                start += 1

            # 若目前加總值大於最終最大值，則將其取代，並記錄目前window之位置
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                max_index = [start, k]

        # 回傳最終數據
        return max_so_far, max_index

    # 找出完整陣列內連續K個整數加總之最大值以及該範圍之起始、終止位置
    max_1, index = max_value(A, K)

    # 利用Divide and Conquer的概念將原始陣列切分成兩個陣列（兩者皆不包含上一步找到的區間範圍）
    # 兩者分別去找出連續L個整數加總之最大值
    max_2, x = max_value(A[0: index[0]], L)
    max_3, y = max_value(A[index[1] + 1: len(A)], L)

    # 驗證K以及L皆有找到最大值，若有找到則return加總，任意一個沒有則return -1
    if max_1 and (max_2 or max_3):
        return max_1 + max(max_2, max_3)
    else:
        return -1


def capital_distance(T):
    target = 0  # 首都
    neighbor = dict()  # 附近鄰居（可以直接到達）
    visited = set()  # 已經拜訪
    distance = []  # 到達首都之距離（城市個數）
    size = len(T) - 1  # 最後回傳陣列之大小

    # 找出首都
    for k, v in enumerate(T):
        if v == T[v]:
            target = v
            break

    # 建立附近鄰居(直達路線)之字典，以減少時間複雜度
    for k, v in enumerate(T):
        if not neighbor.get(v):
            neighbor[v] = set()
        neighbor[v].add(k)
    neighbor[target].remove(target)

    # 從首都開始依序拜訪
    # 首都附近的鄰居距離為1，並記錄在distance內
    # 尋找首都鄰居的鄰居，所以其距離首都為2，也記錄在distance內
    # 依此類推，將距離首都為3,4,5...之城市數量記錄在distance內
    visited.add(target)
    while visited and len(distance) < size:
        next_visit = [item for i in visited if i in neighbor for item in neighbor[i]]
        distance.append(len(next_visit))
        visited = next_visit

    # 將遺漏值補0，直到符合回傳陣列之大小
    while len(distance) < size:
        distance.append(0)

    return distance


print("--------------Solution 1--------------")
print(max_distance(9, 5, 2, 7))
print(max_distance(1, 1, 2, 3))
print(max_distance(2, 4, 2, 4))

print("--------------Solution 2--------------")
print(max_subarray([6, 1, 4, 6, 3, 2, 7, 4], 3, 2))
print(max_subarray([10, 19, 15], 2, 2))
print(max_subarray([5, 2, 3, 8, 1, 3, 7], 3, 2))
print(max_subarray([10, 6, 5, 3, 9, 7, 1], 3, 3))
print(max_subarray([1, 7, 9, 3, 5, 6, 10], 3, 3))
print(max_subarray([20, 30, 70, 10], 2, 2))

print("--------------Solution 3--------------")
print(capital_distance([9, 1, 4, 9, 0, 4, 8, 9, 0, 1]))
print(capital_distance([5, 7, 9, 9, 4, 1, 1, 8, 4, 1]))
