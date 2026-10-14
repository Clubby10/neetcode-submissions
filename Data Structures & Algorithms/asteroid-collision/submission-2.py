class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        abs(asteroid) = size
        - = left
        + = right
        each astroid moves at the same speed
        asteroids[i] != 0
        """
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                
                break
            else:
                stack.append(asteroid)

        return stack