class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for words in strs:
            key="".join(sorted(words))

            if key in seen:
                seen[key].append(words)
            else:
                seen[key]=[words]

        return list(seen.values())

            