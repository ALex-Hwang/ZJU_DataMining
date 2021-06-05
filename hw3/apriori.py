from utilis import *
import pandas as pd

# apriori算法
def apriori(data_set, mini_support):
    # 生成的项集长度
    k = 2
    item_sets = []
    supports = {}

    candidateSet1 = generate_item_set(data_set)
    l1, support1 = generate_support(data_set, candidateSet1, mini_support)

    item_sets.append(l1)
    supports.update(support1)

    while True:
        candidateSeti = generate_new_freq(item_sets[-1], k)
        li, supporti = generate_support(data_set, candidateSeti, mini_support)
        if li:
            item_sets.append(li)
            supports.update(supporti)
            k += 1
        else: 
            break
    
    return item_sets, supports

if __name__ == "__main__":
    data = pd.read_csv('./dataset/bank-additional-full.csv', sep=';')
    # 预处理    


    data = data[['job', 'age', 'marital', 'education', 'y', 'contact', 'month', 'campaign', 'duration']]
    data = data.values.tolist()
    print(len(data))
    l, support = apriori(data, 0.5)
    print(l)
    print("-"*40)
    print(support)


    '''
    dic = {'user_id':[111,111,	
                          112,112,112,112,
                          113,113,113,113,
                          114,114,114,114,
                          115,115,115,115],
               'item_id':['豆奶','莴苣',		
                          '莴苣','尿布','葡萄酒','甜菜',
                          '豆奶','尿布','葡萄酒','橙汁',
                          '莴苣','豆奶','尿布','葡萄酒',
                          '莴苣','豆奶','尿布','橙汁']}
    data = pd.DataFrame(dic)

    # 关联规则中不考虑多次购买同一件物品，删除重复数据
    data = data.drop_duplicates()

    # 初始化列表
    data_set = []

    # 分组聚合，同一用户购买多种商品的合并为一条数据，只有1件商品的没有意义，需要进行过滤
    groups = data.groupby(by='user_id')
    for group in groups:
        if len(group[1]) >= 2:
            data_set.append(group[1]['item_id'].tolist())

    l, support = apriori(data_set, 0.5)
    print(l)
    print(support)

    '''