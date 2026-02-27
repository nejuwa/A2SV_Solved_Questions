class Solution:
    def pancakeSort(self, arr):
        res = []
        n = len(arr)

        for size in range(n, 1, -1):

            max_index = arr.index(size)

            if max_index == size - 1:
                continue

            if max_index != 0:
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
                res.append(max_index + 1)

            arr[:size] = reversed(arr[:size])
            res.append(size)
        return res
