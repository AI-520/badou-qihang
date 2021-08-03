from config import Dict


def calc_dag(sentence):
    DAG = {}
    N = len(sentence)
    for k in range(N):
        tmplist = []
        i = k
        frag = sentence[k]
        while i < N:
            if frag in Dict:
                tmplist.append(i)
            i += 1
            frag = sentence[k: i + 1]
        if not tmplist:
            tmplist.append(k)
        DAG[k] = tmplist
    return DAG


sentence = "经常有意见分歧"
print(calc_dag(sentence))


class DAGDecode:
    def __init__(self, sentence):
        self.sentence = sentence
        self.DAG = calc_dag(sentence)
        self.length = len(sentence)
        self.unfinish_path = [[]]
        self.finish_path = []

    def decode_next(self, path):
        path_length = len("".join(path))
        if path_length == self.length:
            self.finish_path.append(path)
            return
        candidates = self.DAG[path_length]
        new_paths = []
        for candidate in candidates:
            new_paths.append(path + [self.sentence[path_length:candidate + 1]])
        self.unfinish_path += new_paths
        return

    def decode(self):
        while self.unfinish_path != []:
            path = self.unfinish_path.pop()
            self.decode_next(path)


sentence = "经常有意见分歧"
test = DAGDecode(sentence)
test.decode()
print(test.finish_path)
