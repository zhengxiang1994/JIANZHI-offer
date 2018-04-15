class Solution:
    def insertsort(self, L):
        for i in range(1, len(L)):
            inset_index = 0
            for j in range(i):
                if L[i] > L[j]:
                    inset_index += 1
            temp = L[i]
            k = i
            while inset_index < k:
                L[k] = L[k-1]
                k -= 1
            L[inset_index] = temp
        return L


if __name__ == "__main__":
    s = Solution()
    print(s.insertsort([1, 3, 5, 7, 2, 4, 6]))

