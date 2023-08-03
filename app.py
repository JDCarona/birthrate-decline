import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from survey_plotter import plot_pictogram, plot_employment_status, plot_children, plot_financial_factors, plot_choice_factors, plot_external_influences_factors, plot_health_factors

st.set_page_config(layout="centered")
css='''
<style>
    section.main > div {max-width:800px}
</style>
'''
st.markdown(css, unsafe_allow_html=True)

st.title("Falling Behind: A Global Look at Declining Birth Rates and its Consequences")
st.caption('6th June 2023. Jonathan Carona. Lucerne University of Applied Sciences. Data Story')

st.image("./img/jeremy.jpg")

st.write(
    """Imagine a world where the rhythm of life is changing. Where the joyous cries of newborns become less frequent, and the sound of children playing in the streets grows faint. This is the reality we face today, a world grappling with declining birth rates.

Born and raised in Switzerland to Filipino parents, I am a 22-year-old male belonging to Generation Z. I have observed significant generational and cultural disparities regarding 
family sizes between my parents' experiences in the Philippines and my own upbringing in Switzerland. While my parents are part of Generation X, their family sizes differ greatly from those of my generation. With family sizes ranging from 7 to 10 children, it is evident that numerous factors and events have shaped this significant shift over the span of 60 years.

I asked myself, has the birthrate during this time decreased? Should there be a decline, is it because generational or cultural reasons? And how would it affect the future?"""
)

st.header("Consistent birthrate declination")
st.write(
    """To answer the first question, it is interesting to observe the birthrate evolution on a global scale. There is a consistent pattern of declining birth rates worldwide. This phenomenon is not limited to a particular region or culture; it is a global trend that has been observed over the past few decades."""
)
colorscale = [
    [0, '#00FFFF'],  
    [0.25, '#BA55D3'],  
    [0.5, '#9370DB'],  
    [0.75, '#483D8B'],  
    [1, '#00008B']  
]

birth_rate_df = pd.read_csv("./data_clean/birth_rate_clean.csv")


fig = px.choropleth(
    birth_rate_df,
    locations="Country_Code",
    color="Birth_Rate",
    animation_frame="Year", 
    hover_name="Country_Name",
    range_color=[0, 4],
    color_continuous_scale=colorscale
)


fig.update_geos(fitbounds="locations", visible=False, showframe=False)
fig.update_layout(geo=dict(bgcolor= 'rgba(0,0,0,0)'))
fig.update_layout(title="Birth Rate by Country (1960-2020)", coloraxis=dict(colorbar=dict(orientation='h', y=-0.15)), height=600)

st.plotly_chart(fig, use_container_width=True, height=600)

st.write(
    """Examining data from various countries, it is found that birth rates have been steadily decreasing, resulting in smaller family sizes. The statistics reveal a significant shift in demographic patterns that has far-reaching implications for societies across the globe.

Moreover, this decline in birth rates is not confined to developed nations. Even in regions that historically had higher birth rates, such as Africa and the Philippines, there has been a noticeable downward trend. The reasons behind this decline may vary, but the overall pattern remains consistent: fewer children are being born worldwide."""
)

st.header("Possible reasons for the decline")
st.write(
    """Understanding the reasons behind the declining birth rates is crucial to gaining insight into this global phenomenon. Several factors contribute to this trend, and they often intertwine in complex ways.
    A possible way to find out possible reasons for the decline is to ask the people themselves, who are capable of having children. 

In a survey conducted by graduate researchers from Rider University in Lawrenceville NJ where they asked questions towards women who have children and women who do not have children on childlessness. 
The researchers asked 30 questions in the fields financial, choice, outside influences and health. Each question is rated from 1 to 5 indicating how true and significant it is.

In this survey, 124 women of different backgrounds and status were asked:
"""
)

col1, col2 = st.columns(2)
with col1:
   st.pyplot(fig=plot_children(), use_container_width=True)


with col2:
   st.pyplot(fig=plot_employment_status(), use_container_width=True)



st.pyplot(fig=plot_pictogram(), use_container_width=True)

st.subheader("Financial factors")

st.plotly_chart(plot_financial_factors(), use_container_width=True, height=400)

