import csv
import random
import time




############################## Сортировки

def BubbleSort(A): # Сортировка пузырьком
    start = time.time()
    it = 0
    for j in range(len(A) - 1):
        it += 1
        for i in range(len(A) - 1):
            it += 1
            if A[i] > A[i + 1]:
                it +=1
                A[i], A[i + 1] = A[i + 1], A[i]
    stop = time.time()
    sec = stop - start
    print("\nКоличество итераций пузырьком: " + str(it))  
    return sec


global iterationOfQS
iterationOfQS = 0
global BlenItem
BlenItem = 0


def sort2(array2): #быстрая сортировка 
    global iterationOfQS
    iterationOfQS +=1
    array = array2
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0][1]
        for x in array:
            if x[1] < pivot:
                less.append(x)
            if x[1] == pivot:
                equal.append(x)
            if x[1] > pivot:
                greater.append(x)
        iterationOfQS +=1
        return sort2(less)+equal+sort2(greater)
    else: 
        return array

global iterS
iterS = iterationOfQS
global it
it = 132

def InsertionSort(A): # Cортировка вставками
    it = 0
    start1 = time.time()
    for i in range(1, len(A)): 
        it += 1
        new_elem = A[i] 
        j = i - 1 
        while j >= 0 and A[j] > new_elem: 
            A[j + 1] = A[j] 
            j -= 1
            it +=1
        A[j + 1] = new_elem
    stop1 = time.time()
    sec1 = stop1 - start1
    print("\nКоличество итераций вставками: " + str(it)) 
    return sec1



################ поиски
    start1 = time.time()
    stop1 = time.time()
    sec1 = stop1 - start1

def BinSearchVirt(li, x): # бинарный поиск для отсортированного массива
    it = 0
    i = 0
    j = len(li) - 1
    while i < j:
        it += 1
        m = int((i+j)/2)
        if x > li[m][1]:
            i = m + 1
        else:
            j = m
    if li[j][1] == x:
        print("\nКоличество операций в бинарном поиске: " + str(it) + "\n")
        return j
    else:
        print("\nКоличество операций в бинарном поиске: " + str(it) + "\n")
        return 0


def linearSearch(lst, x): # Линейный поиск 
    it = 0
    i = 0
    startLin = time.time()
    while (i < len(lst) and lst[i][1] != x):
        it += 2
        i += 1              
#    stopLin = time.time()

    print("\nКоличество итераций в линейном поиске:" + str(it)+'\n')
    if i < len(lst):
        stopLin = time.time()
        secLin = stopLin - startLin
        print("\nВремя выполнения линейного поиска:" + str(secLin) +'\n')

        return i
    else:
        stopLin = time.time()
        secLin = stopLin - startLin
        print("\nВремя выполнения линейного поиска:" + str(secLin) +'\n')
        return 0



def linearQSearch(lst, x1): # Быстрый Линейный поиск 
    it = 0
    x = ['0.1']
    startLinQ = time.time()
    x.append(x1)
    lst.append(x)
    i = 0
    while int(lst[i][1]) != x1:
        i += 1
        it += 1
    print("\nКоличество итераций в быстром линейном поиске:" + str(it)+'\n')
    
    if i < len(lst):
        stopLinQ = time.time()
        secLinQ = stopLinQ - startLinQ
        print("\nВремя выполнения быстрого линейного поиска:" + str(secLinQ) +'\n')
    
        return 1
    else:
        stopLinQ = time.time()
        secLinQ = stopLinQ - startLinQ
        print("\nВремя выполнения быстрого линейного поиска:" + str(secLinQ) +'\n')
        return 0


def interSearch(lst, x): #Интерполяционный поиск для отсортированного массива
    itIS = 0
    f = '0'
    l = 1
    r = len(lst) - 1
    i = 0
    while (r>=1)and(i<=len(lst)-1):
        itIS +=1
        i = l+((r-l)*(x-lst[l][1]))//((lst[r][1]-lst[l][1]))
        if x != lst[i][1]:
            itIS += 1
            l = i + 1
        else:
            itIS += 1
            print("\nКоличество итераций в блочном поиске: " + str(itIS) + "\n")
            return 1



######################################## ДЕРЕВО


