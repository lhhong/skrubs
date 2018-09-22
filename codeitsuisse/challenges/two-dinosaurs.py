#modulo = 100000123
#
#class Node(object):
#    def __init__(self, start, end):
#        self.start = start
#        self.end = end
#        self.total = 0
#        self.left = None
#        self.right = None
#
#
#class NumArray(object):
#    def __init__(self, nums):
#        """
#        initialize your data structure here.
#        :type nums: List[int]
#        """
#        #helper function to create the tree from input array
#        def createTree(nums, l, r):
#
#            #base case
#            if l > r:
#                return None
#
#            #leaf node
#            if l == r:
#                n = Node(l, r)
#                n.total = nums[l][1]
#                return n
#
#            mid = (l + r) // 2
#
#            root = Node(l, r)
#
#            #recursively build the Segment tree
#            root.left = createTree(nums, l, mid)
#            root.right = createTree(nums, mid+1, r)
#
#            #Total stores the sum of all leaves under root
#            #i.e. those elements lying between (start, end)
#            root.total = (root.left.total + root.right.total) % modulo
#
#        return root
#
#    self.root = createTree(nums, 0, len(nums)-1)
#
#    def update(self, i, val):
#        """
#        :type i: int
#        :type val: int
#        :rtype: int
#        """
#        #Helper function to update a value
#        def updateVal(root, i, val):
#
#            #Base case. The actual value will be updated in a leaf.
#            #The total is then propogated upwards
#            if root.start == root.end:
#                root.total = val
#                return val
#
#            mid = (root.start + root.end) // 2
#
#            #If the index is less than the mid, that leaf must be in the left subtree
#            if i <= mid:
#                updateVal(root.left, i, val)
#
#            #Otherwise, the right subtree
#            else:
#                updateVal(root.right, i, val)
#
#            #Propogate the changes after recursive call returns
#            root.total = (root.left.total + root.right.total) % modulo
#
#            return root.total
#
#        return updateVal(self.root, i, val)
#
#    def sumRange(self, i, j):
#        """
#        sum of elements nums[i..j], inclusive.
#        :type i: int
#        :type j: int
#        :rtype: int
#        """
#        #Helper function to calculate range sum
#        def rangeSum(root, i, j):
#
#            #If the range exactly matches the root, we already have the sum
#            if root.start == i and root.end == j:
#                return root.total
#
#            mid = (root.start + root.end) // 2
#
#            #If end of the range is less than the mid, the entire interval lies
#            #in the left subtree
#            if j <= mid:
#                return rangeSum(root.left, i, j)
#
#            #If start of the interval is greater than mid, the entire inteval lies
#            #in the right subtree
#            elif i >= mid + 1:
#                return rangeSum(root.right, i, j)
#
#            #Otherwise, the interval is split. So we calculate the sum recursively,
#            #by splitting the interval
#            else:
#                return (rangeSum(root.left, i, mid) + rangeSum(root.right, mid+1, j)) % modulo
#
#        return rangeSum(self.root, i, j)
from collections import defaultdict

