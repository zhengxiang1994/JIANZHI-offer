class Solution:
    def selectionsort(self, L):
        for i in range(len(L)-1):
            min_index = i
            for j in range(i+1, len(L)):
                if L[j] < L[min_index]:
                    min_index = j
            temp = L[i]
            L[i] = L[min_index]
            L[min_index] = temp
        return L


if __name__ == "__main__":
    s = Solution()
    print(s.selectionsort([1, 3, 5, 7, 2, 4, 6]))


