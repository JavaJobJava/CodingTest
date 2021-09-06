"""
@file sort-24.py
@brief 안테나
@desc 수학+정렬
"""
import sys

n = int(sys.stdin.readline().rstrip())

positions = list(map(int, sys.stdin.readline().rstrip().split()))

positions.sort()
print(positions[(n-1)//2])
