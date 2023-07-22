from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    
    nei = defaultdict(list)
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j+1:]
            nei[pattern].append(word)
    
    visit = set([beginWord])
    q = deque([beginWord])
    result = 1

    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return result
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for neiWord in nei[pattern]:
                    if neiWord not in visit:
                        visit.add(neiWord)
                        q.append(neiWord)
        result += 1
    return 0

