class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for char in s:
                chars[ord(char)-97] += 1
            map[tuple(chars)].append(s)
        result = []
        for val in map.values():
            result.append(val)
        return result
