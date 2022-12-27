from collections import deque

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        r = []

        w_l = len(words[0])
        w_d = {}

        for w in words:
            if w in w_d:
                w_d[w] += 1
            else:
                w_d[w] = 1

        t_l = w_l * len(words)

        for i in range(w_l):
            t_d = w_d.copy()
            q = deque()
            for j in range(i, len(s) - w_l + 1, w_l):
                w = s[j:j + w_l]
                if w in t_d and t_d[w] > 0:
                    t_d[w] -= 1
                    q.append(w)
                    if sum(t_d.values()) == 0:
                        r.append(j - t_l + w_l)
                        p_w = q.popleft()
                        t_d[p_w] = 1 if p_w not in t_d else t_d[p_w] + 1
                else:
                    while len(q):
                        p_w = q.popleft()
                        if p_w == w:
                            q.append(w)
                            break
                        else:
                            t_d[p_w] = 1 if p_w not in t_d else t_d[p_w] + 1
                            if t_d[p_w] > w_d[p_w]:
                                t_d = w_d.copy()
        return r
