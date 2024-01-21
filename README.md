# goit-algo-hw-04

Sorting algorithms velocity comparison

While testing insertion, merge and Timsort algorithm with different amount of the data, we recived the next results: 

 - Indertion sort is the slowest one, especially on large amount of data its velocity falls incredibly (time complexity O(n*n)). 
 - Merge sort works much faster, because of it's time complexity O(n*log n). 
 - But the fastest results we obtain using build in methods sort() and sorted(), both use Timsort algoriths build on combining insertion and merge sorting algorithms. Sorting time increase smoothly and not significanty even for large data amounts.

![Sorting time comparison for different algorithms](<algo_time_comparison.png>)

So, the Timsort algorithm is the fastest one using combinning of insertion and merge sort algorithms approaches. 
