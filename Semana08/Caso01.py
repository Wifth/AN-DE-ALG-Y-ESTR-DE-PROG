def recx2(x):
    acu = ""
    print(recx(x, acu))

def recx(x, acc):
    if x == 0:
        return acc
    else:
        return recx(x - 1, acc + str(x) + "\n")
        
recx2(5)
    
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