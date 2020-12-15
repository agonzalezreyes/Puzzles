"""
Gas Station
There are N gas stations along a circular route, where the amount of gas at station i is A[i].
You have a car with an unlimited gas tank and it costs B[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station’s index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Example 1:
A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 1, 2]
For i = 4: A[3] = 4 and B[4] = 1; need
So, to go to index = 5, A[3] > B[3] => 4 > 1. So, A[3] - B[3] = 4 - 1 = 3, so it does work and we would have 3 units of gas extra.

Example 2:
A = [1, 2]
B = [2, 1]
For i = 0, A[0] = 1 and B[0] = 2. So B[0] > A[0], A[0] - B[0] = -1. Does not work.
"""

def canCompleteCircuit(A, B):
    if (len(A) == 0):
        return -1
    if (len(A) == 1):
        return -1 if A[0] - B[0] < 0 else 0

    # we will loop array and increment var end until var end reaches the same value as var start
    start = 0
    end = 1

    # gas at any point, if it becomes negative then we increament var start by 1
    curr_gas = A[start] - B[start];

    # to loop in the array, instead of using n=n+1, use n=(n+1)%length
    # so that when we get to the end of the array, it will start from zero.
    while start != end:
        
        while curr_gas < 0 and start != end: # gas level is negative
            # remove the previous start gas since it does not work (is negative)
            curr_gas = curr_gas - (A[start] - B[start])
            start = (start + 1) % len(A)
            
            if (start == 0): # no solution, we came back to start = 0
                return -1

        # add the gas of the station we are at now
        curr_gas += (A[end] - B[end])
        end = (end + 1) % len(A)

    if curr_gas < 0:
        return -1

    return start


from util import Testing as t

tests = t.Testing("Gas Station: canCompleteCircuit")

A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 1, 2]
tests.addTest(3, canCompleteCircuit, (A, B))

A = [1, 2]
B = [2, 1]
tests.addTest(1, canCompleteCircuit, (A, B))

tests.run()
