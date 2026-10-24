class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0
        
        front, back = {beginWord}, {endWord}
        words.discard(beginWord)
        words.discard(endWord)
        steps = 1

        while front and back:
            if len(front) > len(back):
                front, back = back, front

            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nxt =  word[:i] + c + word[i + 1:] 
                        if nxt in back:
                            return steps + 1
                        if nxt in words:
                            words.remove(nxt)
                            next_front.add(nxt)
            
            front = next_front
            steps += 1
        
        return 0
                        