# print all positive numbers in a range
def ptive(name):
    lst1 = []
    for j in name:
        if j > 0:
            lst1.append(j)
    print(lst1)


if __name__ == "__main__":
    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    ptive(lst)
