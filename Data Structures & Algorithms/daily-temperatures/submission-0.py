class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexStack = []
        final = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while (indexStack) and temperatures[indexStack[-1]] < temperatures[i]:
                popped = indexStack.pop()
                final[popped] = i - popped
            final[i] = 0
            indexStack.append(i)
        return final

            