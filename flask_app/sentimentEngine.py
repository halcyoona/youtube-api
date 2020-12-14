
from nltk.corpus import wordnet as wnet
from nltk.corpus import sentiwordnet as swnet
from nltk.corpus import wordnet
import emoji
import regex as re
import nltk
from emosent import get_emoji_sentiment_rank



class SentimentAnalysis:
    data = ""
    X = []
    Y = []
    trainX = []
    trainY = []
    testX = []
    testY = []
    emojiList = []


    def __init__(self, lst):
        self.X = lst
        # print(self.X)


    def split_count(self):
        
        for text in self.X:
            text_de = emoji.demojize(text)
            emojis_list_de = re.findall(r'(:[!_\-\w]+:)', text_de)
            emojis = [emoji.emojize(x) for x in emojis_list_de]
            for i in emojis:
                self.emojiList.append(i)
        

    def emojiSentimentAnalysis(self):
        final_labels = []
        score_lst = []
        negCount = 0
        posCount = 0
        neuCount = 0
        for i in self.emojiList:
            pos_total = 0
            neg_total = 0
            if len(i) > 1:
                for j in i:
                    try:
                        response = get_emoji_sentiment_rank(j)
                    except KeyError:
                        continue
                    score = response['sentiment_score']
                    if score > 0:
                        pos_total += score
                    elif score < 0:
                        neg_total += score
            else:
                try:
                    response = get_emoji_sentiment_rank(i)
                except KeyError:
                    continue
                score = response['sentiment_score']
                if score > 0:
                    pos_total += score
                elif score < 0:
                    neg_total += score

            # print(i)
            # print(pos_total)
            # print(neg_total)
            

            if pos_total > abs(neg_total):
                # print('Pos')
                final_labels.append("POS")
                score_lst.append(pos_total)
                posCount += 1
            elif pos_total < abs(neg_total):
                # print('Neg')
                score_lst.append(neg_total)
                negCount += 1
                final_labels.append("NEG")
            else:
                neuCount += 1
                score_lst.append(0)
                # print('Neu')
                final_labels.append('NEU')
            # print('-----------')

        return {
            "negativeCount": negCount,
            "postiveCount": posCount,
            "neutralCount": neuCount,
            "score": score_lst 
        }
        # print(final_labels)

        # flag = 1
        # for k in range(len(final_labels)):
        #     if flag == 1:
        #         with open(f'{csv_filename}.csv', 'w+') as f:
        #         # https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/#:~:text=Open%20our%20csv%20file%20in,in%20the%20associated%20csv%20file
        #             csv_writer = writer(f)
        #             csv_writer.writerow([self.emojiList[k], final_labels[k]])
        #             flag = 0
        #     else:
        #     #7 write line by line
        #         with open(f'{csv_filename}.csv', 'a+') as f:
        #             # https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/#:~:text=Open%20our%20csv%20file%20in,in%20the%20associated%20csv%20file
        #             csv_writer = writer(f)
        #             csv_writer.writerow([self.emojiList[k], final_labels[k]])
        
    





    def sentiWordNetAnalysis(self):
        final_labels = []
        score_lst = []
        negCount = 0
        posCount = 0
        neuCount = 0
        for i in self.X:
            tokens = i.split(' ')
            pos_total = 0
            neg_total = 0
            for t in tokens:
                syn_t = wnet.synsets(t)
                if len(syn_t) > 0:
                    syn_t = syn_t[0]
                    senti_syn_t = swnet.senti_synset(syn_t.name())
                    if senti_syn_t.pos_score() > senti_syn_t.neg_score():
                        pos_total += senti_syn_t.pos_score()
                    else:
                        neg_total += senti_syn_t.neg_score()
            if pos_total > neg_total:
                final_labels.append("POS")
                score_lst.append(pos_total)
                posCount += 1
            elif pos_total < neg_total:
                final_labels.append("NEG")
                score_lst.append(-neg_total)
                negCount += 1
            else:
                neuCount += 1
                final_labels.append('NEU')
                score_lst.append(0)

        return {
            "negativeCount": negCount,
            "postiveCount": posCount,
            "neutralCount": neuCount,
            "score": score_lst 
        }
        # print(final_labels)
        # flag = 1
        # for k in range(len(final_labels)):
        #     if flag == 1:
        #         with open(f'{csv_filename}.csv', 'w+') as f:
        #         # https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/#:~:text=Open%20our%20csv%20file%20in,in%20the%20associated%20csv%20file
        #             csv_writer = writer(f)
        #             csv_writer.writerow([self.X[k], final_labels[k]])
        #             flag = 0
        #     else:
        #     #7 write line by line
        #         with open(f'{csv_filename}.csv', 'a+') as f:
        #             # https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/#:~:text=Open%20our%20csv%20file%20in,in%20the%20associated%20csv%20file
        #             csv_writer = writer(f)
        #             csv_writer.writerow([self.X[k], final_labels[k]])
        # # print('Accuracy Senti_word_net_Analysis : ', accuracy_score(self.Y, final_labels))

    


if __name__ == "__main__":
    sentifile = 'sentimentAnalysisComments'
    emojifile = 'sentimentAnalysisEmoji'
    lst = ["hello", "🤪", "I love you", "I hate you"]
    l1 = SentimentAnalysis(lst)
    response = l1.sentiWordNetAnalysis()
    # print(response)
    # l1.wordNetAnalysis()
    l1.split_count()
    # response = l1.emojiSentimentAnalysis()
    print(response)