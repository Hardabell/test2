# HAYDAR ARDABELL CODE

input_puzzle = (147981, 691423)

# array index
aturan = [
    
    lambda s: all(int(s[i]) <= int(s[i+1])
                  for i in range(len(s)-1)),
    
    lambda s: any(s[i] == s[i+1] for i in range(len(s)-1))
    
]

def test(num, aturan):
    return all(f(str(num)) for f in aturan)


def solve(input_puzzle, aturan):
    return sum(1 for i in range(input_puzzle[0], input_puzzle[1]+1) if test(i, aturan))


def secure_conatiner():
    return solve(input_puzzle, aturan[:2])


print(secure_conatiner()) 