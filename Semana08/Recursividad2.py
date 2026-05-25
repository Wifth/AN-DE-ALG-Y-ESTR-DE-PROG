def recx(x):
    if x == 1:
        print(x)
        return
    else:
        print(x)
        recx(x - 1)
        
recx(5)
    
"""
int n = 1;
for(int x=5; x>=n; x = x - 1){
    Console.WriteLine(x);
}
5
4
3
2
1
"""