import pandas as pd
import plotly.figure_factory as ff
import statistics as st
import plotly.graph_objects as go
import random

reader = pd.read_csv('hwData.csv')
data = reader['claps'].tolist()
means = []

for x in range(0,1000):
    list = []
    for i in range(0,30):
        x = random.randint(1,len(data)-1)
        list.append(data[x])
    means.append(st.mean(list))

print(st.mean(data))
mean = st.mean(means)
print(mean)
fig = ff.create_distplot([means],['result'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.004]))
fig.show()