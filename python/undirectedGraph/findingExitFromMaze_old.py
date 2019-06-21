class FindingExitFromMaze:
    def __initAdjMatrix(self, n, edges):
        matrix = [[0 for col in range(n)] for row in range(n)]
        for u, v in edges:
            matrix[u-1][v-1] = matrix[v-1][u-1] = 1

        return matrix

    def adjMatrixIter(self, n, m, edges, st, ed):
        matrix = self.__initAdjMatrix(n, edges)

        visited = [0 for i in range(n)]
        visited[st-1] = 1
        stack = [st-1]
        
        while len(stack) != 0:
            lastItem = stack[-1]
            nextItem = None

            for i in range(n):
                if matrix[lastItem][i] == 1 and visited[i] == 0:
                    nextItem = i
                    break

            if nextItem is None:
                stack.pop()
            else:
                visited[nextItem] = 1
                stack.append(nextItem)

        return visited[ed - 1]

    def adjMatrixRecur(self, n, m, edges, st, ed):
        matrix = self.__initAdjMatrix(n, edges)

        visited = [0 for i in range(n)]
        self.amr(matrix, visited, st-1)

        return visited[ed - 1]

    def amr(self, matrix, visited, v):
        visited[v] = 1

        for i in range(len(matrix)):
            if matrix[v][i] == 1 and visited[i] == 0:
                self.amr(matrix, visited, i)




    def __initAdjList(self, n, edges):
        arr = [set() for i in range(n)]
        for u, v in edges:
            arr[u-1].add(v-1)
            arr[v-1].add(u-1)
        
        return arr

    def adjListIter(self, n, m, edges, st, ed):
        arr = self.__initAdjList(n, edges)
        
        visited = [0 for i in range(n)]
        visited[st-1] = 1
        stack = [st-1]

        while len(stack) != 0:
            newItem = None

            for i in arr[stack[-1]]:
                if visited[i] == 0:
                    newItem = i
                    break

            if newItem is None:
                stack.pop()
            else:
                visited[newItem] = 1
                stack.append(newItem)
        
        return visited[ed - 1]
                    

    def adjListRecur(self, n, m, edges, st, ed):
        arr = self.__initAdjList(n, edges)

        visited = [0 for i in range(n)]
        self.alr(arr, visited, st)

        return visited[ed - 1]

    def alr(self, arr, visited, v):
        visited[v] = 1

        for i in arr[v]:
            if visited[i] == 0:
                self.alr(arr, visited, i)
