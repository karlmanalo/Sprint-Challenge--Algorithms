#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
The time requirements increase linearly as input size increases. One
additional calculation is made for each increase in n.

b) O(n log n)
The first loop runs in O(n) time.
The second loop runs in O(log n) time.

c) O(n)
At first glance, a recursive loop may seem to run with a time complexity of
greater than O(n), but in this example, the time requirements increase
linearly as the input size increases. One additional calculation is made for
each increase in n.

## Exercise II

I would approach this problem similar to how we approached our binary
searches. Given a building of n floors such that f is a floor from which eggs 
can be dropped without breaking, I would find the midpoint of the current 
search array (n/2 floors) and drop an egg from that floor. If the egg breaks, f
is a floor beneath us, so our new search array is now from 1 to n/2 (rather 
than from 1 to n). If the egg does not break, f is a floor above us, so our 
new search array is now from n/2 to n. We continue slicing our search array in
half in this manner until we find f, the maximum floor from which an egg can 
be dropped without breaking.

The time complexity of this search is O(log n).

