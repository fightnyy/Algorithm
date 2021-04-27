#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_list = collections.defaultdict(list)

        for word in strs:
            s_list["".join(sorted(word))].append(word)
        return s_list.values()
