def powerSet(nums, idx=0, cur=[]):
  def recursive(idx, cur):
    if len(cur) == length:
      print(cur)
      return
    for i in range(idx, len(nums)):
      cur.append(nums[i])
      recursive(i+1, cur)
      cur.pop()
  for length in range(len(nums) + 1):
    #print('-----length-------', length)
    recursive(idx, cur)

def powerSet2(nums, idx=0, cur=[]):
  if idx == len(nums):
    print(cur)
    return
  powerSet2(nums, idx+1, cur)
  cur.append(nums[idx])
  powerSet2(nums, idx+1, cur)
  cur.pop()

powerSet2([1,2,3])
print('-----')
powerSet([1,2,3])
