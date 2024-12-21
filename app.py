from flask import Flask, request, send_file
import pandas as pd

import visualize as vz

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1000 * 1000

def readData(file):
    if file.content_type == "application/vnd.ms-excel" or file.conennt_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        return pd.read_excel(file)
    elif file.content_type == "text/csv":
        return pd.read_csv(file)
    else:
        return None

@app.route("/", methods=["GET"])
def homePage():
    return ""

@app.route("/visualize",methos=["GET","POST"])
def visualize():
    pass

@app.route("/scatter",methods=["GET", "POST"])
def scatter():
    data = readData(request.files.get("dataset"))
    plt = vz.scatterPlot(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)