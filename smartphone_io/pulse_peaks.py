import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
# try to detect the pulse peaks
milk_data = pd.read_csv('pulse.csv')
time_series = milk_data['z']

peaks = find_peaks(time_series.map(lambda x: -x), threshold=0.08)
indices = peaks[0]
x = milk_data['time_stamp']

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=time_series,
    mode='lines+markers',
    name='Original Plot'
))
fig.add_trace(go.Scatter(
    x=x,
    y=milk_data['y'],
    mode='lines+markers',
    name='Original Plot'
))
fig.add_trace(go.Scatter(
    x=x,
    y=milk_data['x'],
    mode='lines+markers',
    name='Original Plot'
))

fig.add_trace(go.Scatter(
    x=[x[j] for j in indices],
    y=[time_series[j] for j in indices],
    mode='markers',
    marker=dict(
        size=8,
        color='red',
        symbol='cross'
    ),
    name='Detected Peaks'
))

fig.show()
