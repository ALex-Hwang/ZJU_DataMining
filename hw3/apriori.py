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


# 生成关联规则
# 由于我们最后只需要推出y与否，所以我们在最后做一个判断，值输出y作为结果的关联规则。
def association(freq_sets, supports, min_conf):
    rules = []
    max_len = len(freq_sets)

    # 筛选符合规则的频繁集计算置信度，满足最小置信度的关联规则添加到列表
    for k in range(max_len - 1):
        for freq_set in freq_sets[k]:
            for sub_set in freq_sets[k + 1]:
                if freq_set.issubset(sub_set):
                    frq = supports[sub_set]
                    conf = supports[sub_set] / supports[freq_set]
                    rule = (freq_set, sub_set - freq_set, frq, conf)
                    if conf >= min_conf:
                        res_set = sub_set - freq_set
                        if frozenset(["y_no"]).issubset(res_set) or frozenset(["y_yes"]).issubset(res_set):
                            #print(freq_set,"-->", res_set,'frq:',frq,'conf:',conf)
                            rules.append(rule)
    return rules



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

