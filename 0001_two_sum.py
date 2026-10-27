"""
LeetCode Problem #1: Two Sum
Difficulty: Easy
Category: Arrays & Hashing

Problem Statement:
    Given an array of integers 'nums' and an integer 'target', return indices of 
    the two numbers such that they add up to 'target'.
    You may assume that each input would have exactly one solution, and you 
    may not use the same element twice.

Complexity Analysis:
    - Time Complexity: O(N) where N is the number of elements in 'nums'. 
      We traverse the list containing N elements exactly once. Each lookup in the table costs O(1) time.
    - Space Complexity: O(N) to store the elements in the hash map (dictionary).
"""

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store the value as key and its index as value
        visited_map = {}

        for current_index, current_num in enumerate(nums):
            # Compute the required complement to reach the target
            complement = target - current_num

            # Check if the complement has already been seen in the array
            if complement in visited_map:
                # Return the index of the complement and the current index
                return [visited_map[complement], current_index]

            # Otherwise, store the current number and its index in the hash map
            visited_map[current_num] = current_index

        # Return empty list if no solution is found (though problem guarantees one exists)
        return []


if __name__ == "__main__":
    # Test case to verify correctness
    solver = Solution()

    test_nums = [2, 7, 11, 15]
    test_target = 9

    output = solver.twoSum(test_nums, test_target)
    print(f"Input Array: {test_nums} | Target: {test_target}")
    print(f"Output Indices: {output} (Expected: [0, 1])")
