import pandas as pd
import turicreate as tc
from PIL import Image
from turicreate import SFrame, SArray
import streamlit as st



df = pd.read_csv('data_for_model.csv', index_col=0)
model = tc.load_model('turi model')


image = Image.open('photo.png')
st.image(image)

st.markdown("<h1 style='text-align: center; '>Wizard who helps choose the perfect board game </h1>", unsafe_allow_html=True)
st.caption('*the title was generated by _ChatGPT_ :robot_face:')

st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

option = st.selectbox('Please choose a game from the list that you enjoy', (df['title']), 
                      index=1, help='you can completely delete the text and enter any game title')


st.write('You have selected:', option)

game_alias = df.loc[df['title']==option, 'alias'].values.tolist()
pred = model.get_similar_items(SArray(data=game_alias))
st.table(pred[['similar', 'score']])

st.markdown(' ')
st.markdown(' ')
st.markdown(' ')


st.write(':gear: [How it works](https://github.com/pgagp/recsys_bg)')
st.write(':calling: [My contact ](https://t.me/pgagp)')
