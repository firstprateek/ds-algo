# ds-algo

Combinatorial problems are the ones where it is required to create a combinatorial object.
These objects can be of the following type:

n: Number of choices
k: length of combinatorial object


1) Permutation
1.1) With Repetition - n ^ k
1.2) Without Repetition - n!/(n-k)!

2) Combination - n! / (n-k)! x (k!)

3) Power Set - 2 ^ n
	(Sum of all combinations nC0, nC1 .. nCn)


## Template

Q: Given a alphanumeric string "a1b2c3", find all the strings where the letters can have lower or upper case.

slate: partial solution
S: Choices
i: Particular choice

784. Letter Case Permutation

https://leetcode.com/problems/letter-case-permutation/


## Note

1) For finding the time complexity of a recursive problem, use the recursion tree instead of looking at the structure of the code.
2) Time complexity will be branching factor ^ height of tree.
2.5) Multiply by time taken at each node, it could be different at intermediatery node and leaf node.
2.75) Like in above example, the time in intermediate nodes can be n to create a new string if slate is a string. Number of nodes in a tree * work done by that node.
2.99) A string is immutable so a new one is created when doing slate + "s[i]"

3) Use array instead of string for "slate" or partial solution since it is mutable so you won't end up creating a new string at each level.
4) Each frame / active record in the callstack will have its own string variable which will lead to an implicit space complexity of n^2 (0 + 1 + 2 ... n)
5) Array will be passed by reference so the implicit space complexity will be O(n)
6) Explicit space complexity will be 2^n * n for the results array


## Template 2 - Power set

Inclusion / Exclusion approach

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.helper(nums, 0, [])
        return self.results
    
    def helper(self, s, i, slate):
        if i == len(s):
            self.results.append(slate[:])
            return
        
        self.helper(s, i + 1, slate)
        
        slate.append(s[i])
        self.helper(s, i + 1, slate)
        slate.pop()


## Template 3 - Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.helper(nums, 0)
        return self.results
    
    def helper(self, nums, i):
        if i == len(nums):
            self.results.append(nums[:])
            return
        
        for pick in range(i, len(nums)):
            nums[i], nums[pick] = nums[pick], nums[i]
            self.helper(nums, i + 1)
            nums[i], nums[pick] = nums[pick], nums[i]


## Template 3 - Permutations - ii

With O(3n) space

from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.counter = Counter(nums)
        self.helper(nums, 0, [])
        return self.results
    
    def helper(self, nums, i, slate):
        if i == len(nums):
            self.results.append(slate[:])
            return
        
        for key in self.counter.keys():
            if self.counter[key] > 0:
                slate.append(key)
                self.counter[key] -= 1
                self.helper(nums, i + 1, slate)
                slate.pop()
                self.counter[key] += 1


The space taken by the hash map can be reduced by modifying the input array to reflect the current choice

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(slate):
            if len(slate) == len(nums):
                self.results.append(slate[:])
                return
            
            for i in range(len(nums)):
                cur = nums[i]
                if i == 0:
                    prev = None
                else:
                    prev = nums[i - 1]
                
                if cur == None or prev == cur:
                    continue
                
                slate.append(nums[i])
                nums[i] = None
                helper(slate)
                slate.pop()
                nums[i] = cur
        
        nums.sort()
        self.results = []
        helper([])
        return self.results

## BackTracking (pruning)

Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:        
        def helper(i=1, slate=[]):
            # base case
            if len(slate) == k:
                self.results.append(slate[:])
                return

            # backtracking case
            if i > n:
                return
            
            if len(slate) + (n - i + 1) < k:
                return
            
            # general case
            helper(i + 1, slate)
            
            slate.append(i)
            helper(i + 1, slate)
            slate.pop()
        self.results = []
        helper()
















