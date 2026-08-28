class Solution:
    def groupAnagrams(self, strs: List[str]):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return [v for v in ans.values()]