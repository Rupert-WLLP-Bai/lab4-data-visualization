# 按照region进行可视化
import dash
import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# 声明一个Dash对象
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 从../dataset/college-salaries/salaries-by-region.csv读取数据
data = pd.read_csv('./dataset/college-salaries/salaries-by-region.csv')

# Get the list of regions for the dropdown options
regions = sorted(data['Region'].unique())

# Get the list of columns for the scatter and line plot dropdown options
scatter_columns = ['Starting Median Salary', 'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary',
                   'Mid-Career 25th Percentile Salary', 'Mid-Career 75th Percentile Salary',
                   'Mid-Career 90th Percentile Salary']
pie_columns = ['Starting Median Salary', 'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary',
               'Mid-Career 25th Percentile Salary', 'Mid-Career 75th Percentile Salary',
               'Mid-Career 90th Percentile Salary']

# 定义图表的颜色
colors = {
    'Starting Median Salary': '#1f77b4',
    'Mid-Career Median Salary': '#ff7f0e',
    'Mid-Career 10th Percentile Salary': '#2ca02c',
    'Mid-Career 25th Percentile Salary': '#d62728',
    'Mid-Career 75th Percentile Salary': '#9467bd',
    'Mid-Career 90th Percentile Salary': '#8c564b',
    # 六个指标画在一张图上
    'All': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'],
    # 散点图，使用渐变的颜色
    'Scatter': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
    # 折线图
    'Line': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
             '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
}
# Define the layout for the scatter and line plot dropdowns
scatter_layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='scatter-x-axis-dropdown',
            options=[{'label': c, 'value': c} for c in scatter_columns],
            value='Starting Median Salary',
        )], className='col-6'),
    html.Div([
        dcc.Dropdown(
            id='scatter-y-axis-dropdown',
            options=[{'label': c, 'value': c} for c in scatter_columns],
            value='Mid-Career Median Salary',
        )
    ], className='col-6'),
], className='row')

pie_layout = html.Div([
    html.Div([
        dcc.Dropdown(
            id='pie-dropdown',
            options=[{'label': c, 'value': c} for c in pie_columns],
            value='Starting Median Salary',
        )], className='col-6'),
], className='row')

new_scatter_layout = html.Div([
    dcc.Graph(id='new-scatter-plot', className='col-1',
              style={'width': '100%', 'display': 'inline-block'}),
], className='row')


# Define the layout
app.layout = html.Div(children=[
    html.H1(children='College Salaries by Region'),
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': r, 'value': r} for r in regions],
        value=regions[0]
    ),
    html.Div([
        dcc.Graph(id='starting-salary-graph', className='col-3',
                  style={'width': '33%', 'display': 'inline-block'}),
        dcc.Graph(id='mid-career-salary-graph', className='col-3',
                  style={'width': '33%', 'display': 'inline-block'}),
        dcc.Graph(id='mid-10th-percentile-salary-graph', className='col-3',
                  style={'width': '33%', 'display': 'inline-block'}),
    ], className='row'),
    html.Div([
        dcc.Graph(id='mid-25th-percentile-salary-graph', className='col-3',
                  style={'width': '33%', 'display': 'inline-block'}),
        dcc.Graph(id='mid-75th-percentile-salary-graph', className='col-3',
                  style={'width': '33%', 'display': 'inline-block'}),
        dcc.Graph(id='mid-90th-percentile-salary-graph', className='col-3',
                  style={'width': '33%', 'display': 'inline-block'}),
    ], className='row'),
    html.Div([
        dcc.Graph(id='all-salaries-graph', className='col-1',
                  style={'width': '100%', 'display': 'inline-block'}),
    ], className='row'),
    html.Div([
        scatter_layout,
        # 散点图
        dcc.Graph(id='scatter-plot-graph', className='col-1',
                  style={'width': '100%', 'display': 'inline-block'}),
    ], className='row'),
    html.Div([
        pie_layout,
        # 饼图
        dcc.Graph(id='pie-plot-graph', className='col-1',
                  style={'width': '100%', 'display': 'inline-block'}),
    ], className='row'),
    html.Div([
        new_scatter_layout,
    ], className='row'),
])


