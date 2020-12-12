


from flask import Flask, request
from flask import jsonify
from gettingComments import get_id
from gettingComments import get_comments

from gettingStats import getting_statistics
from gettingShares import get_channel_id
from gettingShares import video_share_count
from sentimentEngine import SentimentAnalysis
from csv import writer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/end", methods=["GET"])
def collectSentiment():
    get
    result = []
    corpus = open("final_result.csv").read()
    data = corpus.split('\n')
    # print(self.data)
    del data[-1]
    for row in data:
        rows = row.split(',')
        result.append(rows[0])
    return jsonify({
        "postivePercent":result[0],
        "negativePercent": result[1],
        "neutralPercent": result[2],
        "overallPercent": result[3]
        })

@app.route('/start', methods=['GET'])
def collectdetail():

    api_key = "AIzaSyB2aP-k5RgREln1UKM1q_QCRrh_JA4sSvM"

    # id = get_id('https://www.youtube.com/watch?v=O7SOpGwDVcY')
    # id = get_id("https://www.youtube.com/watch?v=geL6eYSUNvo")
    id = str(request.args.get('id'))
    print(id)
    # comments = get_comments(api_key=api_key, part='snippet', maxResults=10, textFormat='plainText', order='time', videoId=id)
    
    
    info = getting_statistics(id, api_key)
    # COMMENTS = comments["Comments"]
    
    # l1 = SentimentAnalysis(COMMENTS)
    # word = l1.sentiWordNetAnalysis()
    # comments["score"] = word["score"]
    # emoji = l1.emojiSentimentAnalysis()


    # posWord = word["postiveCount"]
    # negWord = word["negativeCount"]
    # neuWord = word["neutralCount"]
    # totalWord = posWord + negWord + neuWord
    # poswp = (posWord /totalWord) * 100
    # negwp = (negWord /totalWord) * 100
    # neuwp = (neuWord /totalWord) * 100


    # posemoji = (emoji["postiveCount"])/4
    # negemoji = (emoji["negativeCount"])/4
    # neuemoji = (emoji["neutralCount"])/4

    # totalemoji = posemoji + negemoji + neuemoji
    # if totalemoji != 0:
    #     posep = (posemoji /totalemoji) * 100
    #     negep = (negemoji /totalemoji) * 100
    #     neuep = (neuemoji /totalemoji) * 100
    #     poswp = (poswp + posep)/ 2
    #     negwp = (negwp + negep)/ 2
    #     neuwp = (neuwp + neuep)/ 2

    # posTotal = poswp
    # negTotal = negwp
    # neuTotal = neuwp
    # overallTotal = (posTotal - negTotal) + neuTotal 
    # with open(f'{"final_result"}.csv', 'w+') as f:
    #             # https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/#:~:text=Open%20our%20csv%20file%20in,in%20the%20associated%20csv%20file
    #     csv_writer = writer(f)
    #     csv_writer.writerow([int(posTotal)])
    #     csv_writer.writerow([int(negTotal)])
    #     csv_writer.writerow([int(neuTotal)])
    #     csv_writer.writerow([int(overallTotal)])

    # response = {
    #     "comments": comments,
    #     "info": info,
    # }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)