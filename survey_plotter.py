import matplotlib.pyplot as plt
from pywaffle import Waffle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

def plot_pictogram():
    colorscale = [
    '#00FFFF','#00008B','#9370DB','#00008B','#BA55D3','#00008B','#FAFAFA'  # dark blue
    ]

    relationship_status = pd.read_csv('./data_clean/relation_ship_clean')


    fig = plt.figure(
        facecolor='#00008B',
        figsize=(8, 8),
        dpi=100,
        FigureClass=Waffle,
        rows=6,
        values=list(relationship_status['counts']),
        colors=colorscale,
        icons='person-dress',
        interval_ratio_x=1,
        interval_ratio_y=2.2,
        block_arranging_style='new-line',
        starting_location='SW'

    )

    # Define the labels for each category
    labels = ['Married', '', 'Single', '', 'In a relationship', '', 'Divorced']

    # Get the number of categories
    num_categories = len(labels)

    # Calculate the width of each category block
    block_width = 1.0 / num_categories

    plt.text(0.5, -0.1, 'Married', ha='center', va='center', color='#00FFFF', fontsize=11, weight='bold')
    plt.text(0.5, -0.2, '40%', ha='center', va='center', color='#00FFFF', fontsize=11, weight='bold')
    plt.text(1.65, -0.1, 'Single', ha='center', va='center', color='#9370DB', fontsize=11, weight='bold')
    plt.text(1.65, -0.2, '39%', ha='center', va='center', color='#9370DB', fontsize=11, weight='bold')
    plt.text(2.45, -0.1, 'In a relationship', ha='center', va='center', color='#BA55D3', fontsize=11, weight='bold')
    plt.text(2.45, -0.2, '15%', ha='center', va='center', color='#BA55D3', fontsize=11, weight='bold')
    plt.text(2.95, -0.1, 'Divorced', ha='center', va='center', color='#FAFAFA', fontsize=11, weight='bold')
    plt.text(2.95, -0.2, '6%', ha='center', va='center', color='#FAFAFA', fontsize=11, weight='bold')

    plt.text(0.85, 1.4, 'What is you relationship status?', ha='center', va='center', color='#FAFAFA', fontsize=16, weight='bold')
    plt.text(1.52, 1.3, '_______________________________________________________________', ha='center', va='center', color='#FAFAFA', fontsize=16, weight='bold')

    return fig

def plot_employment_status():
    question_score = pd.read_csv('./ChildlessnessNJ.csv')

    colorscale = ['#00FFFF', '#9370DB', '#BA55D3', '#00008B'] 

    # create data
    size_of_groups = question_score.value_counts('Employment Status').rename_axis('unique_values').reset_index(name='counts').counts
    group_names = question_score.value_counts('Employment Status').rename_axis('unique_values').reset_index(name='counts').unique_values
    percentages = ['52%', '36%', '9%', '3%']

    plt.figure(figsize=(6, 4))
    # Create a pie plot
    patches, texts = plt.pie(size_of_groups, labels=percentages, colors=colorscale, textprops={'fontsize': 18, 'weight': 'bold'})


    # Set the color for each label
    for text, color in zip(texts, colorscale):
        text.set_color(color)

    # Add a circle at the center to transform it into a donut chart
    my_circle = plt.Circle((0, 0), 0.6, color='#483D8B')
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    plt.gcf().set_facecolor('#483D8B')

    legend = plt.legend(group_names, loc='upper center', bbox_to_anchor=(0.5, 0), fontsize=12, frameon=False)
    plt.setp(legend.get_texts(), color='#FAFAFA', weight='bold')


    plt.text(0, 1.6, 'What is your employment status?', ha='center', va='center', color='#FAFAFA', fontsize=16, weight='bold')
    plt.text(0, 1.5, '______________________________________', ha='center', va='center', color='#FAFAFA', fontsize=16, weight='bold')

    return plt

def plot_children():
    colorscale = ['#00FFFF', '#483D8B'] 
    question_score = pd.read_csv('./ChildlessnessNJ.csv')


    # create data
    size_of_groups = question_score.value_counts('Currently have children').rename_axis('unique_values').reset_index(name='counts').counts
    group_names = question_score.value_counts('Currently have children').rename_axis('unique_values').reset_index(name='counts').unique_values
    percentages = ['60%', '40%']

    plt.figure(figsize=(8, 4), dpi=112)
    # Create a pie plot
    patches, texts = plt.pie(size_of_groups, labels=percentages, colors=colorscale, textprops={'fontsize': 18, 'weight': 'bold'})


    # Set the color for each label
    for text, color in zip(texts, colorscale):
        text.set_color(color)

    plt.gcf().set_facecolor('#9370DB')

    legend = plt.legend(group_names, loc='upper center', bbox_to_anchor=(0.5, 0), fontsize=12, frameon=False)
    plt.setp(legend.get_texts(), color='#FAFAFA', weight='bold')


    plt.text(-0.6, 1.6, 'Do you have children?', ha='center', va='center', color='#FAFAFA', fontsize=16, weight='bold')
    plt.text(0, 1.5, '______________________________________', ha='center', va='center', color='#FAFAFA', fontsize=16, weight='bold')


    return plt

