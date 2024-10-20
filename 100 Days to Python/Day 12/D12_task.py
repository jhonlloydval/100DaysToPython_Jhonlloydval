# D12 TASK
# PRIME NUMBER


def is_prime(num):
    if num <= 1:
        return False
    
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True
           
        
print(is_prime(int(input())))