# Define the callback to update the starting salary graph based on the selected region
@app.callback(Output('starting-salary-graph', 'figure'), [Input('region-dropdown', 'value')])
def update_starting_salary_graph(selected_region):
    filtered_data = data[data['Region'] == selected_region]
    return {
        'data': [
            {'x': filtered_data['School Name'], 'y': filtered_data['Starting Median Salary'], 'type': 'bar',
             'name': 'Starting Median Salary', 'marker': {'color': colors['Starting Median Salary']}},
        ],
        'layout': {
            'title': f'Starting Salaries in {selected_region}',
            'xaxis': {'title': 'School Name', 'tickangle': 45, 'automargin': True, 'tickfont': {'size': 10}},
            'yaxis': {'title': 'Salary'},
            # 设置图表的高度
            'height': 600,
        }
    }


# Define the callback to update the mid-career salary graph based on the selected region
@app.callback(Output('mid-career-salary-graph', 'figure'), [Input('region-dropdown', 'value')])
def update_mid_career_salary_graph(selected_region):
    filtered_data = data[data['Region'] == selected_region]
    return {
        'data': [
            {'x': filtered_data['School Name'], 'y': filtered_data['Mid-Career Median Salary'], 'type': 'bar',
             'name': 'Mid-Career Median Salary', 'marker': {'color': colors['Mid-Career Median Salary']}},
        ],
        'layout': {
            'title': f'Mid-Career Salaries in {selected_region}',
            'xaxis': {'title': 'School Name', 'tickangle': 45, 'automargin': True, 'tickfont': {'size': 10}},
            'yaxis': {'title': 'Salary'},
            # 设置图表的高度
            'height': 600,
        }
    }


# Define the callback to update the mid-10th percentile salary graph based on the selected region
@app.callback(Output('mid-10th-percentile-salary-graph', 'figure'), [Input('region-dropdown', 'value')])
def update_mid_10th_percentile_salary_graph(selected_region):
    filtered_data = data[data['Region'] == selected_region]
    return {
        'data': [
            {'x': filtered_data['School Name'], 'y': filtered_data['Mid-Career 10th Percentile Salary'], 'type': 'bar',
             'name': 'Mid-Career 10th Percentile Salary',
             'marker': {'color': colors['Mid-Career 10th Percentile Salary']}},
        ],
        'layout': {
            'title': f'Mid-Career 10th Percentile Salaries in {selected_region}',
            'xaxis': {'title': 'School Name', 'tickangle': 45, 'automargin': True, 'tickfont': {'size': 10}},
            'yaxis': {'title': 'Salary'},
            # 设置图表的高度
            'height': 600,
        }
    }


# Define the callback to update the mid-25th percentile salary graph based on the selected region
@app.callback(Output('mid-25th-percentile-salary-graph', 'figure'), [Input('region-dropdown', 'value')])
def update_mid_25th_percentile_salary_graph(selected_region):
    filtered_data = data[data['Region'] == selected_region]
    return {
        'data': [
            {'x': filtered_data['School Name'], 'y': filtered_data['Mid-Career 25th Percentile Salary'], 'type': 'bar',
             'name': 'Mid-Career 25th Percentile Salary',
             'marker': {'color': colors['Mid-Career 25th Percentile Salary']}},
        ],
        'layout': {
            'title': f'Mid-Career 25th Percentile Salaries in {selected_region}',
            'xaxis': {'title': 'School Name', 'tickangle': 45, 'automargin': True, 'tickfont': {'size': 10}},
            'yaxis': {'title': 'Salary'},
            # 设置图表的高度
            'height': 600,
        }
    }


