# SEARCH-NEARBY

Problem Statement

The l∞-distance between two points – p1 = (x1, y1) and p2 = (x2, y2), denoted by ∥p1 − p2∥∞, is defined as max(|x1 − x2|, |y1 − y2|). Given a list S of n data points in R2, a query point q ∈ R2, and a non-negative numberd,wewishtofindtheset{p∈S|∥p−q∥∞ ≤d},thesetofallpointsinSthatareatmostan l∞-distance d away from the point q. You are required to design and program an appropriate data structure, which we call PointDatabase, to store a set of data points that admits the following.
3
1. An algorithm which, given a list S of data points, outputs an object R(S) of PointDatabase which is a “representation” of S.
2. An algorithm which, given the object R(S) of PointDatabase, a query point q, and a distance d, outputstheset{p∈S|∥p−q∥∞ ≤d}.

   
More specifically, your task is to implement a Python class PointDatabase with the following methods.

•init (self, pointlist): A constructor which, given a list pointlist of pairs of numbers, creates an object of PointDatabase. This method must run in time O(nlogn), where n is the number of points in pointlist.
•searchNearby(self, q, d): An accessor method which, given a point q and distance d, returns the list of all points, in the set that self represents, that are at l∞-distance at most d from q (arranged in an arbitrary order). This method must run in time O(m + log2 n), where n is the cardinality of the set of points that self represents, and m is the number of points returned.
For simplicity, you may assume the following.

1. The coordinates of all points involved are integers (thus, avoiding floats and the resulting errors).
2. In the list pointlist from which a PointDatabase object is constructed, no two data points have the
   same x-coordinate, and no two data points have the same y-coordinate.
3. No data point is at l∞-distance exactly d from the query point q.
