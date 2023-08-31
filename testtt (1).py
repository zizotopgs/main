import streamlit as st
import requests
from streamlit_lottie import st_lottie
import joblib
import numpy as np

st.set_page_config(page_title='combany loan', page_icon='::star::')

def load_lottie(https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dialabank.com%2Fbusiness-loan-article%2Fwhy-is-business-loan-important%2F&psig=AOvVaw0_31l_tOTKw2wE_nyhwgCF&ust=1693505284611000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKjEvvn8hIEDFQAAAAAdAAAAABAE): # test url if you want to use your own lottie file 'valid url' or 'invalid url'
    r = requests.get(https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dialabank.com%2Fbusiness-loan-article%2Fwhy-is-business-loan-important%2F&psig=AOvVaw0_31l_tOTKw2wE_nyhwgCF&ust=1693505284611000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKjEvvn8hIEDFQAAAAAdAAAAABAE)
    if r.status_code != 200:
        return None
    return r.json()

def prepare_input_data_for_model(RATE_owner_1,PERCENT_OWN_owner_1,RATE_owner_2,PERCENT_OWN_owner_2,completion_status):
st.text('enter the rate:')
Rate_owner_1=st.number_input(' rate owner 1 : ', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    #rates for owners
    if Rate_owner_1 == 'A':
        rat=1
    else if 
        Rate_owner_1 = 'B':
        rate=2
        elif
         Rate_owner_1 = 'C':
         rate=3
         elif
           Rate_owner_1 = 'D':
           rate=4
           else:
           rate=5

        if  Rate_owner_2 =='A': 
        rate=1
        elif
        Rate_owner_2 =='B' :
        rate=2
        elif
            Rate_owner_2 =='C':
            rate=3
            elif 
             Rate_owner_2 =='D':
             rate=4
             else:
             rate=5
             if Rate_owner_3 =='A':
             rate=1
             elif Rate_owner_3 =='B':
             rate=2
             elif Rate_owner_3 =='C':
             rate=3
             elif Rate_owner_3 =='D':
             rate=4
             else:
             rate=5

             if Rate_owner_4 =='A':
             rate=1
             elif Rate_owner_4=='B':
             rate=2
             elif Rate_owner_4 =='C':
             rate=3
             elif Rate_owner_4 =='D':
             rate=4
             else:
             rate=5

             #rate for id location
             if RATE_ID_Location=='A':
             rateid=1
             else:
             rateid=2
             #

             if RATE_ID_FOR_judgement_lien_percent
             









    #s_b = ssc_b.map(sb)
    if RATE_ID_FOR_Location == 'A':
        location = 1
    else:
        loaction = 0
    #h_b = hsc_b.map(hb)
    st.text('enter the precentge:')
    PERCENT_OWN_owner_1=st.number_input('Percentage 1 : ', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    if PERCENT_OWN_owner_1 >40:
        rank = 0
    else:
        rank = 1
    
    st.text('enter the precentge2:')
    PERCENT_OWN_owner_1=st.number_input('Percentage 2: ', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    
    if PERCENT_OWN_owner_2>40
        rank = 0 
    
    else:
       rank= 2
  
    if
        wexp = 0
    else:
        wexp = 1
    #specia = specialisation.map(spec)
    if specialisation == 'Mkt&Fin':
        specia = 0
    else:
        specia = 1
    
    A = [sex,ssc_p,s_b,hsc_p,h_b,h_s,degree_p,g_d,wexp,employability_test,specia,mba_p]
    sample = np.array(A).reshape(-1,len(A))
    
    return sample



loaded_model = joblib.load(open("combony loan", 'rb'))



st.write('# Job Placement Deployment')
#st.header('Placement')

lottie_link = "https://assets8.lottiefiles.com/packages/lf20_ax5yuc0o.json"
animation = load_lottie(lottie_link)

st.write('---')
st.subheader('Enter your details to predict your job placement status')

with st.container():
    
    right_column, left_column = st.columns(2)
    
    with right_column:
        name = st.text_input('Name:')
        
        gender = st.radio('Gender : ', ['F', 'M'])
        
        ssc_p = st.number_input('SSC Percentage : ', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        
        ssc_b = st.radio('SSC Board : ', ['Central', 'Others'])
        
        hsc_p = st.number_input('HSC Percentage : ', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        
        hsc_b = st.radio('HSC Board : ', ['Central', 'Others'])
        
        hsc_subject = st.selectbox('HSC Subject : ', ('Commerce', 'Science', 'Arts'))
        
        degree_p = st.number_input('Degree Percentage : ', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        
        undergrad_degree = st.selectbox('Undergraduate Degree : ', ('comm&Mgmt', 'Sci&Tech', 'Others'))
        
        workex = st.radio('Work Experience : ', ['Yes', 'No'])
        
        employability_test = st.number_input('Employability Test Percentage : ', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        
        specialisation = st.selectbox('Specialisation : ', ('Mkt&Fin', 'Mkt&HR'))
        
        mba_p = st.number_input('MBA Percentage : ', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        
        sample = prepare_input_data_for_model(gender,ssc_p,ssc_b , hsc_p,hsc_b,hsc_subject,degree_p,undergrad_degree,workex,employability_test,specialisation,mba_p)
        

    with left_column:
        st_lottie(animation, speed=1, height=400, key="initial")
        

    if st.button('Predict'):
            pred_Y = loaded_model.predict(sample)
            
            if pred_Y == 0:
                #st.write("## Predicted Status : ", result)
                st.write('### Congratulations ', name, '!! You are placed.')
                st.balloons()
            else:
                st.write('### Sorry ', name, '!! You are not placed.')
    