st.write(
    """
    Women's increasing participation in the workforce has transformed societal norms, shifting away from traditional roles of homemaking. Today, women, both with and without children, perceive that those in high-income jobs may choose not to have children due to the high opportunity cost of potential earnings. 
    This reflects the significance of financial considerations and career aspirations in the decision-making process surrounding childlessness. Furthermore, there is a shared recognition that having children can potentially act as a career impediment for women. 
    When considering the expense of raising children, there is a slight difference in opinion between women with and without children, indicating varied perspectives on this matter.
    """
)

st.subheader("Choice and perception")

st.plotly_chart(plot_choice_factors(), use_container_width=True, height=400)

st.write("""
Women, regardless of their parental status, hold the belief that choosing not to have a child is a valid decision, indicating a shared understanding and respect for individual choices. 
Moreover, there is a strong consensus among women that it is reasonable for a woman to decide against having a child, reflecting societal acceptance and recognition of diverse paths to fulfillment. 
""")

st.subheader("External influences")

st.plotly_chart(plot_external_influences_factors(), use_container_width=True, height=400)

st.write("""
Women, both with and without children, recognize the societal pressure that exists around motherhood.
However, it is noteworthy that peer pressure has a minimal impact on a woman's decision to remain childless. 
This underscores the importance of honoring women's autonomy and personal agency in determining their path to parenthood, regardless of external influences. 
""")

st.subheader("Health factors")

st.plotly_chart(plot_health_factors(), use_container_width=True, height=400)

st.write("""
The prime years for women, typically around the age of 27, coincide with their peak physical and reproductive capabilities. It is during this period that many women choose to have their first child. 
This decision is often influenced by the awareness of the potential health risks associated with delayed motherhood beyond the age of 35. 
Recognizing the significance of timing and the consideration of health-related factors, women often prioritize starting a family before the age of 35 to mitigate potential complications. 

""")

st.header("Future consequences")
st.write(
    """
As birth rates decline, the average age of the population increases. This demographic shift poses challenges for healthcare systems, pension programs, and social welfare services. The proportion of older adults grows, putting pressure on the working-age population to support the elderly."""
)

from PIL import Image
manIcon = Image.open("./img/man.png")
womanIcon = Image.open("./img/woman.png")
swissIcon = Image.open("./img/schweiz.png")

colorscale = [
    [0, '#00FFFF'], 
    [0.25, '#9370DB'], 
    [0.5, '#BA55D3'],  
    [0.75, '#483D8B'],  
    [1, '#00008B']  
]
colorscale_two = [
    '#00FFFF',  
    '#9370db', 
    '#BA55D3', 
    '#483D8B', 
    '#00008B',  
]

swiss_pyramid = pd.read_csv("./data_clean/Switzerland-2021.csv")
fig = px.bar(
    orientation="h",
    y=swiss_pyramid["Age"],
    x=-swiss_pyramid["M"],
    title='Age pyramid of men and women in Switzerland'
    
)

layout = go.Layout(
    yaxis=go.layout.YAxis(title="Age group"),
    xaxis=go.layout.XAxis(
        range=[-400_000, 400_000],
        tickvals=[-300_000, -200_000, -100_000, 0, 100_000, 200_000, 300_000],
        ticktext=[300_000, 200_000, 100_000, 0, 100_000, 200_000, 300_000],
        title="Population count",
    ),
    barmode="overlay",
    bargap=0.1,
    height=600
)
fig.update_layout(layout)
fig.update_traces(
    selector=dict(type="bar"),
    marker=dict(color=[
        colorscale_two[3], 
        colorscale_two[3], 
        colorscale_two[0], 
        colorscale_two[0], 
        colorscale_two[3], 
        colorscale_two[3], 
        colorscale_two[3], 
        colorscale_two[3], 
        colorscale_two[3], 
        colorscale_two[3],
        colorscale_two[1],
        colorscale_two[1],
        colorscale_two[3],
        colorscale_two[3],
        colorscale_two[3],
        colorscale_two[3],
        colorscale_two[3],
        colorscale_two[3],
        colorscale_two[3],
        colorscale_two[3],
        colorscale_two[3],
    ]),
)

