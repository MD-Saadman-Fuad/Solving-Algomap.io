class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
            m = len(matrix)
            n = len(matrix[0])

            answer = []
            direction = "right"
            top = 0
            right = n
            down = m
            left = -1

            row, col = 0, 0
            
            while len(answer)<(m*n):
                if direction == "right":
                    while col < right:
                        answer.append(matrix[row][col])
                        col+=1
                    row, col = row+1, col-1
                    direction = "down"
                    right -=1

                elif direction == "down":
                    while row < down:
                        answer.append(matrix[row][col])
                        row+=1
                    row, col = row-1, col-1
                    direction = "left"
                    down -=1
                
                elif direction == "left":
                    while col > left:
                        answer.append(matrix[row][col])
                        col -=1
                    row, col = row -1 , col +1
                    direction = 'top'
                    left+=1
                else:
                    while row > top:
                        answer.append(matrix[row][col])
                        row-=1
                    row, col = row+1, col+1
                    direction = "right"
                    top+=1
                
            return answer
    
s = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(s.spiralOrder(matrix))