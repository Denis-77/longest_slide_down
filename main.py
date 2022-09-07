def longest_slide_down(pyramid):
    max_level = len(pyramid) - 1
    level = max_level - 1
    while level >= 0:
        for index_elem, elem in enumerate(pyramid[level]):
            if pyramid[level + 1][index_elem] > pyramid[level + 1][index_elem + 1]:
                pyramid[level][index_elem] += pyramid[level + 1][index_elem]
            else:
                pyramid[level][index_elem] += pyramid[level + 1][index_elem + 1]
        level -= 1
    return pyramid[0][0]
