from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        max_count = 0
        most_task = -1
        for task in tasks:
            freq[task] += 1
            if freq[task] > most_task:
                most_task = freq[task]
                max_count = 1
            elif freq[task] == most_task:
                max_count += 1
        
        return max(len(tasks), (n + 1) * (most_task - 1) + 
max_count)
