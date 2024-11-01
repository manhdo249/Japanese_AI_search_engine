import json


tf_path = r'Japan_data\tf_idf_dict.json'
ds_path = r'Japan_data\ds.json'
doc_path = r'Japan_data\docs.json'


def get_tfidf_dict(tf_idf_path):
    def json_line_reader(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                yield json.loads(line.strip())
    # Load
    tf_idf_dict = {}
    for item in json_line_reader(tf_idf_path):
        tf_idf_dict.update(item)
    return tf_idf_dict


tf_idf_dict = get_tfidf_dict(tf_path)

with open(ds_path, 'r') as f:
    ds = json.load(f)

with open(doc_path, 'r') as f:
    data = json.load(f)
docs = data['docs']


class TFIDF():
    def __init__(self):
        # Load
        self.tf_idf_dict = tf_idf_dict
        self.ds = ds
        self.docs = docs

    def search(self, q, k=10):
        def tf_idf_score(word, doc_idx):
            if word in self.tf_idf_dict:
                if str(doc_idx) in self.tf_idf_dict[word]:
                    return self.tf_idf_dict[word][str(doc_idx)]
                else:
                    return 0.0
            else:
                return 0.0
        # Search documents using TF-IDF
        finals = []
        # print(self.tf_idf_dict)
        # Lặp qua những văn bản
        for i in range(len(self.docs)):
            if self.ds[str(i)] == 0:
                continue
            score = 0
            # Lặp qua các từ trong truy vấn
            for t in q.split():
                t = t.lower()
                score += tf_idf_score(t, i) / self.ds[str(i)]
                finals.append((score, i))
        final_sort = sorted(finals, key=lambda x: -x[0])
        results = [self.docs[i] for _, i in final_sort[:k]]
        return results
