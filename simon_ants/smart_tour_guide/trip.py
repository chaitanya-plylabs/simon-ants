from mipcl_py.mipshell.mipshell import *
class Trip(Problem):
    def model(self, n, cost):
        self.n = n
        self.x = x = VarVector((n,n),"x",BIN)
        u = VarVector([n], "u")
        p = VarVector([n], "p")
        minimize(sum_(cost[i][j] * x[i][j] for i in range(n) for j in range(n)))
        for j in range(n):
            sum_(x[i][j] for i in range(n) if i != j) == 1
        for i in range(n):
            sum_(x[i][j] for j in range(n) if j != i) == 1
        for i in range(n):
            u[i] <= n-1
            u[i] >= 0
        for i in range(1,n):
            for j in range(1,n):
                if( i != j):
                    u[i] - u[j] + n*x[i][j] <= n-1

    def setSolution(self):
        x = self.x
        n = self.n
        self.path = path = []
        self.next = next = [0 for i in range(n)]
        edges = 0
        current = 0
        while(edges < n):
            for j in range(n):
                if(x[current][j].val > 0.5):
                    path.append((current,j))
                    next[current] = j
                    break
            current = j
            edges += 1
    
    def getPath(self):
        return self.path
    
    def getNextLookup(self):
        return self.next

