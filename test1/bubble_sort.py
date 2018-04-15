class Solution:
    def bubblesort(self, L):
        for i in range(len(L)-1):
            for j in range(len(L)-i-1):
                if L[j+1] < L[j]:
                    L[j], L[j+1] = L[j+1], L[j]
        return L


if __name__ == "__main__":
    s = Solution()
    print(s.bubblesort([1, 3, 5, 7, 2, 4, 6]))



