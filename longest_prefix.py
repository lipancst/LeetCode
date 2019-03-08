class Solution(object):
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        index = len(strs[0])
        for e1, e2 in zip(strs, strs[1:]):
            count = 0
            for i in xrange(min(len(e1), len(e2))):
                if e1[i] == e2[i]:
                    count += 1
            if index > count:
                index = count
        if index == 0:
            return ""
        else:
            return strs[0][0:index]

    def longest_common_prefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]
        return min(strs)