def evaluate(inputVal):
    print(inputVal)
    A = inputVal["calories_for_each_type_for_raphael"]
    B = inputVal["calories_for_each_type_for_leonardo"]
    diff = inputVal["maximum_difference_for_calories"]
    modding = 100000123

    def getPossibleSumsWithCount(arr):
        d = defaultdict(int)
        d[0] = 1
        for a in arr:
            new_d = defaultdict(int)
            for s in d:
                new_d[s+a] += d[s]
                new_d[s] += d[s]
                #if s+a not in new_d:
                #    new_d[s+a] = d[s]
                #else:
                #    new_d[s+a] += d[s]
                #if s not in new_d:
                #    new_d[s] = d[s]
                #else:
                #    new_d[s] += d[s]
            d = new_d
        return d

    aPoss = getPossibleSumsWithCount(A)
    bPoss = getPossibleSumsWithCount(B)

    print('enumerated')

    a = sorted([(k, v) for k, v in aPoss.items()])
    b = sorted([(k, v) for k, v in bPoss.items()])

    print("sorted")
    lPtr = -1
    rPtr = -1

    total = 0
    pSum = 0
    for k, v in a:
        while lPtr < len(b) and (lPtr < 0 or (k - b[lPtr][0]) > diff):
            if lPtr >= 0:
                pSum -= b[lPtr][1]
                pSum %= modding
            lPtr += 1
        while rPtr < (len(b) - 1) and (b[rPtr + 1][0] - k) <= diff:
            rPtr += 1
            pSum += b[rPtr][1]
            pSum %= modding

        total += (pSum * v) % modding
        total %= modding

    return {"result": total}

    #aSum = sum(A)
    #bSum = sum(B)

    #A_table = {}
    #B_table = {}

    #def srA(h, v):
    #    A_table[h] = v
    #    return v

    #def srB(h, v):
    #    B_table[h] = v
    #    return v

    #def findNoCombi(i, d, array, sr, table):
    #    h = (i, d)
    #    if h in table:
    #        return table[h]

    #    if i < -1:
    #        return sr(h, 0)

    #    if d == 0:
    #        return sr(h, 1)

    #    if d < 0:
    #        return sr(h, 0)

    #    combi = sum([
    #        findNoCombi(i-1, d, array, sr, table),
    #        findNoCombi(i-1, d-array[i], array, sr, table)
    #    ])
    #    combi %= modding

    #    return sr(h, combi)

    #result = 0
    #BB = {}
    #for i in range(bSum+1 + 2 * diff):
    #    BB[i-diff] = 0
    #    if i <= bSum:
    #        BB[i-diff] += findNoCombi(len(B) - 1, i, B, srB, B_table)
    #        BB[i-diff] %= modding
    #    if i != 0:
    #        BB[i-diff] += BB[i-diff-1]
    #        BB[i-diff] %= modding
    #    if i > 2 * diff:
    #        BB[i-diff] -= findNoCombi(len(B) - 1, i-2*diff-1, B, srB, B_table)
    #        BB[i-diff] %= modding

    #for i in range(aSum+1):
    #    aRes = findNoCombi(len(A)-1, i, A, srA, A_table)
    #    result += aRes * BB[i]

    #    #for j in range(i-diff, i+diff + 1):

    #    #    abRes = aRes * findNoCombi(len(B)-1, j, B, srB, B_table)
    #    #    result += abRes
    #    #    result %= modding

    #return {"result": result}

#    dp_table = {}
#
#    def sr(h, v):
#        dp_table[h] = v
#        return v
#
#    def findNoCombi(aI, bI, d):
#        h = (aI, bI, d)
#        if h in dp_table:
#            return dp_table[h]
#
#        if aI < -1 or bI < -1:
#            return sr(h, 0)
#
#        if aI < 0 and bI < 0:
#            if d == 0:
#                return sr(h, 1)
#            else:
#                return sr(h, 0)
#
#        if aI < 0 or bI < 0:
#            if d == 0:
#                return sr(h, 1)
#
#        combi = sum([
#            findNoCombi(aI-1, bI, d),
#            findNoCombi(aI-1, bI, d-A[aI]),
#            findNoCombi(aI, bI-1, d),
#            findNoCombi(aI, bI-1, d+A[bI]),
#        ])
#        combi %= modding
#
#        return sr(h, combi)
#
#    result = 0
#    for i in range(-diff, diff):
#        result += findNoCombi(len(A)-2, len(A)-2, i)
#        result %= modding
#
#    return {"result": result}

