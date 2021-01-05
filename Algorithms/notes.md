# Notes

## Sorting

### Implemented
- [x] Selection Sort
- [x] Bubble Sort
- [x] Insertion Sort
- [x] MergeSort
- [x] QuickSort
- [x] HeapSort
- [x] TimSort
- [ ] Tree Sort - TODO: Implement
- [x] Radix Sort

### Analysis 
| Name      | Best | Average | Worst | Memory | Stable |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| **Selection sort** | n<sup>2</sup> | n<sup>2</sup> | n<sup>2</sup> | 1 | Depends |
| **Bubble sort** | n | n<sup>2</sup> | n<sup>2</sup> | 1 | Yes | 
| **Insertion sort** | n | n<sup>2</sup> | n<sup>2</sup> | 1 | Yes |
| **Mergesort** | nlogn | nlogn | nlogn | Depends | Yes |
| **In-place Mergesort** | - | - | n(logn)<sup>2</sup> | 1 | Yes |
| **Quicksort** | nlogn | nlogn | n<sup>2</sup> | logn | Depends |
| **Heapsort** | nlogn | nlogn | nlogn | 1 | No |
| **Timsort** | n | nlogn | nlogn | n | Yes |
| Introsort | nlogn | nlogn | nlogn | logn | No |
| Shell sort | n | n(logn)<sup>2</sup> | O(nlog<sup>2</sup>n) | 1 | No |
| Binary Tree sort | n | nlogn | nlogn | n | Yes |
| Cycle sort | - | n<sup>2</sup> | n<sup>2</sup> | 1 | No |
| Library sort | - | nlogn | n<sup>2</sup> | n | Yes |
| Patience sorting | - | - | nlogn | n | No |
| Smoothsort | n | nlogn | nlogn | 1 | No |
| Strand sort | n | n<sup>2</sup> | n<sup>2</sup> | n | Yes |
| Tournament sort | - | nlogn | nlogn | | |
| Cocktail sort | n | n<sup>2</sup> | n<sup>2</sup> | 1 | Yes |
| Comb sort | - | - | n<sup>2</sup> | 1 | No |
| Gnome sort | n | n<sup>2</sup> | n<sup>2</sup> | 1 | Yes |
| Bogosort | n | n•n! | n•n!→∞ | 1 | No |

## Search

### Implemented
- [x] Regular Linear Search
- [x] Recursive Binary Search
- [x] Iterative Binary Search
