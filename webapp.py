import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

# initializing the StandardScaler Object
scaler=StandardScaler()


# loading our model file (model.sav) into this program
model=pickle.load(open('model.sav','rb'))

# loading scaler object file in the program
scaler=pickle.load(open('scaler.sav','rb'))

# function for prediction
def fraudPrediction(step,pay_type,amount,oldbalanceOrg,oldbalanceDest,isFlaggedFraud):

    input_data=np.array([[step,pay_type,amount,oldbalanceOrg,oldbalanceDest,isFlaggedFraud]])
    
    # transforming the ndarray values
    input_data_scaler=scaler.transform(input_data)

    # prediction part
    pred=model.predict(input_data_scaler)

    if(pred==0):
        return "**Normal Transaction** 💰"
    else:
        return "**Fraud Transaction** 💰"


# main() for web app interface and input tasks

def main():

    
    # for wide look 
    st.set_page_config(layout="wide")


    
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/1242348/pexels-photo-1242348.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    html_temp="""

    <div style="background-color:#542edb;padding:10xp">
    <h2 style="color:#e8b323;text-align:center;">fraudulent transactions Predicition  Model</h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)


    step = int(st.number_input('**Insert time ( 1 unit= 1 hrs)**'))
    payment_type=st.selectbox('**Payment Options?**', ('CASH_OUT','PAYMENT','CASH_IN','TRANSFER','DEBIT'))

    if payment_type=='CASH_OUT':
        payment_type=int(5)
    elif payment_type=='PAYMENT':
        payment_type=int(4)
    elif payment_type=='CASH_IN':
        payment_type=int(3)
    elif payment_type=='TRANSFER':
        payment_type=int(2)
    else:
        payment_type=int(1)
    
    amount=float(st.number_input('**Insert Amount :-**'))
    oldbalanceOrg=float(st.number_input('**What was sender old balance :-**'))
    oldbalanceDest=float(st.number_input('**What was receiver cold balance :-**'))

    isFlaggedFraud=st.selectbox('**is transaction flagged fraud ?**', ('YES (1)', 'No (0)'))
    
    if isFlaggedFraud=='YES (1)':
        isFlaggedFraud=int(1)
    else:
        isFlaggedFraud=int(0)


    # creating the object, for displaying the predicted string
    whichCategory= ''

    # button for prediction
    if st.button("**Predict**"):
        whichCategory=fraudPrediction(step,payment_type,amount,oldbalanceOrg,oldbalanceDest,isFlaggedFraud)

    st.success(whichCategory)


if __name__ == '__main__':
    main()