tests = [
    {
        "number_of_types_of_food" : 2,
        "calories_for_each_type_for_raphael" : [4,5],
        "calories_for_each_type_for_leonardo" :  [3,6],
        "maximum_difference_for_calories": 3
    },
    {'number_of_types_of_food': 40, 'calories_for_each_type_for_raphael': [1928, 1716, 1810, 1723, 1506, 1943, 1996, 1874, 1930, 1826, 1629, 1530, 1729, 1924, 1680, 1990, 1812, 1831, 1686, 1574, 1706, 1938, 1655, 1871, 1644, 1880, 1601, 1569, 1959, 1651, 1510, 1809, 1607, 1721, 1815, 1818, 1600, 1856, 1811, 1998], 'calories_for_each_type_for_leonardo': [1634, 1934, 1876, 1974, 1780, 1604, 1905, 1598, 1775, 1808, 1663, 1878, 1917, 1552, 1531, 1563, 1962, 1541, 1788, 1944, 1641, 1792, 1501, 1657, 1687, 1512, 1670, 1901, 1793, 1910, 1992, 1921, 1830, 1744, 1683, 1884, 1766, 1829, 1619, 1645], 'maximum_difference_for_calories': 2236},
    {'number_of_types_of_food': 200, 'calories_for_each_type_for_raphael': [1690, 1800, 1651, 1852, 1819, 1936, 1842, 1842, 1898, 1779, 1686, 1922, 1527, 1633, 1734, 1689, 1592, 1592, 1508, 1537, 1852, 1852, 1709, 1812, 1561, 1856, 1746, 1982, 1690, 1538, 1681, 1640, 1910, 1838, 1910, 1871, 1943, 1804, 1596, 1804, 1633, 1921, 1521, 1644, 1541, 1795, 1607, 1935, 1731, 1608, 1763, 1567, 1558, 1536, 1606, 1634, 1572, 1854, 1645, 1536, 1834, 1836, 1734, 1907, 1872, 1554, 1568, 1885, 1806, 1707, 1819, 1724, 1942, 1797, 1745, 1611, 1791, 1694, 1762, 1582, 1919, 1821, 1559, 1987, 1538, 1943, 1768, 1686, 1986, 1594, 1833, 1826, 1635, 1854, 1578, 1602, 1674, 1704, 1832, 1551, 1820, 1973, 1569, 1792, 1731, 1962, 1757, 1510, 1617, 1844, 1607, 1924, 1970, 1530, 1830, 1599, 1829, 1628, 1503, 1913, 1608, 1621, 1989, 1735, 1710, 1825, 1920, 1838, 1904, 1667, 1698, 1975, 1870, 1675, 1860, 1938, 1634, 1681, 1889, 1873, 1897, 1807, 1893, 1648, 1603, 1840, 1695, 1822, 1532, 1999, 1991, 1642, 1856, 1795, 1564, 1554, 1875, 1625, 1972, 1956, 1928, 1716, 1810, 1723, 1506, 1943, 1996, 1874, 1930, 1826, 1629, 1530, 1729, 1924, 1680, 1990, 1812, 1831, 1686, 1574, 1706, 1938, 1655, 1871, 1644, 1880, 1601, 1569, 1959, 1651, 1510, 1809, 1607, 1721, 1815, 1818, 1600, 1856, 1811, 1998], 'calories_for_each_type_for_leonardo': [1926, 1811, 1603, 1981, 1624, 1981, 1780, 1761, 1938, 1922, 1521, 1992, 1526, 1866, 1544, 1864, 1502, 1986, 1700, 1813, 1599, 1735, 1936, 1764, 1795, 1838, 1829, 1786, 1516, 1567, 1675, 1893, 1612, 1953, 1755, 1691, 1751, 1836, 1726, 1774, 1850, 1545, 1816, 1745, 1528, 1831, 1527, 1515, 1829, 1504, 1663, 1637, 1737, 1812, 1689, 1863, 1722, 1845, 1954, 1661, 1975, 1503, 1919, 1899, 1531, 1618, 1539, 1824, 1616, 1960, 1918, 1877, 1608, 1549, 1652, 1651, 1854, 1740, 1930, 1770, 1655, 1637, 1533, 1685, 1795, 1565, 1938, 1724, 1681, 1974, 1642, 1856, 1953, 1542, 1748, 1590, 1710, 1806, 1543, 1664, 1872, 1901, 1588, 1876, 1693, 1643, 1796, 1667, 1852, 1873, 1549, 1552, 1768, 1908, 1830, 1959, 1837, 1569, 1830, 1827, 1627, 1657, 1591, 1960, 1521, 1771, 1844, 1778, 1528, 1741, 1656, 1662, 1530, 1979, 1705, 1859, 1976, 1559, 1782, 1674, 1913, 1792, 1854, 1522, 1595, 1785, 1659, 1502, 1922, 1708, 1564, 1817, 1537, 1769, 1518, 1870, 1703, 1718, 1727, 1943, 1634, 1934, 1876, 1974, 1780, 1604, 1905, 1598, 1775, 1808, 1663, 1878, 1917, 1552, 1531, 1563, 1962, 1541, 1788, 1944, 1641, 1792, 1501, 1657, 1687, 1512, 1670, 1901, 1793, 1910, 1992, 1921, 1830, 1744, 1683, 1884, 1766, 1829, 1619, 1645], 'maximum_difference_for_calories': 22236}
]

