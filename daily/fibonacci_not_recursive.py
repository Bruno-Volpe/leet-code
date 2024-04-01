def fibonacci(n): 
    if n < 0: 
        raise("Incorrect input")
    
    if n == 0: return 0
    
    prev, ant_prev = 1, 0
    fibonacci_arr = [ant_prev, prev]
    
    for i in range(2, n):
        current = prev + ant_prev
        fibonacci_arr.append(current)
        ant_prev = prev
        prev = current
    
    return fibonacci_arr
    
print(fibonacci(7))