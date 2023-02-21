import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import plotly.io as pio

date = datetime.today().strftime('%b-%d-%Y')

st.set_page_config(
    page_title='Tempe Wastewater',
    page_icon='🚱',
    layout='wide'
)


st.markdown('# Tempe Wastewater Virus Tracker')
st.markdown(f'#### {date}')
st.markdown('---')
st.sidebar.header('Tempe Wastewater Virus Tracker')
st.write(
    '''
    ### About this page
    The interactive visualizations below displays currently circulating viruses within Tempe wastewater.
    '''
)

@st.cache_data
def getData():
    df = pd.read_csv('data/TempeWW_test.csv')
    df['Week'] = pd.to_datetime(df['Week']).dt.strftime('%b %d %Y')

    df = df.set_index('Week')
    df = df.loc[:, 'SARS-CoV-2':'West Nile virus']
    df = df.applymap(lambda x: x if not np.isnan(x)
                       else np.random.choice(range(10)))
    return df

df = getData()

p = go.Figure(
    data=px.bar(df,
                color='variable',
                # text='variable', # get feedback
                title='Circulating Viruses in Tempe Waste Water',
                labels={
                    'value': 'Relative virus abundance',
                    'Week': 'Week',
                    'variable': '10 High-risk pathogens'},
                # template='plotly_dark'
                )
)

for i in range(len(df.columns)):
    p.data[i].marker.line.width = 0.8
    p.data[i].marker.line.color = 'black'

p.update_layout(
    # hovermode='x', # get feedback
    # hovermode='x unified', # get feedback
    xaxis=dict(
        tickangle=-45,
    ),
    autosize=True,
)
st.plotly_chart(p, use_container_width=True)


st.write(
    '''
    ### Influenza A
    Influenza A virus is a contagious virus that causes respiratory illness.
    - Symptoms include:
        - Fever
        - Cough
        - Shortness of breath or difficulty breathing
        - Sore throat
        - Runny or Stuffy nose
    - Vaccination:
        - The best way to prevent influenza is by getting the [influenza vaccination](https://www.google.com/search?q=flu+vaccination+near+me&ei=kSbtY-6zB-3AkPIPmqGAoAU&ved=0ahUKEwiuwO-Nlpj9AhVtIEQIHZoQAFQQ4dUDCBA&uact=5&oq=flu+vaccination+near+me&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzoKCAAQRxDWBBCwA0oECEEYAEoECEYYAFCKCViKCWDmCmgBcAJ4AIABAIgBAJIBAJgBAKABAcgBCMABAQ&sclient=gws-wiz-serp)
    '''
)
