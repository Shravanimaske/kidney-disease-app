import pickle

import streamlit as st # frontend code
# loading the trained model
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

@st.cache()

def prediction(age, wc, htn, dm):
    if htn =='no':
        htn=0
    else:
        htn=1
        
    if dm=='no':
        dm =0
    else:
        dm = 1
        
    # making prediction
    prediction = classifier.predict(
    [[age, wc, htn, dm]])
        
    if prediction == 0:
        pred='Kindey Disease not detected'
    else:
        pred = 'Kindey Disease found'
    
    return pred
    
    
# Write streamlit function now
def main():
    html_temp= """
    <div style ="background-color:cyan:padding:13px">
    <h1 style="color:black;text-align:center;">Kidney Disease Prediction</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    htn = st.selectbox('htn',("no","yes"))
    dm= st.selectbox('dm status',('no','yes'))
    age=st.number_input("Age")
    wc=st.number_input("WC")
    RESULT=""
    
    
    # WHEN 'PREDICT' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(age, wc, htn, dm)
        st.success("Report Results: {}".format(result))
        
if __name__=='__main__':
    main()