def plot_financial_factors():
    colorscale = ['#9370DB', '#BA55D3'] 

    stacked_df = pd.read_csv("./data_clean/stacked_df_v2.csv")
    fig = px.bar(stacked_df[stacked_df['text'].isin(stacked_df['text'][:2])], x="0", y="text", color='hasChild', orientation='h', barmode='group', color_discrete_sequence=colorscale, text_auto=True)
    fig.update_layout(width=800, height=400, xaxis=dict(range=[1, 5]), yaxis=dict(visible=False), bargap=0.6, xaxis_title="Average rating", yaxis_title="Statements")

    annotations = []  # List to store annotations
    startplace = 0.4
    for i in stacked_df['text'][:2]:
        annotation = dict(
            x=1, y=startplace,
            text=f'<b>{i}</b>',
            font=dict(family="Arial", size=14, color="#FAFAFA"),
            showarrow=False,
            xanchor='left',
            align='left'
        )
        startplace += 1
        annotations.append(annotation)
    fig.update_layout(annotations=annotations, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')  # Add annotations to the figure
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.05,
        xanchor="left",
        x=0,
        traceorder="reversed",
        font=dict(size=14)
    ), legend_title_text='',
    
    )

    return fig

def plot_choice_factors():
    colorscale = ['#9370DB', '#BA55D3'] 

    stacked_df = pd.read_csv("./data_clean/stacked_df_v2.csv")
    fig = px.bar(stacked_df[stacked_df['text'].isin(stacked_df['text'][2:4])], x="0", y="text", color='hasChild', orientation='h', barmode='group', color_discrete_sequence=colorscale, text_auto=True)
    fig.update_layout(width=800, height=400, xaxis=dict(range=[1, 5]), yaxis=dict(visible=False), bargap=0.6, xaxis_title="Average rating", yaxis_title="Statements")

    annotations = []  # List to store annotations
    startplace = 0.4
    for i in stacked_df['text'][2:4]:
        annotation = dict(
            x=1, y=startplace,
            text=f'<b>{i}</b>',
            font=dict(family="Arial", size=14, color="#FAFAFA"),
            showarrow=False,
            xanchor='left',
            align='left'
        )
        startplace += 1
        annotations.append(annotation)
    fig.update_layout(annotations=annotations, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')  # Add annotations to the figure
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.05,
        xanchor="left",
        x=0,
        traceorder="reversed",
        font=dict(size=14)
    ), legend_title_text='',
    
    )

    return fig



def plot_external_influences_factors():
    colorscale = ['#9370DB', '#BA55D3'] 

    stacked_df = pd.read_csv("./data_clean/stacked_df_v2.csv")
    fig = px.bar(stacked_df[stacked_df['text'].isin(stacked_df['text'][4:6])], x="0", y="text", color='hasChild', orientation='h', barmode='group', color_discrete_sequence=colorscale, text_auto=True)
    fig.update_layout(width=800, height=400, xaxis=dict(range=[1, 5]), yaxis=dict(visible=False), bargap=0.6, xaxis_title="Average rating", yaxis_title="Statements")

    annotations = []  # List to store annotations
    startplace = 0.4
    for i in stacked_df['text'][4:6]:
        annotation = dict(
            x=1, y=startplace,
            text=f'<b>{i}</b>',
            font=dict(family="Arial", size=14, color="#FAFAFA"),
            showarrow=False,
            xanchor='left',
            align='left'
        )
        startplace += 1
        annotations.append(annotation)
    fig.update_layout(annotations=annotations, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')  # Add annotations to the figure
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.05,
        xanchor="left",
        x=0,
        traceorder="reversed",
        font=dict(size=14)
    ), legend_title_text='',
    
    )

    return fig



def plot_health_factors():
    colorscale = ['#9370DB', '#BA55D3'] 

    stacked_df = pd.read_csv("./data_clean/stacked_df_v2.csv")
    fig = px.bar(stacked_df[stacked_df['text'].isin(stacked_df['text'][6:8])], x="0", y="text", color='hasChild', orientation='h', barmode='group', color_discrete_sequence=colorscale, text_auto=True)
    fig.update_layout(width=800, height=400, xaxis=dict(range=[1, 5]), yaxis=dict(visible=False), bargap=0.6, xaxis_title="Average rating", yaxis_title="Statements")

    annotations = []  # List to store annotations
    startplace = 0.4
    for i in stacked_df['text'][6:8]:
        annotation = dict(
            x=1, y=startplace,
            text=f'<b>{i}</b>',
            font=dict(family="Arial", size=14, color="#FAFAFA"),
            showarrow=False,
            xanchor='left',
            align='left'
        )
        startplace += 1
        annotations.append(annotation)
    fig.update_layout(annotations=annotations, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')  # Add annotations to the figure
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.05,
        xanchor="left",
        x=0,
        traceorder="reversed",
        font=dict(size=14)
    ), legend_title_text='',
    
    )

    return fig
