'''
# Check prime efficiently

def check_prime(n):
    if n <=0:
        return
    for i in range(2,(n//2)+1,1):
        if n%i==0:
            return "Not prime Number"
        else:
            return"Not prime Number"
print(check_prime(12))
'''

'''
# Generate prime numbers in range

def generate_prime(n):
    result=[]
    for i in range(2,n+1,1):
        is_prime=True
        for j in range(2,int(i*0.5)+1,1):
            if i%j ==0:
                is_prime=False
        if is_prime:
            result.append(i)
    return result
print(generate_prime(122))
'''
'''
# Implement binary search
def binary_search(arr,target):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1

print(binary_search([2,4,6,8,10,12,14,16],10))
'''

#Implement linear search

'''
def linear_search(arr,target):
    result=[]
    for i in range(len(arr)):
        if arr[i]==target:
            result.append(i)
            
    return result
print(linear_search([2,4,61,254,21,1,42,12,42,121],42))
'''

'''
# Bubble sort

def bubble_sort(lst):
    a=len(lst)
    for i in range(a):
        for j in range(0,a-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]

    return lst

print(bubble_sort([5, 3, 8, 4, 2]))
'''

'''
# selection sort

def selection_sort(arr):
    n=len(arr)

    for i in range(n):
        min_index=i
        print(min_index)

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index=j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [64, 25, 12, 22, 11]
print(selection_sort(arr))
'''

# insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1]=key

print(insertion_sort([5, 3, 4, 1]))

























