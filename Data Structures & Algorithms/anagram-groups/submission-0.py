class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for str in strs:
            cnt = [0] * 26
            for i in range(len(str)):
                cnt[ord(str[i]) - ord('a')] += 1
            group[tuple(cnt)].append(str)
        return list(group.values())