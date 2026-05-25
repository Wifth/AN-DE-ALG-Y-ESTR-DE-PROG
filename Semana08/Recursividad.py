#def recx(n)

def recx(x, n):
    if x == n:
        print(x)
        return
    else:
        print(x)
        recx(x + 1, n)
        
recx(1, 5)
    
"""
int n = 5;
for(int x=1; x<=n; x = x + 1){
    Console.WriteLine(x);
}
1
2
3
4
5
"""