import sys
import json
import random


class KMeansCluster:
    def __init__(self, sentences, cluster_num):
        self.sentences = sentences
        self.cluster_num = cluster_num
        self.points = self.pick_start_point(sentences, cluster_num)
        self.buffer = {}

    def cluster(self):
        result = []
        for i in range(self.cluster_num):
            result.append([])
        for item in self.sentences:
            distance_min = sys.maxsize
            index = -1
            for i in range(len(self.points)):
                distance = self.distance(item, self.points[i])
                if distance < distance_min:
                    distance_min = distance
                    index = i
            result[index] = result[index] + [item]
        new_center = []
        distances = []
        for item in result:
            center, distance_to_all = self.center(item)
            new_center.append(center)
            distances.append(distance_to_all)

        if (self.points == new_center):
            return result
        self.points = new_center
        return self.cluster()

    def center(self, cluster_sentences):
        center = "             "
        distance_to_all = 999999
        for sentence_a in cluster_sentences:
            distance = 0
            for sentence_b in cluster_sentences:
                distance += self.distance(sentence_a, sentence_b)
            distance /= len(sentences)
            if distance < distance_to_all:
                center = sentence_a
                distance_to_all = distance
        return center, distance_to_all

    def distance(self, p1, p2):
        if p1 + p2 in self.buffer:
            return self.buffer[p1 + p2]
        elif p1 + p2 in self.buffer:
            return self.buffer[p2 + p1]
        else:
            distance = 1 - len(set(p1) & set(p2)) / len(set(p1).union(set(p2)))
            self.buffer[p1 + p2] = distance
            return distance

    def pick_start_point(self, sentences, cluster_num):
        return random.sample(sentences, cluster_num)


def load_sentence(path):
    sentences = []
    with open(path, encoding="utf8") as f:
        for index, line in enumerate(f):
            line = json.loads(line)
            title, content = line["title"], line["content"]
            sentences.append(title)
    return sentences


sentences = load_sentence("../下午/tag_news.json")
km = KMeansCluster(sentences, 50)
res = km.cluster()
print(json.dumps(res, ensure_ascii=False, indent=2))
