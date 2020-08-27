from collections import deque
"""
[9 6 1 3 2 5 4 8 7]
stack = []
push 9; min_ele = 9; stack =[9];
push 6
6 < min_ele; push 2 * 6 - min_ele = 3; push 3; min_ele = 6; stack = [3 9];
push 1
1 < min_ele; push 2 * 1 - min_ele = -4; push -4; min_ele = 1; stack = [-4 3 9]
push 3
3 >= min_ele; push 3; min_ele = 1; stack = [3 -4 3 9]
push 2
2 >= min_ele; push 2; min_ele = 1; stack = [2 3 -4 3 9]
getMin = 1
pop
2 >= min_ele; pop 2; min_ele = 1; stack = [3 -4 3 9]
pop
3 >= min_ele; pop 3; min_ele = 1; stack = [-4 3 9]
pop
-4 < min_ele; min_ele = 2 * min_ele - (-4) = 2 + 4 = 6; pop and return prev_value of min_ele; min_ele = 6; stack = [3 9]
pop
3 < min_ele; min_ele = 2 * min_ele - 3 = 12 - 3 = 9; pop and return prev_value of min_ele; min_ele = 9; stack = [9]
pop
9 >= min_ele; pop 9; min_ele = 9; stack = []
"""


class stack:
    def __init__(self):
        self.s = deque()
        self.minEle = None

    def push(self, x):
        # CODE HERE
        if len(self.s) == 0:
            self.minEle = x
            self.s.appendleft(x)
        elif x >= self.minEle:
            self.s.appendleft(x)
        else:
            self.s.appendleft(2 * x - self.minEle)
            self.minEle = x

    def pop(self):
        # CODE HERE
        if len(self.s) != 0:
            if self.s[0] >= self.minEle:
                return self.s.popleft()
            else:
                temp = self.minEle
                self.minEle = 2 * self.minEle - self.s[0]
                self.s.popleft()
                return temp
        else:
            self.minEle = None
            return -1

    def getMin(self):
        # CODE HERE
        if len(self.s) == 0:
            self.minEle = None
            return -1
        else:
            return self.minEle
