import winsound
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print("Swap occurred:", arr)
            winsound.Beep(1000, 600)  
            time.sleep(0.5) 

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main():
    arr = input("Enter the array elements separated by space: ").split()
    arr = [int(x) for x in arr]  # Convert input strings to integers
    print("Given array is:", arr)
    merge_sort(arr)
    print("Sorted array is:", arr)

if __name__ == "__main__":
    main()
