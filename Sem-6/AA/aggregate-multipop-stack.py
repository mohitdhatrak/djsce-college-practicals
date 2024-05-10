# Multipop stack amortized analysis using aggregate method 
# Assuming the multipop operation 
# Cost of push : 1, Cost of pop : 1 and Cost of multipop(k) : min(len(stack), k)
# Here each multipop can remove at max n elements from the stack and there can be n such operations the worst case time complexity turns out to be O(n^2) which is not a very tight bound or and overestimate.
# Aggregate method 
# Since for every multipop(k) we need atleast k elements in the stack, hence we cannot multipop n elements n times and the worst case can not be more that O(n) and T(n) making the amortized cost to be T(n) / n 

def push(stack, n, cost):
    for i in range(n):
        stack.append(i)
        cost += 1
    return cost
    
def multipop(stack, n, cost):
    for i in range(n):
        k = int(input('\nEnter the number of elements to multipop: '))
        for i in range(min(k, len(stack))):
            stack.pop()
            cost += 1

        print(f'Stack after multipop({k}):', stack)
        print(f'Cost after multipop({k}):', cost)    
    return cost

stack = []
cost = 0
operations = 0

n = int(input('Enter the number of elements to push in stack: '))
operations += n # each push and pop counts as 1 operation, and has cost 1
cost = push(stack, n, cost)
print(f'Stack after {n} push operations:', stack)
print(f'Cost after {n} push operations:', cost)

n = int(input('\nEnter the number of multipop operations to perform: '))
operations += n # each multipop(k) counts as 1 operation, and has cost as k
cost = multipop(stack, n, cost)

amortized_cost = cost / operations
print('\nTotal cost =', cost)
print('Total operations =', operations)
print('Amortized Cost per operation:', round(amortized_cost, 2))    