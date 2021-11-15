from typing import List


class Solution:
    # Create a vector named sessions. The len of which denotes the number of work sessions we currently have,
    # and sessions[i] denotes the number of work hours we have completed in the ith session.
    #
    # Each task in the tasks array has two options:
    # Get included in one of the session in sessions
    # Get included in a new session by adding one to the sessions.
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort(reverse=True)  # handle big task 1st could save dfs cost

        n, res, sessions = len(tasks), len(tasks), list()

        def dfs(pos):
            nonlocal res
            if len(sessions) >= res:
                return

            if pos == n:
                res = len(sessions)
                return

            for i, sess in enumerate(sessions):
                if sess + tasks[pos] <= sessionTime:
                    sessions[i] += tasks[pos]
                    dfs(pos + 1)
                    sessions[i] -= tasks[pos]

            sessions.append(tasks[pos])
            dfs(pos + 1)
            sessions.pop()

        dfs(0)
        return res
