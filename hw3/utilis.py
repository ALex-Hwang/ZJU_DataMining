import pandas as pd

def generate_item_set(data_set):
    item_set = set()
    for transaction in data_set:
        for item in transaction:
            # frozenset有issubset方法
            item_set.add(frozenset([item]))
    return item_set

def generate_support(data_set, item_set, mini_support):
    res = set()
    count = {}
    support = {}

    for transaction in data_set:
        for item in item_set:
            if item.issubset(transaction):
                if item in count:
                    count[item] += 1
                else:
                    count[item] = 1

    size = float(len(data_set))

    for item in count:
        if (count[item]/size) >= mini_support:
            res.add(item)
            support[item] = count[item]/size


    return res, support


def generate_new_freq(item_set, k):
    res = set()
    size = len(item_set)
    item_list = list(item_set)

    # 遍历set，开始合并操作
    for i in range(size):
        for j in range(i+1, size):
            list1 = list(item_list[i])
            list2 = list(item_list[j])
            # 确保k-1个元素是相同的，再进行union
            list1.sort()
            list2.sort()
            if list1[0:k-2] == list2[0:k-2]:
                temp = item_list[i] | item_list[j]
                res.add(temp)
                
    return res


    
