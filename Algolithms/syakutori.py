# n,kをglobalに定義
n = 0
k = 0

# 条件を記入
def predicate(x):
    # xは判定する数、kは閾値
    return x<=k

#条件を満たす最長の配列の長さの場合
def syakutori(lis):
    longest = 0
    right =0
    sum_part = 0
    for left in range(n):
    # 条件を満たすときのループ
        while right<n and predicate(sum_part+lis[right],k):
            sum_part+= lis[right]
            right +=1
        # 上記をbreakしたとき(このときのrightはギリギリ条件を満たす)
        longest = max(longest, right-left)
        # left+=1の準備
        if right == left: right+=1
        else: sum_part-=lis[left]
    return longest


if __name__ == "__main__":
    n,k = map(int,input().split())
    lis = list(map(int, input().split()))

    ans = syakutori(lis)
    print(ans)