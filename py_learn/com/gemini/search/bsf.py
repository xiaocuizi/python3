from collections import deque

# 广度优先搜索 （breadth-first search BSF）
# 图的概念：图由节点和变组成，图用于模拟不同的东西如何相连的
# 案例：查找最短路径问题

# 关系图
graph = []
def search(name):
    # 定义一个搜索队列
    search_queue = deque()
    # 将目标加入搜索队列
    search_queue += graph[name]
    # 已经检查过的
    searched = []
    while search_queue:
        object = search_queue.popleft()
        if (is_result(object)):
            return True
        else:
            search_queue += graph[object]
            searched.append(object)
            return False


# 规则
def is_result(name):
    return name[-1] == "m"



print(search("you"))



