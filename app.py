import streamlit as st
import pandas as pd
import numpy as np
import os
import requests
import plotly.express as px
from datetime import datetime, timedelta
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from PIL import Image
ALPHAVANTAGE_API_KEY = 'H983JJABQU6EEV35'
ts = TimeSeries(key=ALPHAVANTAGE_API_KEY, output_format='pandas')
cc = CryptoCurrencies(key=ALPHAVANTAGE_API_KEY, output_format='pandas')

resp = requests.get('https://www.alphavantage.co/query', params={
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'AZUL4.SA.SA',
    'market': 'BRL',
    'apikey': ALPHAVANTAGE_API_KEY,
    'datatype': 'json',
    'outputsize': "full"})
doc = resp.json()
        
df = pd.DataFrame.from_dict(doc['Time Series (Daily)'], orient='index', dtype=np.float)
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'Data', '4. close': 'Preço', '6. volume': 'Volume'})


st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)
def main():
    overview = '[OverView](https://github.com/JoseEstevan/OverView)'
    
    st.title(overview)
    st.subheader('Azul')
    
    menu = ['OverView','Ações','Sobre']
    choice = st.sidebar.selectbox("Menu",menu)
    financ = Image.open('Azul.jpg')
    
    if choice == 'OverView':
        st.markdown("A Azul (Azul Linhas Aéreas Brasileiras S/A) é uma empresa brasileira do setor de transporte aéreo, constituída como sociedade anônima de capital aberto e negociada na B3 sob o código AZUL4. Sua atividade principal é o transporte aéreo de passageiros. O foco da Azul são as rotas aéreas regionais dentro do Brasil. Nesse sentido, a empresa possui atuação em quase todos os estados brasileiros. Além de operar com voos para as capitais, a companhia também realiza rotas para aeroportos menores no interior do país. A Azul também realiza voos internacionais para destinos selecionados e opera voos para Estados Unidos, Argentina, Uruguai, Guiana, França e Portugal. Em Portugal, Argentina e Estados Unidos, a companhia realiza voos para mais de um destino.")
        st.subheader('Principais produtos e serviços comercializados pela Azul')
        st.markdown('A atividade principal da Azul é o transporte aéreo de passageiros. As rotas operadas pela Azul possuem foco em voos regionais dentro do Brasil, com mais de 100 destinos diferentes.Além dos voos regionais, a Azul também realiza rotas internacionais. A empresa opera voos saindo do Brasil para países como Estados Unidos, Argentina, Uruguai, Guiana, França e Portugal.')
        st.image(financ, width=1200)
        d = {'Receita Líquida': [11.442, 9.057, 7.704, 6.669, 6.257, 5.803],'Custos': [-11.366,	-6.791,	-5.520,	-5.451,	-5.637,	-4.743], 'Lucro Líquido': [-2.403, -635, 424, -126, -1.074,-65], 'Ano': [20191231, 20181231, 20171231, 20161231, 20151231 ,20141231]}
        datad= pd.DataFrame(data=d)
        datad['Ano'] = datad['Ano'].apply(lambda x: pd.to_datetime(int(x), format="%Y%m%d"))  
        graph1 = px.line(datad,x="Ano", y="Receita Líquida", title='Receita Líquida em Bilhões', height=600, width=1000)
        st.plotly_chart(graph1) 
        
        graph2 = px.line(datad,x="Ano", y="Custos", title='Custos em Bilhões', height=600, width=1000)
        st.plotly_chart(graph2) 
        
        graph2 = px.line(datad,x="Ano", y="Lucro Líquido", title='Lucro Líquido em Bilhões', height=600, width=1000)
        st.plotly_chart(graph2) 
        st.text('Obs: Os valores com decimais estão em Bilhões, os outros estão em Milhões.')
        #st.image()
        #st.image([image1,image2])

        
    
    
    elif choice == 'Ações':
        
        df = pd.DataFrame.from_dict(doc['Time Series (Daily)'], orient='index', dtype=np.float)
        df.reset_index(inplace=True)
        df = df.rename(columns={'index': 'Data', '4. close': 'Preço', '6. volume': 'Volume'})
        
        figg = px.line(df, x='Data', y=df['Preço'], title='Valor das Ações', width=1250, height=800)
        figg.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
        ])))
        st.plotly_chart(figg)


        fig = px.line(df, x='Data', y=df['Volume'], title='Volume Negociado', width=1250, height=800)
        fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
        ])))
        st.plotly_chart(fig)


    elif choice == 'Sobre':
        st.header("Sobre")
        st.markdown('Esta aplicação faz parte do meu projeto OverView, que consiste em fazer análises sobre diferentes assuntos, a fim de praticar e testar coisas novas.')
        st.subheader('Redes Sociais')
        
        linkedin = '[LinkedIn](https://www.linkedin.com/in/joseestevan/)'
        st.markdown(linkedin, unsafe_allow_html=True) 
        
        github = '[GitHub](https://github.com/JoseEstevan)'
        st.markdown(github, unsafe_allow_html=True)  

        medium = '[Medium](https://joseestevan.medium.com/)'
        st.markdown(medium, unsafe_allow_html=True) 
            
    st.subheader('By: José Estevan')

if __name__ == '__main__':
    main()




