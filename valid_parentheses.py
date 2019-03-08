class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pare_l = ['(', '[', '{']
        pare_r = [')', ']', '}']
        if len(s) % 2 != 0:
            return False
        tmp = []
        for e in s:
            if e in pare_l:
                tmp.append(e)
            elif e in pare_r:
                if len(tmp) != 0:
                    index_e = pare_r.index(e)
                    if tmp[-1] != pare_l[index_e]:
                        return False
                    else:
                        tmp.pop()
                else:
                    return False

        return True if len(tmp) == 0 else False

    def is_valid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        pars = [None]
        par_dic = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in par_dic:
                if par_dic[c] != pars.pop():
                    return False
            else:
                pars.append(c)

        return len(pars) == 1
