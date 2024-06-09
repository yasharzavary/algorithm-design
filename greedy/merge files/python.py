
# node class for making tree
class node:
    def __init__(self) -> None:
        self.__data = None;
        self.right = None
        self.left = None

    @property
    def data(self):return self.data
    @data.setter
    def data(self, new):self.data = new

    def __add__(self, other):
        if(isinstance(other, int)):return self.data + other
        else: return self.data + other.data
    def __radd__(self, other):
        if(isinstance(other, int)):return self.data + other
        else: return self.data + other.data

    def __str__(self): return str(self.data)


def merge_file(nums: list):
    """
        params:
            nums: number list
        
        return:
            tree's first node
            total size
    """
    total = 0
    # main loop for pop and add to the number list
    while len(nums) != 1:
        x = nums.pop()
        y = nums.pop()
        new = node()
        node.data = x + y
        total = x+y
        node.right = x
        node.left = y
        nums.append(new)
    return nums[0], total

#input
numbers = list(map(int, input().split()))
result, num = merge_file(sorted(numbers, reverse=True))
print(num)
print(result)