fig.add_trace(
    go.Bar(
        orientation="h", y=swiss_pyramid["Age"], x=swiss_pyramid["F"], showlegend=False,
        marker=dict(color=[
            colorscale_two[2], 
            colorscale_two[2], 
            colorscale_two[0], 
            colorscale_two[0], 
            colorscale_two[2], 
            colorscale_two[2], 
            colorscale_two[2], 
            colorscale_two[2], 
            colorscale_two[2], 
            colorscale_two[2],
            colorscale_two[1],
            colorscale_two[1],
            colorscale_two[2],
            colorscale_two[2],
            colorscale_two[2],
            colorscale_two[2],
            colorscale_two[2],
            colorscale_two[2],
            colorscale_two[2],
            colorscale_two[2],
            colorscale_two[2],
    ])
    )
)

fig.add_layout_image(
    dict(
        source=womanIcon,
        xref="x",
        yref="y",
        x=400_000,  
        y='90-94',  
        sizex=100_000,  
        sizey=10, 
        xanchor="right",  
        yanchor="middle",  
        opacity=1,
        layer="above"
    )
)

fig.add_layout_image(
    dict(
        source=manIcon,
        xref="x",
        yref="y",
        x=-300_000,  
        y='90-94',  
        sizex=100_000,  
        sizey=10, 
        xanchor="right",  
        yanchor="middle",  
        opacity=1,
        layer="above"
    )
)

fig.add_layout_image(
    dict(
        source=swissIcon,
        xref="x",
        yref="y",
        x=-300_000,  
        y='5-9',  
        sizex=75_000,  
        sizey=8,  
        xanchor="right",  
        yanchor="middle",  
        opacity=1,
        layer="above"
    )
)

fig.add_annotation(x=200_000, y='15-19',
            text="Entering Workforce <br> Generation Z",
            showarrow=True,
            arrowhead=2,
            arrowcolor='#FAFAFA',
            xref="x", 
            yref='y',
            axref="x", 
            ayref='y',
            ax=325_000,
            ay='15-19',
            )

fig.add_annotation(x=-325_000, y='55-59',
            text="Leaving Workforce <br> Generation X",
            showarrow=True,
            arrowhead=2,
            arrowcolor='#FAFAFA',
            xref="x", 
            yref='y',
            axref="x", 
            ayref='y',
            ax=-310_000,
            ay='70-74',
            )


st.plotly_chart(fig, use_container_width=True, height=800)
st.write(
    """
As you can see in the age population pyramid, the highlighted age groups 50 to 59 are the biggest groups. In 10 years time these people will retire and leave the workforce.
To compensate for the loss of workforce, the amount of people from the younger generations between 10 to 19 years must be at least the same amount as the people retiring.
But this is not the case. The amount of people entering the workforce is much lower.
"""
)

st.write(
    """A shrinking workforce can lead to economic slowdowns and reduced productivity. With fewer young people entering the labor market, there may be a shortage of skilled workers in various industries. 
    This can hinder economic growth and innovation. The continuing decline in birth rates will inevitably bring about cultural and social transformations. 
    With smaller family sizes becoming the norm, societal structures and dynamics will undergo significant changes. 
    With fewer children being born, the transmission of cultural practices, languages, and values may be at risk. 
    This can lead to a loss of cultural diversity and potentially reshape societal norms and identities.
    To add to the problem of the elderly to youngster ratio, the life expectancy and median age because of medical advancements and overall healthcare improvements are increasing. 
    This means that the elderly will be in need of care for a longer period of time.
"""
)

st.header("What can we do against it? And what have we already done?")
st.write(
    """
Addressing the challenges posed by declining birth rates requires a multifaceted approach that encompasses social, economic, and policy interventions. Here are some strategies that have been implemented or proposed to mitigate the consequences and encourage sustainable birth rates:

Family-Friendly Policies: Governments can implement policies that support families, such as parental leave, flexible work arrangements, and affordable childcare. These measures can alleviate the financial and logistical burdens associated with raising children, making it more feasible for individuals to start families:

In the case of Switzerland in the year of 2020, the people voted that fathers are allowed to have a 2 week paid parental leave that one can take during the first six months after the baby has been born.

And in the events of Japan, the government has decided to double the monthly child allowance from 5'000 ¥ to 10'000 ¥.
"""
)

st.header("Conclusion")
st.write(
    """The global decline in birth rates presents both challenges and opportunities. By understanding the underlying factors, acknowledging the potential consequences, and implementing comprehensive strategies, we can strive for a sustainable balance that preserves the fabric of our societies, empowers individuals, and embraces the changes of the future."""
)
