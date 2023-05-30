import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.title("Falling Behind: A Global Look at Declining Birth Rates and its Consequences")
st.caption('15th of May 2023. Jonathan Carona')

st.image("./baby.jpg")

st.write(
    """Imagine a world where the rhythm of life is changing. Where the joyous cries of newborns become less frequent, and the sound of children playing in the streets grows faint. This is the reality we face today, a world grappling with declining birth rates.

Born and raised in Switzerland to Filipino parents, I am a 22-year-old male belonging to Generation Z. I have observed significant generational and cultural disparities regarding 
family sizes between my parents' experiences in the Philippines and my own upbringing in Switzerland. While my parents are part of Generation X, their family sizes differ greatly from those of my generation. With family sizes ranging from 7 to 10 children, it is evident that numerous factors and events have shaped this significant shift over the span of 60 years.

I asked myself, has the birthrate during this time decreased? Should there be a decline, is it because generational or cultural reasons? And how would it affect the future?"""
)

st.header("Consistent birthrate declination")
st.write(
    """To answer my first question, it is interesting to observe the birthrate evolution on a global scale. I discovered a consistent pattern of declining birth rates worldwide. This phenomenon is not limited to a particular region or culture; it is a global trend that has been observed over the past few decades."""
)

birth_rate_df = pd.read_csv("./data_clean/birth_rate_clean.csv")

# use the choropleth mapbox trace type in plotly express
fig = px.choropleth(
    birth_rate_df,
    locations="Country_Code",
    color="Birth_Rate",
    animation_frame="Year",  # add animation slider
    hover_name="Country_Name",
    range_color=[0, 4],
    color_continuous_scale='RdYlGn_r'
)


# Remove antarctica
fig.update_geos(fitbounds="locations", visible=False, showframe=False)

# show the figure
fig.update_layout(title="Birth Rate by Country (1960-2020)", dragmode=False, coloraxis=dict(colorbar=dict(orientation='h', y=-0.15)), height=600, width=689)

st.plotly_chart(fig, use_container_width=True, height=600, width=689)



st.write(
    """Examining data from various countries, it is found that birth rates have been steadily decreasing, resulting in smaller family sizes. The statistics reveal a significant shift in demographic patterns that has far-reaching implications for societies across the globe.

Moreover, this decline in birth rates is not confined to developed nations. Even in regions that historically had higher birth rates, such as Africa and the Philippines, there has been a noticeable downward trend. The reasons behind this decline may vary, but the overall pattern remains consistent: fewer children are being born worldwide."""
)

st.header("Possible reasons for the decline")
st.write(
    """Understanding the reasons behind the declining birth rates is crucial to gaining insight into this global phenomenon. Several factors contribute to this trend, and they often intertwine in complex ways:

In a survey conducted by graduate researchers from Rider University in Lawrenceville NJ where they asked questions towards unmarried and married women on childlessness. 
The researchers asked 30 questions in the fields financial, choice, outside influences and health. Each question is rated between 1 and 5 indicating how true and significant it is."""
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "Data",
        "Financial Questions",
        "Choice Questions",
        "External Influence Questions",
        "Health Questions",
    ]
)
questions = pd.read_csv("./data_clean/childlessness_questions.csv")
questions = questions.set_index("Question Code")
with tab1:
    question_mean = pd.read_csv("./data_clean/child_survey_mean.csv")
    st.plotly_chart(
        px.bar(
            question_mean, x="Question", y="Mean", title="Average Rating of Questions"
        ),
        use_container_width=True,
    )

with tab2:
   st.dataframe(questions[questions["Construct Name"] == "Financial"][['Full Question ']], use_container_width=True)


with tab3:
   st.dataframe(questions[questions["Construct Name"] == "Choice"][['Full Question ']], use_container_width=True)
   

with tab4:
   st.dataframe(questions[questions["Construct Name"] == "Outside Influences"][['Full Question ']], use_container_width=True)
   

with tab5:
   st.dataframe(questions[questions["Construct Name"] == "Health"][['Full Question ']], use_container_width=True)
   
