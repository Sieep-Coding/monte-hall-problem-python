import plotly.graph_objs as go

data = [go.Bar(x=['Switch', 'Stay'], y=[2/3, 1/3])]

layout = go.Layout(title='Monty Hall Problem',
                   xaxis=dict(title='Strategy'),
                   yaxis=dict(title='Probability of Winning'),
                   showlegend=False)

fig = go.Figure(data=data, layout=layout)
fig.show()