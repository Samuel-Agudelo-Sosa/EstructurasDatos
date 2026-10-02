def increasing():
    test = int(input())
    for i in range(test):
        arr = [int(x) for x in input().split()]
        arr.sort()
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                print("NO")
                break
            
        else:
            print("YES")
                

increasing()
