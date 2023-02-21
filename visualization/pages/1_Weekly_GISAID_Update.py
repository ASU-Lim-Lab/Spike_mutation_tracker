import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
from datetime import datetime

date = datetime.today().strftime('%b-%d-%Y')

st.set_page_config(
    page_title='GISAID update',
    page_icon='📊',
    layout='wide'
)

st.markdown('# Weekly Arizona GISAID Update')
st.markdown(f'#### {date}')
st.markdown('---')
st.sidebar.header('GISAID data')
st.write(
    '''
    ### About this page
    This page displayes currenlty circulating SARS-CoV-2 lineages in Arizona.

    #### Highlights
    - To date, the Lim lab has contributed more than 75,0000 sequences towards SARS-CoV-2 surveillance efforts in [Arizona](https://news.asu.edu/20220510-arizona-impact-milestone-arizona-researchers-sequence-genomes-more-100000-covid19-samples).
    - Sequenced samples include saliva samples provided by the ASU Biodesign Clinical Testing Lab (ABCTL) and partnered hospitals (Valleywise, Phoenix Children’s, Dignity Health) and [waste water](https://journals.asm.org/doi/full/10.1128/mbio.03101-22) samples provided by Halden lab.
    - Data was also obtained from the Global Initiave on Sharing Avian Influenza Data (GISAID) database. To learn more, visit [GISAID.org](https://gisaid.org/).

    ##### Other Resources
    - Johns Hopkins University COVID-19 global data [dashboard](https://gisanddata.maps.arcgis.com/apps/dashboards/bda7594740fd40299423467b48e9ecf6).

    '''
)


@st.cache_data
def get_data():
    df = pd.read_csv('data/VariantTable.csv')
    df = df.drop(columns=['Other'])
    return df


@st.cache_data
def get_data2():
    df2 = pd.read_csv('data/VBMTableSummary.csv')
    return df2


@st.cache_data
def get_data3():
    df3 = pd.read_csv('data/VOCTableSummary.csv')
    return df3


@st.cache_data
def get_data4():
    df = pd.read_csv('data/T_VariantTable.csv')
    df = df.rename(columns={'Unnamed: 0': 'Variants'})
    df = df.set_index('Variants')
    week_list = [i for i in df.columns]
    df1 = pd.DataFrame({
        'Week': week_list,
        'Alpha (B.1.1.7)': df.iloc[0].tolist(),
        'Delta (B.1.617.2)': df.iloc[1].tolist(),
        'Gamma (P.1)': df.iloc[2].tolist(),
        'Beta (B.1.351)': df.iloc[3].tolist(),
        'Epsilon (B.1.427/429)': df.iloc[4].tolist(),
        'Eta (B.1.525)': df.iloc[5].tolist(),
        'Iota (B.1.526)': df.iloc[6].tolist(),
        'Kappa (B.1.617.1)': df.iloc[7].tolist(),
        'Zeta (P.2)': df.iloc[8].tolist(),
        'Mu (B.1.621)': df.iloc[9].tolist(),
        'Omicron (BA.1/B.1.1.529)': df.iloc[10].tolist(),
        'Omicron (BA.2 sublineage)': df.iloc[11].tolist(),
        'Omicron (BA.2.75)': df.iloc[12].tolist(),
        'Omicron (BA.2.12.1)': df.iloc[13].tolist(),
        'Omicron (BA.3)': df.iloc[14].tolist(),
        'Omicron (BA.4)': df.iloc[15].tolist(),
        'Omicron (BA.5)': df.iloc[16].tolist()})
    df_melt = df1.melt(id_vars=['Week'], var_name='Lineages',
                       value_name='Amount', value_vars=df1.columns[1:], ignore_index=True)
    df_melt['%'] = 100 * df_melt['Amount'] /\
        df_melt.groupby('Week')['Amount'].transform('sum')
    return df_melt


df = get_data().set_index('Week')
df2 = get_data2().set_index('Variant')
df3 = get_data3().set_index('Variant')
df4 = get_data4()

#_____Graph1_______

p = px.bar(df,
           color='variable',
           # color_discrete_sequence=[
           #     '#3182bd', '#6baed6', '#9ecae1', '#c6dbef', '#e6550d',
           #     '#fd8d3c', '#fdae6b', '#fdd0a2', '#31a354', '#74c476',
           #     '#a1d99b', '#c7e9c0', '#756bb1', '#9e9ac8', '#bcbddc',
           #     '#dadaeb', '#636363'],
           title='Variant Table',
           labels={
               'value': 'Total Count',
               'Week': 'Week',
               'variable': 'Lineages'
           },
           )

p.update_layout(
    xaxis=dict(
        tickangle=-45,
        # tick0=0.1,
        # dtick=0.2
    ),
    autosize=True,
    # width=900,
    # height=500,
)


#_____Graph2_______
p2 = px.bar(df4,
            x='Week',
            y='%',
            color='Lineages',
            title='Variant Table',
            # template='plotly_white'
            )

p2.update_layout(barmode='relative',
                 xaxis=dict(
                     tickangle=-45,
                     # tick0=0.1,
                     # dtick=0.2
                 ),
                 autosize=True,
                 # width=900,
                 # height=500,
                 )


for i in range(len(df.columns)):
    p.data[i].marker.line.width = 0.8
    p.data[i].marker.line.color = 'black'
    p2.data[i].marker.line.width = 0.8
    p2.data[i].marker.line.color = 'black'

st.plotly_chart(p, use_container_width=True)
st.plotly_chart(p2, use_container_width=True)
st.markdown('''The graph above displays the total count for each major SARS-CoV-2 variant in Arizona.
    The legend allows for a variety of different interactions, including hiding lineage counts and box zooming.''')
st.dataframe(df2,
             width=1200,
             height=248
             )
st.dataframe(df3,
             width=1200,
             )
