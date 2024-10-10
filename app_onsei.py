import streamlit as st
import streamlit.components.v1 as stc
import base64
import time

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
        .notranslate {
        translate: no;
    }
    </style>
    """, unsafe_allow_html=True)


st.title('大熊老師音声素材集（試作中）')
# 言語タグを使用してヘッダーを設定
st.markdown("""
    <h3 class="notranslate">ボタンを押すとその音声が流れます。</h3>
    """, unsafe_allow_html=True)


bonabu = st.button('ボナヴ～!')
no_say = st.button('〇〇とか言うな!')
koutei = st.button('全肯定老師')
ASMR = st.button('ASMR')
yummy = st.button('yummy')
hoo = st.button('hoo!')
semi = st.button('ずっきーなるなる')
ii = st.button('いぃ～？')
iikagen =st.button('いいかげんにしろ!')
kora1 =st.button('コラ!')
kora2 =st.button('コラ～!')
kora3 =st.button('コラッ!')
tixekera =st.button('チェケラ!')
usodaro =st.button('嘘だろ')
bonayoro =st.button('ぼなよろ')
bonaoya =st.button('ぼなおや')
kyarason = st.button('キャラソン')
hannya =st.button('般若心経')


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

if koutei:

    audio_path1 = 'zenkoutei.mp3' #入力する音声ファイル
    talk(audio_path1)


if ASMR:

    audio_path1 = 'ASMR.mp3' #入力する音声ファイル
    talk(audio_path1)    

if yummy:

    audio_path1 = 'yummy.mp3' #入力する音声ファイル
    talk(audio_path1)
if hoo:

    audio_path1 = 'hoo.mp3' #入力する音声ファイル
    talk(audio_path1)
if semi:

    audio_path1 = 'semi.mp3' #入力する音声ファイル
    talk(audio_path1)
if ii:

    audio_path1 = 'ii.mp3' #入力する音声ファイル
    talk(audio_path1)
if iikagen:

    audio_path1 = 'iikagen.mp3' #入力する音声ファイル
    talk(audio_path1)
if kora1:

    audio_path1 = 'kora1.mp3' #入力する音声ファイル
    talk(audio_path1)
if kora2:

    audio_path1 = 'kora2.mp3' #入力する音声ファイル
    talk(audio_path1)
if kora3:

    audio_path1 = 'kora3.mp3' #入力する音声ファイル
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

if bonaoya:

    audio_path1 = 'bonaoya.mp3' #入力する音声ファイル
    talk(audio_path1)

if kyarason:

    audio_path1 = 'kyarason.mp3' #入力する音声ファイル
    talk(audio_path1)

if hannya:

    audio_path1 = 'hannya.mp3' #入力する音声ファイル
    talk(audio_path1)



    
