# pip install -U streamlit
# streamlit run app.py
# python -m venv .venv
# .\.venv\scripts\activate

import streamlit as st 
import pickle 
import sklearn

# load model
model = pickle.load(open('model2.pkl', 'rb'))
vectorizer = pickle.load(open("vectorizer.pkl", 'rb'))

# Function to render the initial cube animation with 6 cubes
def render_js_animation():
    animation_code = """
    <div class="container" style="position:relative; height:300px; display:flex; justify-content:center; align-items:center;">
        <div class="flex">
            <div class="cube">
                <div class="wall front"></div>
                <div class="wall back"></div>
                <div class="wall left"></div>
                <div class="wall right"></div>
                <div class="wall top"></div>
                <div class="wall bottom"></div>
            </div>
            <div class="cube">
                <div class="wall front"></div>
                <div class="wall back"></div>
                <div class="wall left"></div>
                <div class="wall right"></div>
                <div class="wall top"></div>
                <div class="wall bottom"></div>
            </div>
            <div class="cube">
                <div class="wall front"></div>
                <div class="wall back"></div>
                <div class="wall left"></div>
                <div class="wall right"></div>
                <div class="wall top"></div>
                <div class="wall bottom"></div>
            </div>
        </div>
        <div class="flex">
            <div class="cube">
                <div class="wall front"></div>
                <div class="wall back"></div>
                <div class="wall left"></div>
                <div class="wall right"></div>
                <div class="wall top"></div>
                <div class="wall bottom"></div>
            </div>
            <div class="cube">
                <div class="wall front"></div>
                <div class="wall back"></div>
                <div class="wall left"></div>
                <div class="wall right"></div>
                <div class="wall top"></div>
                <div class="wall bottom"></div>
            </div>
            <div class="cube">
                <div class="wall front"></div>
                <div class="wall back"></div>
                <div class="wall left"></div>
                <div class="wall right"></div>
                <div class="wall top"></div>
                <div class="wall bottom"></div>
            </div>
        </div>
    </div>
    <style>
        .flex {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 10px;
        }

        .cube {
            position: relative;
            width: 60px;
            height: 60px;
            transform-style: preserve-3d;
            animation: rotate 4s infinite;
            margin: 10px;
        }

        .wall {
            position: absolute;
            width: 60px;
            height: 60px;
            background: rgba(255, 255, 255, 0);
            border: 1px solid #000000 ;
        }

        .front { transform: translateZ(30px); }
        .back { transform: translateZ(-30px) rotateY(180deg); }
        .left { transform: rotateY(-90deg) translateX(-30px); transform-origin: center left; }
        .right { transform: rotateY(90deg) translateX(30px); transform-origin: center right; }
        .top { transform: rotateX(90deg) translateY(-30px); transform-origin: top center; }
        .bottom { transform: rotateX(-90deg) translateY(30px); }

        @keyframes rotate {
            0% { transform: rotateX(0deg) rotateY(0deg); }
            50% { transform: rotateX(180deg) rotateY(180deg); }
            100% { transform: rotateX(360deg) rotateY(360deg); }
        }
    </style>
    """
    st.markdown(animation_code, unsafe_allow_html=True)


# Function to render result animation
def render_result_animation(result):
    if result == 1:
        animation_code = """
        <div style="display:flex;justify-content:center;align-items:center;height:200px;">
            <div style="width:100px;height:100px;border-radius:50%;background-color:#ff5722;animation:bounce 1s infinite;"></div>
            <style>
                @keyframes bounce {
                    0%, 100% { transform: translateY(0); }
                    50% { transform: translateY(-20px); }
                }
            </style>
        </div>
        """
    else:
        animation_code = """
        <div style="display:flex;justify-content:center;align-items:center;height:200px;">
            <div style="width:100px;height:100px;border-radius:50%;background-color:#4caf50;animation:scale 1s infinite;"></div>
            <style>
                @keyframes scale {
                    0%, 100% { transform: scale(1); }
                    50% { transform: scale(1.2); }
                }
            </style>
        </div>
        """
    st.markdown(animation_code, unsafe_allow_html=True)



# عرض انيمشن المكعبات
render_js_animation()

def main():
    st.subheader("Enter your favorits:")

    # style change
    st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFB6B9;  
         color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

st.markdown("""
    <style>
        body {
            background-color: #F5CBCB; /* Light blue */
            color: #333333; /* Dark text */
        }
        .stApp {
            background-color: #FFEAEA;
        }
    </style>
""", unsafe_allow_html=True)


# create title
st.title('🌟Text Classification Model "♥..♥"')

review = st.text_input('Enter your Text:')

if st.button('Predict'):
    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)

    if prediction[0] == 0:
        st.success('business')
    elif prediction[0] == 1:
        st.success('entertainment')
    elif prediction[0] == 2:
        st.success('politics')
    elif prediction[0] == 3:
        st.success('sport')
    else:
        st.warning('tech')