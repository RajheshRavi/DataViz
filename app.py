from flask import Flask, request, send_file
import pandas as pd
import io

import visualize as vz

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1000 * 1000

def readData(file):
    if file.content_type == "application/vnd.ms-excel" or file.content_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        return pd.read_excel(file)
    elif file.content_type == "text/csv":
        return pd.read_csv(file)
    else:
        return None

@app.route("/", methods=["GET"])
def homePage():
    return ""

@app.route("/visualize",methods=["GET","POST"])
def visualize():
    pass

@app.route("/scatter",methods=["GET", "POST"])
def scatter():
    data = readData(request.files.get("dataset"))
    plt = vz.scatterPlot(data)
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    return send_file(img, mimetype="image/png")

@app.route("/piechart",methods=["GET", "POST"])
def pie():
    data = readData(request.files.get("dataset"))
    plt = vz.pieChart(data)
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    return send_file(img, mimetype="image/png")

@app.route("/lineplot",methods=["GET", "POST"])
def line():
    data = readData(request.files.get("dataset"))
    plt = vz.linePlot(data)
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    return send_file(img, mimetype="image/png")

@app.route("/boxplot",methods=["GET", "POST"])
def box():
    data = readData(request.files.get("dataset"))
    plt = vz.boxPlot(data)
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    return send_file(img, mimetype="image/png")

@app.route("/heatmap",methods=["GET", "POST"])
def heat():
    data = readData(request.files.get("dataset"))
    plt = vz.heatMap(data)
    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)
    return send_file(img, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)