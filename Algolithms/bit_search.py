# bit全探索を行う関数
def bit_search(n):
    bit_list = []
    for i in range(2**n):
        bit_cart=[]
        for j in range(n):
            if((i>>j)&1):
                bit_cart.append(1)
            else:
                bit_cart.append(0)
        bit_list.append(bit_cart)

    return bit_list


if __name__ == "__main__":
    from pprint import pprint
    bit_list = bit_search(3)
    pprint(bit_list)
    print(bit_list[1][1])