from collections import deque
#binary search tree

class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.left =None
        self.right =None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root =None
        
    def insert(self,val):
        self.root =self._insert(self.root,val)
        return self.root is not None
    def _insert(self,node,val):
        if node is None:
            return Node(val)
        
        if val < node.val:
            node.left = self._insert(node.left,val)
        else:
            node.right = self._insert(node.right,val)
        return node
    
    def search(self,val):
        return self._search(self.root,val)
    def _search(self,node, val):
        if node is None or node.val ==val:
            return node
        if val < node.val:
            return self._search(node.left,val)
        else:
            return self._search(node.right, val)
    def delete(self,val):
        self.root = self._delete(self.root,val)
    def _delete(self,node,val):
        if node is None:
            return None
        
        if val < node.val:
            node.left =self._delete(node.left,val)
        elif val>node.val:
            node.right = self._delete(node.right,val)
        else:
            if node.left is None:
                return node.left
            node.val = BinarySearchTree._get_min_val(node.right)
            node.right = self._delete(node.right, node.val)
        
        return node
    
    @classmethod
    def _get_min_val(cls,node):
        min_val =node.val
        while node.left:
            min_val = node.left.val
            node = node.left
        return min_val
    
    def to_list(self):
        return self._to_list(self.root)

    def _to_list(self, node):
        if node is None:
            return []
        return self._to_list(node.left) + [node.val] + self._to_list(node.right)

    def print_by_ascending(self):
        self._inorder(self.root)
        
    def _preorder(self, node):
        if node:
            print(node.val, end=' ')
            self._inorder(node.left)
            self._inorder(node.right)
    
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            print(node.val ,end=' ')
            self._inorder(node.right)
            
    def _postorder(self,node):
        if node:
            self._inorder(node.left)
            self._inorder(node.val, end=' ')

    def _postorder(self,node):
        if node:
            self._inorder(node.left)
            self._inorder(node.right)
            print(node.val, end = ' ')
    
    def level_order(self,node):
        if node is None:
            return     
        queue = deque()
        queue.append(node)
        
        level =0
        while queue:
            values = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur :
                    values.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                
                if values:
                    print(f'level : {level} , values : {values}')
                level +=1

nums = [10, 3, 4, 11, 32, 21, 45, 8, 1, 18]

bst = BinarySearchTree()
for n in nums:
    bst.insert(n)
assert bst.search(10) is not None
assert bst.search(18) is not None
assert bst.search(100) is None

print('\n\n오름 차순 정렬 출력')
bst.print_by_ascending()

print('\n\n레벨 오더 순회')
print(bst.level_order(bst.root))

print('\n\n이진 트리의 값을 오름 차순 정렬 리스트 자료구조로 반환')
print(bst.to_list())