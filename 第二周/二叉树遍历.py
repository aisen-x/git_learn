class Node:
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    # 广度遍历

    def gdpredor(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item)
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)
    # 前中后序遍历非递归实现
    def qxbl(self):
        if self.root is None: return []
        cur, strack, res = self.root, [], []
        while strack or cur:
            while cur:
                res.append(cur.item)
                strack.append(cur)
                cur = cur.lchild
            ram = strack.pop()
            cur = ram.rchild
        return res

    def zxbl(self):
        if self.root is None: return []
        cur, strack, res = self.root, [], []
        while strack or cur:
            while cur:
                strack.append(cur)
                cur = cur.lchild
            ram = strack.pop()
            res.append(ram.item)
            cur = ram.rchild
        return res

    def hxbl(self):
        if self.root is None: return []
        cur, strack, res = self.root, [], []
        while strack or cur:
            while cur:
                res.append(cur.item)
                strack.append(cur)
                cur = cur.rchild
            ram = strack.pop()
            cur = ram.lchild
        return res[::-1]

# 前中后序遍历递归实现
def qxbl(node):
    if node is None:
        return
    print(node.item)
    qxbl(node.lchild)
    qxbl(node.rchlid)
def zxbl(node):
    if node is None:
        return
    zxbl(node.lchild)
    print(node.item)
    zxbl(node.rchlid)
def hxbl(node):
    if node is None:
        return
    hxbl(node.lchild)
    hxbl(node.rchild)
    print(node.item)
# 前中后序遍历非递归实现


