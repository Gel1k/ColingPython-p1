import pickle
import tqdm
from corus import load_corpora


class UnigramMorphAnalyser:

    def __init__(self):
        self.path = None

    def __getitem__(self, token):
        stats = self.load()
        return stats[token]

    def train(self, path):
        self.path = path
        records = load_corpora(path)
        stats = {}

        for rec in tqdm.tqdm(records):
            for par in rec.pars:
                for sent in par.sents:
                    for token in sent.tokens:
                        for i in range(-4, 0):
                            text = token.text[i:]
                            token_pos = token.forms[0].grams[0]
                            if text in stats:
                                if token_pos in stats[text]:
                                    stats[text][token_pos] += 1
                                else:
                                    stats[text][token_pos] = 1
                            else:
                                stats[text] = {token_pos: 1}
        return stats

    def save(self, test_path):
        with open('model.pkl', 'wb') as handle:
            pickle.dump(self.train(test_path), handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self):
        with open('model.pkl', 'rb') as handle:
            stats = pickle.load(handle)
        return stats

    def predict(self, token='str'):
        stats = self.load()
        fin_stats = {}
        needed_range = min(4, len(token))

        for i in range(-needed_range, 0):
            text = token[i:]
            if text in stats:
                token_stats = stats[text]
                all_sum = sum(token_stats.values())
                for j in token_stats:
                    prob = token_stats[j] / all_sum
                    fin_stats[j] = prob
            else:
                continue

        fin_stats = dict(reversed(sorted(fin_stats.items(), key=lambda item: item[1])))
        return fin_stats

    def eval(self, eval_path='str'):
        model = self.load()
        test_data = load_corpora(eval_path)
        c = 0
        c_cor = 0

        for rec in tqdm.tqdm(test_data):
            for par in rec.pars:
                for sent in par.sents:
                    for token in sent.tokens:
                        analyzer_data = self.predict(token.text)
                        if len(analyzer_data) > 0:
                            c += 1
                            analyzer_output = list(analyzer_data)[0]
                            if analyzer_output == token.forms[0].grams[0]:
                                c_cor += 1
                        else:
                            continue
        return c_cor / c