# Define the callback to update the mid-75th
@app.callback(Output('mid-75th-percentile-salary-graph', 'figure'), [Input('region-dropdown', 'value')])
def update_mid_75th_percentile_salary_graph(selected_region):
    filtered_data = data[data['Region'] == selected_region]
    return {
        'data': [
            {'x': filtered_data['School Name'], 'y': filtered_data['Mid-Career 75th Percentile Salary'], 'type': 'bar',
             'name': 'Mid-Career 75th Percentile Salary',
             'marker': {'color': colors['Mid-Career 75th Percentile Salary']}},
        ],
        'layout': {
            'title': f'Mid-Career 75th Percentile Salaries in {selected_region}',
            'xaxis': {'title': 'School Name', 'tickangle': 45, 'automargin': True, 'tickfont': {'size': 10}},
            'yaxis': {'title': 'Salary'},
            # 设置图表的高度
            'height': 600,
        }
    }


# Define the callback to update the mid-90th
@app.callback(Output('mid-90th-percentile-salary-graph', 'figure'), [Input('region-dropdown', 'value')])
def update_mid_90th_percentile_salary_graph(selected_region):
    filtered_data = data[data['Region'] == selected_region]
    return {
        'data': [
            {'x': filtered_data['School Name'], 'y': filtered_data['Mid-Career 90th Percentile Salary'], 'type': 'bar',
             'name': 'Mid-Career 90th Percentile Salary',
             'marker': {'color': colors['Mid-Career 90th Percentile Salary']}},
        ],
        'layout': {
            'title': f'Mid-Career 90th Percentile Salaries in {selected_region}',
            'xaxis': {'title': 'School Name', 'tickangle': 45, 'automargin': True, 'tickfont': {'size': 10}},
            'yaxis': {'title': 'Salary'},
            # 设置图表的高度
            'height': 600,
        }
    }


# Define the callback to update the all salaries graph based on the selected region
@app.callback(Output('all-salaries-graph', 'figure'), [Input('region-dropdown', 'value')])
def update_all_salaries_graph(selected_region):
    filtered_data = data[data['Region'] == selected_region]
    return {
        'data': [
            {'x': filtered_data['School Name'], 'y': filtered_data['Starting Median Salary'], 'type': 'bar',
             'name': 'Starting Median Salary', 'marker': {'color': colors['Starting Median Salary']}},
            {'x': filtered_data['School Name'], 'y': filtered_data['Mid-Career Median Salary'], 'type': 'bar',
             'name': 'Mid-Career Median Salary', 'marker': {'color': colors['Mid-Career Median Salary']}},
            {'x': filtered_data['School Name'], 'y': filtered_data['Mid-Career 10th Percentile Salary'], 'type': 'bar',
             'name': 'Mid-Career 10th Percentile Salary',
             'marker': {'color': colors['Mid-Career 10th Percentile Salary']}},
            {'x': filtered_data['School Name'], 'y': filtered_data['Mid-Career 25th Percentile Salary'], 'type': 'bar',
             'name': 'Mid-Career 25th Percentile Salary',
             'marker': {'color': colors['Mid-Career 25th Percentile Salary']}},
            {'x': filtered_data['School Name'], 'y': filtered_data['Mid-Career 75th Percentile Salary'], 'type': 'bar',
             'name': 'Mid-Career 75th Percentile Salary',
             'marker': {'color': colors['Mid-Career 75th Percentile Salary']}},
            {'x': filtered_data['School Name'], 'y': filtered_data['Mid-Career 90th Percentile Salary'], 'type': 'bar',
             'name': 'Mid-Career 90th Percentile Salary',
             'marker': {'color': colors['Mid-Career 90th Percentile Salary']}},
        ],
        'layout': {
            'title': f'Salaries in {selected_region}',
            'xaxis': {'title': 'School Name', 'tickangle': 45, 'automargin': True, 'tickfont': {'size': 10}},
            'yaxis': {'title': 'Salary'},
            # 设置图表的高度
            'height': 600,
        }
    }


