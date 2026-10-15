import random
import time
import matplotlib.pyplot as plt


def selection_sort(arr):
    n=len(arr)

    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j -= 1
        arr[j+1]=key
    return arr

def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

algorithms = {
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Bubble Sort": bubble_sort,
    "Merge Sort": merge_sort,
}

sizes = [100, 250, 500, 1000, 1500, 2000] 
repeats = 3                               


def measure(func, data):
    start = time.perf_counter()
    func(data.copy())  
    return time.perf_counter() - start

def run_benchmark():
    results = {}
    for name in algorithms:
        results[name] = []

    for size in sizes:
        data = []
        for i in range(size):
            data.append(random.randint(0, 100000)) #0 ile 100000 arasında rastgele bir tam sayı üretir.

        for name in algorithms:
            func = algorithms[name]

            total = 0
            for again in range(repeats):
                total = total + measure(func, data)

            average = total / repeats
            results[name].append(average)

        print("n =", size, "completed")

    return results


def print_table(results):
    print("\nAverage times (seconds):")

    print("n", end="\t")
    for name in algorithms:
        print(name, end="\t")
    print()                     

    for i in range(len(sizes)):
        print(sizes[i], end="\t")
        for name in algorithms:
            sure = results[name][i]
            print(f"{sure:.5f}", end="\t") #sayıyı virgülden sonra 5 basamakla yazar.
        print()

def plot_results(results, filename="sort_graph.png"):
    for name in algorithms:
        plt.plot(sizes, results[name], marker="o", label=name)

    plt.title("Speed ​​Comparison of Sorting Algorithms")
    plt.xlabel("List size (n)")
    plt.ylabel("Time (second)")
    plt.legend()                

    plt.savefig(filename) 
    plt.show()       
    print("Chart saved:", filename)


if __name__ == "__main__":
    results = run_benchmark()
    print_table(results)
    plot_results(results)
