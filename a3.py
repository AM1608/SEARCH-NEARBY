
class Node:
    def __init__(self, d,):
        self.data = d
        self.left = None
        self.right = None
        self.ytree=None 
class PointDatabase:
    def __init__(self,pointlist):
        
        l1 = sorted(pointlist, key = lambda elem: elem[0]) 
        l2 = sorted(pointlist, key = lambda elem: elem[1])
        
                
        def makeBST(arr):
        
            if not arr:
                return None
            
            mid = (len(arr)) // 2
                            
            root = Node(arr[mid])
                                        
            root.left = makeBST(arr[:mid])
            root.right = makeBST(arr[mid+1:])

            return root

        x_tree= makeBST(l1)
        

        x_tree.ytree=makeBST(l2)

        def build_ytree(node,list):
            if len(list)==1:
                return
            ltree=[]
            rtree=[]
            for i in list:
                if i[0]<node.data[0]:
                    ltree.append(i)
                elif i[0]>node.data[0]:
                    rtree.append(i)
            if node.left:
                node.left.ytree = makeBST(ltree)
            if node.right:
                node.right.ytree = makeBST(rtree)
            if node.left:
                build_ytree(node.left,ltree)
            if node.right:
                build_ytree(node.right,rtree)

        build_ytree(x_tree,l2)
        self.tree=x_tree
        

    def searchNearby(self,qu,d):

        def find(root, key,idx):
           
            if root is None:
                return
        
            
            if root.data[idx] == key:

                if root.left is not None:
                    ins = root.left
                    while(ins.right):
                        ins = ins.right
                    find.pre = ins
        
        
                
                if root.right is not None:
                    ins = root.right
                    while(ins.left):
                        ins = ins.left
                    find.suc = ins
        
                return
        
            
            if root.data[idx] > key :
                find.suc = root
                find(root.left, key,idx)
        
            else:
                find.pre = root
                find(root.right, key,idx)
        

        def ancestor(root, n1, n2,id):
 
            
            if root is None:
                return None
        
           
            if(root.data[id] > n1[id] and root.data[id] > n2[id]):
                return ancestor(root.left, n1, n2,id)
        
            
            if(root.data[id] < n1[id] and root.data[id] < n2[id]):
                return ancestor(root.right, n1, n2,id)
        
            return root

        def storesubtree(r,p):
            if(r):
                storesubtree(r.left)
                p.append(r.data)
                storesubtree(r.right)

        def searchnode(node,x,id):
            if node is None or node.data[id]==x:
                return node
            
            if node.data[id]<x:
                return searchnode(node.right,x,id)

            return searchnode(node.left,x,id)

        def search_ytree(tree,x,y):
            ans=[]
            s=searchnode(tree,x,1)
            if (s):
                a=s
                
            else:
                find.pre = None
                find.suc = None
                find(tree,x,1)
                a=find.suc
            s=searchnode(tree,y,1)
            if (s):
                b=s
            else:
                find.pre = None
                find.suc = None
                find(tree,y,1)
                b=find.pre
            if(a==None or b==None):
                return ans
            split=ancestor(tree,a.data,b.data,1)
            ans.append(split.data)
            if split.data==a.data:
                m=False
            else:
                m=True
            rot=split.left
            while(rot and m):
                
                if(rot.data[1]<a.data[1]):
                    rot=rot.right
                if(rot.data[1]>a.data[1]):
                    ans.append(rot.data)
                    storesubtree(rot.right,ans)
                    rot=rot.left
                if(rot.data[1]==a.data[1]):
                    ans.append(rot.data)
                    break
            if split.data==b.data:
                m=False
            else:
                m=True
            rot=split.right
            while(rot and m):
               
                if(rot.data[1]<b.data[1]):
                    ans.append(rot.data)
                    storesubtree(rot.left,ans)
                    rot=rot.right
                if(rot.data[1]>b.data[1]):
                    rot=rot.left
                if(rot.data[1]==b.data[1]):
                    ans.append(rot.data)
                    break
            return ans

        def search_xtree(tree,x,y,p,q):
            mylist=[]
            s=searchnode(tree,x,0)
            if (s):
                a=s
                
            else:
                find.pre = None
                find.suc = None
                find(tree,x,0)
                a=find.suc
            s=searchnode(tree,y,0)
            if (s):
                b=s
                
            else:
                find.pre = None
                find.suc = None
                find(tree,y,0)
                b=find.pre
            
            if(a==None or b==None):
                return mylist
            split=ancestor(tree,a.data,b.data,0)
            
            if split.data==a.data:
                m=False
            else:
                m=True
            
            if(split.data[1]>=p and split.data[1]<=q):
                mylist.append(split.data)
            rot=split.left
            while(rot and m):
                
                if(rot.data[0]<a.data[0]):
                    rot=rot.right
                if(rot.data[0]>a.data[0]):
                    if (rot.data[1]>=p and rot.data[1]<=q):
                        mylist.append(rot.data)
                    if(rot.right):
                        mylist+=search_ytree(rot.right.ytree,p,q)
                    rot=rot.left
                if(rot.data[0]==a.data[0]):
                    if (rot.data[1]>=p and rot.data[1]<=q):
                        mylist.append(rot.data)
                    break
            if split.data==b.data:
                m=False
            else:
                m=True
            rot=split.right
            while(rot and m):
               
                if(rot.data[0]<b.data[0]):
                    if (rot.data[1]>=p and rot.data[1]<=q):
                        mylist.append(rot.data)
                    if(rot.left):
                        mylist+=search_ytree(rot.left.ytree,p,q)
                    rot=rot.right
                if(rot.data[0]>b.data[0]):
                    rot=rot.left
                if(rot.data[0]==b.data[0]):
                    if (rot.data[1]>=p and rot.data[1]<=q):
                        mylist.append(rot.data)
                    break
            return mylist
        return search_xtree(self.tree,qu[0]-d,qu[0]+d,qu[1]-d,qu[1]+d)







            
