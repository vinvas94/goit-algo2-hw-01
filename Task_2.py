import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))
    
    # Приклад використання
if __name__ == "__main__":
    arr = [3, 2, 1, 5, 4, 6]
    k = 5  
    result = quickselect(arr, k)
    print(f"{k + 1}-й найменший елемент: {result}")