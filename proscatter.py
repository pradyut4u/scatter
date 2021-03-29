import pandas as pd
import plotly_express as pe

df = pd.read_csv(r"D:/python/Data-visualization-master/csv files/covid.csv")
diagram = pe.scatter(df,x="date",y="cases",color="country")
diagram.show()