st.caption("""The chat above shows the average of all answers per question. Questions 7 was a free text question and therefore not visible in the chart. The details of each question can be found inside each tab.""")


st.subheader("Financial Factors")
st.write(
    """The survey indicates that financial considerations play a significant role in women's decision-making about having children. Regarding the financial questions, all received relatively high ratings, suggesting that financial stability, the cost of raising children, and the financial judgment faced by women who choose not to have children are important factors influencing their decisions."""
)
st.subheader("Choice and Societal Perception")
st.write(
    """
Questions related to choice and societal perception also received notable ratings. It is evident that women's decisions about having children are influenced by the perception of society and the judgments they may face. While the majority agreed that it is reasonable for a woman to choose not to have a child, there were varying opinions about societal perception and the perceived impact of a woman's decision on her value and character.
"""
)

st.subheader("External Influences")
st.write(
    """
External influences, including family, religion, and peer pressure, were acknowledged but received somewhat lower ratings. While these factors play a role, they appear to have a slightly lesser impact on women's decisions compared to financial and choice-related factors.
"""
)

st.subheader("Health Considerations")
st.write(
    """
Health concerns received mixed ratings. Some questions indicated that health risks and age-related fertility decline were recognized as factors influencing women's decisions about having children, albeit not to a significant extent."""
)

st.header("Future consequences")
st.write(
    """
As birth rates decline, the average age of the population increases. This demographic shift poses challenges for healthcare systems, pension programs, and social welfare services. The proportion of older adults grows, putting pressure on the working-age population to support the elderly."""
)

swiss_pyramid = pd.read_csv("./Switzerland-2021.csv")
fig = px.bar(
    orientation="h",
    y=swiss_pyramid["Age"],
    x=-swiss_pyramid["M"],
)

layout = go.Layout(
    yaxis=go.layout.YAxis(title="Age"),
    xaxis=go.layout.XAxis(
        range=[-400_000, 400_000],
        tickvals=[-300_000, -200_000, -100_000, 0, 100_000, 200_000, 300_000],
        ticktext=[300_000, 200_000, 100_000, 0, 100_000, 200_000, 300_000],
        title="Number",
    ),
    barmode="overlay",
    bargap=0.1,
)
fig.update_layout(layout)

fig.add_trace(
    go.Bar(
        orientation="h", y=swiss_pyramid["Age"], x=swiss_pyramid["F"], showlegend=False
    )
)

st.plotly_chart(fig, use_container_width=True)
st.caption(
    """
As you can see in the age population pyramid, the highlighted age groups 50 to 59 are the biggest groups. In 10 years time these people will retire and leave the workforce.
To compensate for the loss of workforce, the amount of people from the younger generations between 10 to 19 years must be at least the same amount as the people retiring.
But this is not the case. The amount of people entering the workforce is much lower.
"""
)

life_expectancy_df = pd.read_csv("./data_clean/life_expectancy_switzerland.csv")
fig = px.line(
    life_expectancy_df,
    x="Year",
    y="Life expectancy at birth (historical)",
    title="Life Expectancy and median age in Switzerland",
)

median_age = pd.read_csv("./data_clean/median_age_switzerland.csv")
fig.add_scatter(x=median_age["Year"], y=median_age["median_age"], mode="lines")

st.plotly_chart(fig, use_container_width=True)
st.caption(
    """To add to the problem of the elderly to youngster ratio, as evident from this graph, the life expectancy and median age are increasing. This means that the elderly will be in need of care for a longer period of time."""
)

st.write(
    """A shrinking workforce can lead to economic slowdowns and reduced productivity. With fewer young people entering the labor market, there may be a shortage of skilled workers in various industries. This can hinder economic growth and innovation. The continuing decline in birth rates will inevitably bring about cultural and social transformations. With smaller family sizes becoming the norm, societal structures and dynamics will undergo significant changes. With fewer children being born, the transmission of cultural practices, languages, and values may be at risk. This can lead to a loss of cultural diversity and potentially reshape societal norms and identities.
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
