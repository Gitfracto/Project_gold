import numpy as np #np.nan y mucho mas
import pandas as pd #dataframe y mucho mas
import re

def clean_gmt(x):
    return x.replace("GMT+0200","").replace("GMT+0100","").replace("23:00:00.000","")

def cleaning_day(x):
    y = x.split('.')
    return int(y[0])

def cleaning_month(x):
    y = x.split('.')
    return int(y[1])

def cleaning_year(x):
    return int(re.findall(r'\b\d{4}\b',x)[0])

def clean_titles(x):
    return x.replace("PRECIOUS-","")

def clean_url(x):
    return "https://www.reuters.com" + x

def fecha():
    year = int(input("Coloque el año:"))
    month = int(input("Coloque el mes:"))
    day =  int(input("Coloque el dia:"))
    if year not in [2020,2021] or day not in list(range(1,32)) or month not in list(range(1,13)):
        return "Haz cometido un error al introducir alguno de los datos, por favor revise :)"
    a =list(colec1.find({"$and":[ {"year": year, "month": month,"day":day}]}))
    b =list(colec2.find({"$and":[ {"year": year, "month": month,"day":day}]}))
    c =list(colec3.find({"$and":[ {"year": year, "month": month,"day":day}]}))
    bb = pd.DataFrame(b).drop(["_id"],axis=1)
    if a:
        aa = pd.DataFrame(a).drop(["_id"],axis=1)
        bb =pd.merge(aa,bb, how = "left")
    if c:
        cc = pd.DataFrame(c).drop(["_id"],axis=1)
        bb =pd.merge(bb,cc, how = "left")

    return bb