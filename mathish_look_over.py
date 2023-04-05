def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
    
print(is_triangle(1, 2, 2))

def bouncing_ball(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        print(count)
        h*=bounce
        if h > window: count += 1
    return count or -1

print(bouncing_ball(30, 0.66, 1.5))

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
        
print(find_even_index([1,2,3,4,3,2,1]))

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

print(sort_array([5, 3, 2, 8, 1, 4]))


def scrambl(s1, s2):
    common = [item for item in s2 if s1.count(item) >= s2.count(item)]
    if len(common) == len(s2):
        return True
    return False
import time 

def scrambll(s1, s2):
    setting_one = set(s1)
    setting_two = set(s2)
    empty_1 = {}
    empty_2={}
    for setting in setting_two.union(setting_one):
        empty_1[setting] = s1.count(setting)
        empty_2[setting] = s2.count(setting)
    for key, val in empty_2.items():
            if key not in empty_1 or val > empty_1[key] :
                return False
    return True

print(scrambll('amylmycujpbjpfn', 'nfajmbjpjp'))
#og function
start_time = time.time()
scrambl('rkqodlw', 'world')
end_time = time.time()
total_time = end_time - start_time
print(f'total time : {total_time}')


#  time for updated func
start_time = time.time()
scrambll('rkqodlw', 'world')
end_time = time.time()
total_time = end_time - start_time
print(f'total time : {total_time}')

class add(int):
    def __call__(self,n):
        return add(self+n)

print(add(1)(2))


def move_zeross(lst):
    zeros = []
    not_zeros = []
    for nums in lst:
        if nums == 0:
            zeros.append(nums)
        else:
            not_zeros.append(nums)
    return not_zeros + zeros
    
def move_zeros(lst):
    return sorted(lst, key=lambda x: x == 0)

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))

def cakes(recipe, available):
    default = []
    for r in recipe:
        if r not in available:
            return 0
        else:
             default.append(available[r]/recipe[r])
    return int(min(default))
                
def cakes_better(recipe, available):
	return min(available.get(k, 0)/recipe[k] for k in recipe)

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))

print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},{"sugar": 500, "flour": 2000, "milk": 2000}))