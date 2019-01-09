from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def main():
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import json

    table_Datas = []
    for j in range(1,9):
        id = j
        url = "http://www.nepalstock.com/main/todays_price/index/%s" % id
        gethtml = requests.get(url)
        html = gethtml.text
        bs = BeautifulSoup(html, "lxml")
        table = bs.find('table',{'class':'table'})
        tr = table.findAll('tr')
        for td in tr:
            t_d = td.findAll('td')
            for tD in t_d:
                table_Datas.append(td.text.strip())       

    level1 = pd.Series(table_Datas).drop_duplicates().tolist()

    level2 = []
    for k in level1:
        if len(k)>35:
            level2.append(k)
        else:
            pass 

    d = []
    for l in range(1, len(level2)):
        c = level2[l].split("\n")
        d.append(c)

    df = pd.DataFrame(d[1:],columns=d[0])
    df.rename(columns={'Traded Companies': 'company_name','No. Of Transaction': 'no_of_transaction', 'Max Price':'max_price','Min Price':'min_price','Closing Price':'closing_price','Traded Shares':'traded_shares','Previous Closing':'previous_closing','Difference Rs.':'difference_rs'}, inplace=True)
    jsn = json.loads(df.to_json(orient='records'))
    return jsonify(jsn)
    # return Response(data: jsonify(jsn))

if __name__ == '__main__':
    app.run(debug=True)