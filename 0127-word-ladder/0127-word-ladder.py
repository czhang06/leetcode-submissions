class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0
        
        dq = deque([(beginWord, 1)])
        words.discard(beginWord)

        while dq:
            word, steps = dq.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    nxt = word[:i] + letter + word[i+1:]
                    if nxt in words:
                        words.remove(nxt)
                        dq.append((nxt, steps + 1))
        
        return 0