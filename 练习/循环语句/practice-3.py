row = int(input("请输入行数："))
fuhao = "*"
for i in range(1, row+1):
    for j in range(1, i+1):
        print(fuhao, end=" ")
    print()