class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        wordLength = len(beginWord)

        mapping = defaultdict(list)

        for word in wordList:
            for i in range(wordLength):
                mapping[word[:i] + '*' + word[i+1:]].append(word)
        
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord:True}

        while queue:
            node, steps = queue.popleft()
            for i in range(wordLength):
                intermediate = node[:i] + "*" + node[i+1:]
                for neighbor in mapping[intermediate]:
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited[neighbor] = True
                        queue.append((neighbor,steps + 1))
                mapping[intermediate] = []
        return 0