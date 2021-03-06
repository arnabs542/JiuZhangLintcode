# 391. Number of Airplanes in the Sky
# 中文English
# Given an list interval, which are taking off and landing time of the flight.
# How many airplanes are there at most at the same time in the sky?
#
# Example
# Example 1:
#
# Input: [(1, 10), (2, 3), (5, 8), (4, 7)]
# Output: 3
# Explanation:
# The first airplane takes off at 1 and lands at 10.
# The second ariplane takes off at 2 and lands at 3.
# The third ariplane takes off at 5 and lands at 8.
# The forth ariplane takes off at 4 and lands at 7.
# During 5 to 6, there are three airplanes in the sky.
# Example 2:
#
# Input: [(1, 2), (2, 3), (3, 4)]
# Output: 1
# Explanation: Landing happen before taking off.
# Notice
# If landing and taking off of different planes happen at the same time, we consider landing should happen at first.

#
# 391. 数飞机
# 中文English
# 给出飞机的起飞和降落时间的列表，用序列 interval 表示. 请计算出天上同时最多有多少架飞机？
# 如果一架飞机的降落时间恰好等于另一架飞机的起飞时间，则认为先降落。
#
# Example
# 样例 1:
#
# 输入: [(1, 10), (2, 3), (5, 8), (4, 7)]
# 输出: 3
# 解释:
# 第一架飞机在1时刻起飞, 10时刻降落.
# 第二架飞机在2时刻起飞, 3时刻降落.
# 第三架飞机在5时刻起飞, 8时刻降落.
# 第四架飞机在4时刻起飞, 7时刻降落.
# 在5时刻到6时刻之间, 天空中有三架飞机.
# 样例 2:
#
# 输入: [(1, 2), (2, 3), (3, 4)]
# 输出: 1
# 解释: 降落优先于起飞.
# Notice
# 如果多架飞机降落和起飞在同一时刻，我们认为降落有优先权。

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        points = []
        for airplane in airplanes:
            points.append((airplane.start, 1))
            points.append((airplane.end, -1))

        number_of_airplane, max_number_of_airplan = 0, 0
        for _, count_delta in sorted(points):
            number_of_airplane += count_delta
            max_number_of_airplan = max(max_number_of_airplan, number_of_airplane)

        return max_number_of_airplan
    