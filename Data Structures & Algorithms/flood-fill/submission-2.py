class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # BFS
        origin = image[sr][sc]
        if origin == color:
            return image

        ROWS, COLS = len(image), len(image[0])

        queue = deque([(sr, sc)])
        image[sr][sc] = color
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == origin:
                    image[nr][nc] = color
                    queue.append((nr, nc))
                    
        return image

