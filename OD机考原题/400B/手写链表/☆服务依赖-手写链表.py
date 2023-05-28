# -*- coding: utf-8 -*-
# @Time  : 2023/05/25 20:27
# @author: dtf
'''
https://dream.blog.csdn.net/article/details/128989908
服务依赖or服务失效判断

每个服务用字符串（只包含字母和数字，长度<=10）唯一标识，服务间可能有依赖关系，如A依赖B，则当B故障时导致A也故障
传递具有依赖性，如A依赖B，B依赖C，当C故障时导致B故障，也导致A故障。
给出所有依赖关系以及当前已知故障服务，要求输出所有正常服务
输入：
    依赖关系列表
    故障服务列表
输出：
    依赖关系列表中提及的所有服务中可以正常工作的服务列表
    按照依赖关系列表中出现的次序排序。特别的，没有正常节点输出单独一个半角逗号

输入：
    a1-a2,a5-a6,a2-a3
    a5,a2
输出：
    a6,a3

'''


def add(server_link):
    # 依赖-被依赖
    a, b = server_link.split("-")
    # 键（a），键值（{"val": a, "next": []}），即{a: {"val": a, "next": []}}
    if a not in nodes:
        nodes[a] = {"val": a, "next": []}
        '''！！！最绝的是，放在这里只会记录一次'''
        node_indices[a] = len(node_indices)     # 记录该元素在字典中出现的先后顺序
    else:
        # 如果nodes存在heads中，说明a-b, c-a，这种情况存在，即c依赖a,a依赖b，那么a当然不能存在heads中，他们是一条线上的，即b要当头
        # [{'val': 'a6', 'next': []}, {'val': 'a3', 'next': []}]
        if nodes[a] in heads:
            heads.remove(nodes[a])
    '''
    构成的形式为b->a，即一旦b是故障服务，那么a也故障
    按照上述类型，逐渐把所有的关系捋顺
    '''
    # 被依赖服务，并没有在节点字典中
    if b not in nodes:
        nodes[b] = {"val": b, "next": [nodes[a]]}
        node_indices[b] = len(node_indices)
        heads.append(nodes[b])


def delete(del_node):
    def delete_next(node):
        if del_node in node["next"]:
            node["next"].remove(del_node)
            return
        for _node in node["next"]:
            delete_next(_node)

    '''这种情况代表，所有服务都依赖的那一个服务故障了，后边所有的就全部故障了，直接输出","'''
    if del_node in heads:
        heads.remove(del_node)
        return
    for _node in heads:
        delete_next(_node)


'''数据处理部分'''
servers = input()   # 服务器列表
errors = input()    # 故障列表
heads = []
nodes = {}          # 以字典形式存储所有的节点，类型为：{key1:{}，key2:{}......}
node_indices = {}   # 以字典形式存储依赖关系中该服务出现的先后顺序，类型为：{a:1, b:2......}
for s in servers.split(','):    # 处理服务器之间的依赖关系
    add(s)
# 遍历删除 节点 以及 头节点 中所有的故障服务
for e in errors.split(','):     # 处理故障
    delete(nodes[e])
'''# heads:  [{'val': 'a6', 'next': []}, {'val': 'a3', 'next': []}]
print('heads: ', heads)
# nodes:  {'a1': {'val': 'a1', 'next': []}, 'a2': {'val': 'a2', 'next': [{'val': 'a1', 'next': []}]}, 
# 'a5': {'val': 'a5', 'next': []}, 'a6': {'val': 'a6', 'next': []}, 'a3': {'val': 'a3', 'next': []}}
print('nodes: ', nodes)
# node_indices:  {'a1': 0, 'a2': 1, 'a5': 2, 'a6': 3, 'a3': 4}
print('node_indices: ', node_indices)'''
'''处理结果输出部分'''
result = []
# 递归获取链表中所有的节点值
def do_next(node):
    result.append(node["val"])
    for n in node["next"]:
        do_next(n)
# 遍历所有的头节点列表
for n in heads:
    do_next(n)
# 按依赖关系列表中出现的先后顺序排序
result = sorted(result, key=lambda x: node_indices[x])
# 没有正常节点，输出单独一个半角逗号
print(",".join(result) if result else ",")

# print('heads2: ', heads)
# print('nodes2: ', nodes)
# print('node_indices2: ', node_indices)