# Define the callback to update the scatter plot based on the selected x-axis and y-axis
@app.callback(
    Output('scatter-plot-graph', 'figure'),
    [Input('region-dropdown', 'value'), Input('scatter-x-axis-dropdown', 'value'),
     Input('scatter-y-axis-dropdown', 'value')]
)
def update_scatter_plot(selected_region, x_axis_column, y_axis_column):
    filtered_data = data[data['Region'] == selected_region]
    return {
        'data': [
            {
                'x': filtered_data[x_axis_column],
                'y': filtered_data[y_axis_column],
                'type': 'scatter',
                'mode': 'markers'
            }
        ],
        'layout': {
            'title': f'Scatter Plot of {y_axis_column} vs. {x_axis_column} for {selected_region} Colleges',
            'xaxis': {'title': x_axis_column},
            'yaxis': {'title': y_axis_column}
        }
    }


# Define the callback to update the pie chart based on the selected region
@app.callback(Output('pie-plot-graph', 'figure'), [Input('region-dropdown', 'value'), Input('pie-dropdown', 'value')])
def update_pie_plot(selected_region, pie_plot_column):
    filtered_data = data[data['Region'] == selected_region]
    # 去除filter_data中的美元符号和逗号, 并转换为float类型
    # 先拷贝一份数据, 避免修改原始数据
    filtered_data = filtered_data.copy()
    filtered_data[pie_plot_column] = filtered_data[pie_plot_column].str.replace(
        '$', '', regex=False)
    filtered_data[pie_plot_column] = filtered_data[pie_plot_column].str.replace(
        ',', '', regex=False)
    filtered_data[pie_plot_column] = filtered_data[pie_plot_column].astype(
        float)

    return {
        'data': [
            {
                'labels': filtered_data['School Name'],
                'values': filtered_data[pie_plot_column],
                'type': 'pie',
                'textinfo': 'label+percent',
                'insidetextorientation': 'radial'
            }
        ],
        'layout': {
            'title': f'Pie Chart of {pie_plot_column} for {selected_region} Colleges',
            'height': 1500,
            # 自动调整图表的大小
            'autosize': True
        }
    }


import plotly.colors

@app.callback(Output('new-scatter-plot', 'figure'), [Input('region-dropdown', 'value')])
def update_new_scatter_plot(selected_region):
    filtered_data = data[data['Region'] == selected_region].copy()

    # 处理数据，去除符号并转换为float类型
    for column in scatter_columns:
        filtered_data[column] = filtered_data[column].str.replace('$', '', regex=False)
        filtered_data[column] = filtered_data[column].str.replace(',', '', regex=False)
        filtered_data[column] = filtered_data[column].astype(float)

    # 计算纵坐标对应的点大小
    min_salary = filtered_data[scatter_columns].min().min()
    max_salary = filtered_data[scatter_columns].max().max()

    scatter_data = []
    color_scale = plotly.colors.sequential.Viridis  # 使用Viridis渐变色
    for i, column in enumerate(scatter_columns):
        normalized_sizes = 30 + 30 * ((filtered_data[column] - min_salary) / (max_salary - min_salary))
        scatter_data.append({
            'x': filtered_data['School Name'],
            'y': [column] * len(filtered_data),
            'type': 'scatter',
            'mode': 'markers',
            'name': column,
            'marker': {
                'size': normalized_sizes,
                'color': filtered_data[column],  # 使用属性列的值作为颜色
                'colorscale': color_scale,  # 使用Viridis渐变色
            }
        })

    return {
        'data': scatter_data,
        'layout': {
            'title': f'Scatter Plot of Salaries for {selected_region} Colleges',
            'xaxis': {'title': 'School Name'},
            'yaxis': {'title': 'Salary Type', 'tickmode': 'array', 'tickvals': scatter_columns, 'ticktext': scatter_columns},
            'height': 600,
            'legend': {
                'x': 1.02,  # 调整图例的水平位置
                'y': 1  # 调整图例的垂直位置
            }
        }
    }

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
