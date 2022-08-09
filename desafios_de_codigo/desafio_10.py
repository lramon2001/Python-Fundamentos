t = int(input())
for i in range(0,t):
    a, b, n = input().split()
        
    result = []
    for j in range(0,int(n)):
        result.insert(j, int(a))
        
        for k in range(0,j+1):
            exp = pow(2, k)
            result[j] += exp * int(b);
            
    for r in result:
        print(r, end = ' ')
        
    print('')
