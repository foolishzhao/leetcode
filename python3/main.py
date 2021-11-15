import heapq
import functools
from typing import List
import itertools
import collections
import math
import random
import bisect
from python3.common.define import TreeNode
from functools import reduce
import operator
import functools

from functools import reduce, lru_cache
import operator
import time
from typing import Optional
from python3.common.define import ListNode


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, gl = ListNode(), 1
        p.next = head
        while p:
            cl = gl
            if gl % 2 == 1:
                while p and cl:
                    p = p.next
                    cl -= 1
            else:
                q = p.next
                p.next = None
                while q and cl:
                    t = q.next
                    q.next = p.next
                    p.next = q
                    q = t
                    cl -= 1
                while p.next:
                    p = p.next
                p.next = q
            gl += 1

        return head
