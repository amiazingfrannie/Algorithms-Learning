'''
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
'''

def draw_line(tick_length, tick_label = ''):
    line = "-" * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, line_length):
    draw_line(line_length, '0')
    for i in range(1, num_inches+1):
        draw_interval(line_length - 1)
        draw_line(line_length, str(i))

draw_ruler(1,3)


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

list_num = [3,5,10,15,20]
binary_search(list_num, 20, 0, 5)
print(binary_search(list_num, 20, 0, 5))




import os

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            print(childpath)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total),path)
    return total

disk_usage(r"\Users\fanfan\Desktop\Leetcode")

print(os.listdir(r"\Users\fanfan\Desktop\Leetcode"))