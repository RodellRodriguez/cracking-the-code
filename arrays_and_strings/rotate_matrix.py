'''
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''

'''
4x4 matrix

1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16

turns into

13 9  5 1
14 10 6 2
15 11 7 3
16 12 8 4

1 (0,0) -> (0,3)     5 (1,0) -> (0,2)   9 (2,0) -> (0,1)
2 (0,1) -> (1,3)     6 (1,1) -> (1,2)   10 (2,1) -> (1,1)
3 (0,2) -> (2,3)     7 (1,2) -> (2,2)   11 (2,2) -> (2,1)
4 (0,3) -> (3,3)     8 (1,3) -> (3,2)   12 (2,3) -> (3,1)

Algorithm for x1,y1 -> x2,y2 is: x2=y1 and y2=(N-1-x1)

This algorithm copies the the values into a new matrix.
Time Complexity is O(N) and Space Complexity is O(N)

Can we do this in place to reduce Space Complexity to O(1)?

The way to do it is rotate the outer layer of the the NxN matrix and then move onto the inner layer until no layers are left.
The way the layers would rotate is that each layer is comprised of 4 parts: top (1,2,3,4), right (4,8,12,16), bottom (13,14,15,16)
and left (1,5,9,13). You save the value at top then: swap left into top, bottom into left, right into bottom, and finally the saved value
of top into right. You do this for the entirety of the array of top then then move onto the inner layer and repeat.

The issue is how to figure out the idicies in the for loops. Im still confused by how to keep track of all the indicies

'''
