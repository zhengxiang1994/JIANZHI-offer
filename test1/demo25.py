class Solution:
    def coder(self, ls):
        count = 0
        result = []
        for i in range(len(ls)):
            if ls[i] == 0:
                count += 1
                if count >= 16:
                    result.append(0)
                    result.append(15)
                    count = 0
            else:
                result.append(ls[i])
                result.append(count)
                count = 0
        if ls[-1] == 0:
            result.append(0)
            result.append(count-1)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.coder([0, 0, 1, 0, 0, 0, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 9, 0, 0, 0]))