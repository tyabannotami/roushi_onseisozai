import streamlit as st
import streamlit.components.v1 as stc
import base64
import time

st.title('大熊老師音声素材集')
st.subheader('ボタンを押すとその音声が流れます。')


bonabu = st.button('ボナブ～!')
no_say = st.button('〇〇とか言うな!')
yummy = st.button('yummy')
ii = st.button('いぃ～？')
iikagen =st.button('いいかげんにしろ!')
kora =st.button('コラッ!')
tixekera =st.button('チェケラ!')
usodaro =st.button('嘘だろ')
bonayoro =st.button('ぼなよろ')




def talk(path):
    audio_placeholder = st.empty()

    file_ = open(path, "rb")
    contents = file_.read()
    file_.close()

    audio_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
    audio_html = """
                    <audio autoplay=True>
                    <source src="%s" type="audio/ogg" autoplay=True>
                    Your browser does not support the audio element.
                    </audio>
                """ %audio_str

    audio_placeholder.empty()
    time.sleep(0.5) #これがないと上手く再生されません
    audio_placeholder.markdown(audio_html, unsafe_allow_html=True)

if bonabu:

    audio_path1 = 'bonavu.mp3' #入力する音声ファイル
    talk(audio_path1)

if no_say:

    audio_path1 = 'no_say.mp3' #入力する音声ファイル
    talk(audio_path1)
    
if yummy:

    audio_path1 = 'yummy.mp3' #入力する音声ファイル
    talk(audio_path1)
if ii:

    audio_path1 = 'ii.mp3' #入力する音声ファイル
    talk(audio_path1)
if iikagen:

    audio_path1 = 'iikagen.mp3' #入力する音声ファイル
    talk(audio_path1)
if kora:

    audio_path1 = 'kora.mp3' #入力する音声ファイル
    talk(audio_path1)
if tixekera:

    audio_path1 = 'tixekera.mp3' #入力する音声ファイル
    talk(audio_path1)
if usodaro:

    audio_path1 = 'usodaro.mp3' #入力する音声ファイル
    talk(audio_path1)
if bonayoro:

    audio_path1 = 'bonayoro.mp3' #入力する音声ファイル
    talk(audio_path1)




    