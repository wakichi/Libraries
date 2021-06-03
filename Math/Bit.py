
def get_bit(num, where):
    """
    numのwhere番目のbitをgetする関数
    num: int
    where: int, 1-index, 1以上
    Hint: curry化しても便利
    """
    mask = 1 << where - 1
    masked_num = num & mask
    return masked_num >> where - 1
