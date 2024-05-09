import plotly.graph_objs as go


## Visualize the probabability of the Monty Hall Problem
## X represents the strategy taken.
## Y Represents the probability of each strategy.
data = [go.Bar(x=['Switch', 'Stay'], y=[2/3, 1/3])]
layout = go.Layout(title='Monty Hall Problem',
                   xaxis=dict(title='Strategy'),
                   yaxis=dict(title='Probability of Winning'),
                   showlegend=False)
fig = go.Figure(data=data, layout=layout)
## fig.show()  <-- Uncomment here. ##


## Visualize using a pie chart instead.
pie_data = [go.Pie(labels=['Win', 'Lose'], values=[2, 1])]
pie_layout = go.Layout(title='Monty Hall Problem',
                       showlegend=False)
pie_fig = go.Figure(data=pie_data, layout=pie_layout)
pie_fig.show()

