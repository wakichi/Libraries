# 右側がtrue 左側がfalse返す。
def predicate(x:int)-> bool:
    # ここを設定する。
    pass
    # sample
    #return x >= 20
    

# 二分探索
def binary_search(lis:list) -> int:
    left = 0
    right = 10**10 
    while right - left > 1:
        mid = left + (right - left)//2
        if predicate(lis[mid]):
            right = mid
        else:
            left = mid
    return right


print(binary_search(list(range(2,100))))