class TreeNode:
    def __init__(self, key, val,left=None,right=None,
         parent=None):
        self.payload = val
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,value,lc,rc):
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:

    def __init__(self):
      self.root = None
      self.size = 0

    def length(self):
      return self.size

    def __len__(self):
      return self.size

    def __iter__(self):
      return self.root.__iter__()

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        global BlenItem
        global iterS
        iterS += 1
        sortTreeC = True
        if BlenItem > 15:
            iterS +=1
            sortTreeC = False
        if key < currentNode.key:
            iterS += 1
            if currentNode.hasLeftChild():
                   iterS +=1 
                   self._put(key,val,currentNode.leftChild)
            else:
                   iterS += 1 
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            iterS += 1
            if currentNode.hasRightChild():
                   iterS += 1 
                   self._put(key,val,currentNode.rightChild)
            else:
                    iterS += 1
                    if sortTreeC == True:
                        iterS +1 
                        currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                    else: return None
    def __setitem__(self,k,v):
        global BlenItem
        BlenItem +=1
        self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def findEl(self, value):
      current = self
      global it
      while current.hasLeftChild():
          it += 12
          current = current.leftChild
      print(it)
      self.__iter__()
      return current
    
    def __iter__(self):
       global it 
       if self:
            it += 2
            if self.hasLeftChild():
                it += 1
                for elem in self.leftChiLd:
                   it += 1 
                   if self.payload == value:
                       it += 1 
                       return self.key
                   yield elem
                yield self.key
            if self.hasRightChild():
                it += 10
                if self.paylosd == value:
                    it += 10
                    return self.key
                for elem in self.rightChild:
                   yield elem

    def getFinditem(self, value):
        self.__iter__()
        return 0

    def getSortitem(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False
    



########################################

def WriteArray(arr):
    f = open('massive.txt', 'w')
    for i in range(0, len(arr)-1):
        f.write(str(arr[i][0]) + '\n' + str(arr[i][1]) + '\n')
    f.close()


def ReadArray():
    
    f = open('massive.txt', 'r')
    arr = []
    b1 = [0, 0]
    arr1 = []
    arr1 = [line.strip() for line in f]
    for i in range(0, len(arr1), 2):
        arr.append(arr1[i:i+2])
    for i in range(0, len(arr)):
        arr[i][0] = float(arr[i][0])
        arr[i][1] = int(arr[i][1])
                   
    return arr

def RandomEl(a):
    b = 0
    while (b < 5):
        b = (random.randint(0, len(a)-1))
        element = a[b][1]
    print("индекс: " + str(b) + "\n")
    return element


a = []
m =[]


# Генерация массива

y = input("Если вы будете сами вводить данные массива, введите '0',\n если же автоматически - '1',\nесли данные будут считываться с файла - '2'\n")
if y == '0':
    
    x = input("Введите количество элементов массива\n")
    for i in range(int(x)):
        b = [0.1]
        text = input("\nВведите элемент\n")
        b.append(int(text))
        a.append(b)
        m.append(b)
        b.pop()
elif y == '1':
    x = input("\nВыберите количество элементов в массиве: 5, 10, 15, 30, 50, 100\n")
    for i in range(int(x)):
        b = [0.1]
        b.append(random.randint(1, 16000))
        a.append(b)
        m.append(b)
elif y == '2':
    print("Введите название файла: \n")
    text = input()
    with open(text+".csv") as f:
        reader = csv.reader(f)
        for row in reader:
            a.append(row)
            m.append(row)

else:
    print("\nНеправильно\n")
    exit(0)


WriteArray(a)

print("\n")

print("Время выполнения сортировки вставками: " + str(InsertionSort(a)) + "\n")

a = []
a = ReadArray()

print("\n")
print("Время выполнения сортировки пузырьком: " + str(BubbleSort(a)) + "\n")

a = []
a = ReadArray()

print("\n")
start6 = time.time()
sort2(a)
stop6 = time.time()
print("\nКоличество итераций быстрой сортировкой: " + str(iterationOfQS))
print("\nВремя выполнения быстрой сортировки: "+str(stop6-start6) + "\n")

a = []
a = ReadArray()

myTree = BinarySearchTree()
for i in range(0, len(a)-1):
    myTree.__setitem__(i, a[i][1])
StartTS = time.time()
for i in range(0, len(a)-1):
    myTree.getSortitem(i)
StopTS = time.time()
secTs = StopTS - StartTS
print("\nКоличество итераций сортировкой деревом: " + str(iterS) + "\n")
print("\nВремя выполнения сортировкой деревом: " + str(secTs) + "\n")

print("\n\nПроверка поисков\n")

el = RandomEl(a)
print("Значение искомое: "+str(el) + "\n")
print('\n\n')
startBin = time.time()
ses = 0.0011101
sort2(a)
BinSearchVirt(a, el)
stopBin = time.time()
secBin = stopBin - startBin
print("Время бинарного поиска: " + str(secBin) + "\n")
print('\n')
linearSearch(a, el)
print('\n\n')
sort2(a)
linearQSearch(a, el)
print("\n")
sort2(a)
start = 0
stop = 0
b = sort2(a)
start = time.time()
interSearch(b, el)
stop = time.time()
sec = stop - start
print("\nВремя выполнения блочного поиска: " + str(sec) + "\n")
print("\n")
sec -= ses
start = 0
stop = 0
start = time.time()
myTree.getFinditem(el)
stop = time.time()
ses = stop - start
print("\nКоличество итераций поиска по лереву: " + str(iterS))
print("\nВремя выполнения поиска по дереву: " + str(sec) + "\n")
