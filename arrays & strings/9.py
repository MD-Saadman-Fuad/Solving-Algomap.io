class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
            answer = []
            intervals.sort()

            answer.append(intervals[0])
            i = 1
            j = 0

            while i < len(intervals):
                if answer[j][1] >= intervals[i][0]:
                    answer[j][1] = (max(answer[j][1], intervals[i][1]))
                else:
                    answer.append(intervals[i])
                    j+=1
                i+=1
            return answer
s = Solution()
print(s.merge([[1,3],[2,6],[8,10],[15,18]]))