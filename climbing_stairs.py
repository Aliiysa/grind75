def climbStair(n):
    memory = {}
    memory[1] = 1
    memory[2] = 2

    def climb(n):
        if n in memory:
            return memory[n]
        else:
            memory[n] = climb(n-1) + climb(n-2)
            return memory[n]
    
    return climb(n)
