
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
st.set_page_config(page_title='Multi-disease Prediction',  layout = 'wide', initial_sidebar_state = 'auto')
# favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multi-Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'
                           ],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page 
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Name = st.text_input("Name of the patient")
    with col2:
        Age = st.text_input("Age")
    with col3:
        Gender = st.text_input("Gender")
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    # code for Prediction
    diab_diagnosis = ''
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        if(Pregnancies and Glucose and BloodPressure and SkinThickness and Insulin and BMI and DiabetesPedigreeFunction and Age) : 
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            #st.success("sd"+diab_diagnosis)
            st.write("Patient Name : ",Name)
            st.write("Age : ",Age)
            st.write("Gender : ",Gender)
            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic '
                st.error(diab_diagnosis)
            else:
                diab_diagnosis = 'The person is not diabetic 😊'
                st.success(diab_diagnosis)
        else : 
            st.warning("Please fill all details")
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Name = st.text_input("Name of the patient")
    with col2:
        age = st.text_input("Age")
    # with col3:
    #     Gender = st.text_input("Gender")
    with col3:
        sex = st.text_input('Sex (1-F,0-M)')
    with col1:
        cp = st.text_input('Chest Pain types')
    with col2:
        trestbps = st.text_input('Resting Blood Pressure')
    with col3:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col1:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col2:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col3:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col1:
        exang = st.text_input('Exercise Induced Angina')
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col3:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col1:
        ca = st.text_input('Major vessels colored by flourosopy')        
    #col1, col2= st.columns(2)
    with col2:
        thal = st.text_input('thal: 0 = normal; 1 = fixed; 2 = reversable')
    
    
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        
        if(age and sex and cp and trestbps and chol and fbs and restecg and thalach and exang and oldpeak and slope and ca and thal) : 
            heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])                          
            st.write("Patient Name : ",Name)
            st.write("Age : ",age)
            if(sex=="1"):
                st.write("Gender : Female")
            else:
                st.write("Gender : Male")
           # st.write("Gender : ",Gender)
            if (heart_prediction[0] == 1):
                st.error('The person is having heart disease')
            else:
                st.success('The person does not have any heart disease 😊')
            #st.success(heart_diagnosis)
        else : 
            st.warning("Please fill all details")

# # Parkinson's Prediction Page
# if (selected == "Parkinsons Prediction"):

#     # page title
#     st.title("Parkinson's Disease Prediction using ML")
#     col1, col2, col3 = st.columns(3)  
#     with col1:
#         Name = st.text_input("Name of the patient")
#     with col2:
#         Age = st.text_input("Age")
#     with col3:
#         Gender = st.text_input("Gender")
#     with col1:
#         fo = st.text_input('Multi-Dimensional Voice Program : (Hz)')
#     with col2:
#         fhi = st.text_input('Multi-Dimensional Voice Program :  (Hz)')
#     with col3:
#         flo = st.text_input('Multi-Dimensional Voice Program :   (Hz)')
#     with col1:
#         Jitter_percent = st.text_input('Multi-Dimensional Voice Program : Jitter(%)')
#     with col2:
#         Jitter_Abs = st.text_input('Multi-Dimensional Voice Program : Jitter(Abs)')
#     with col3:
#         RAP = st.text_input('MDVP : RAP')
#     with col1:
#         PPQ = st.text_input('MDVP : PPQ')
#     with col2:
#         DDP = st.text_input('Jitter : DDP')
#     with col3:
#         Shimmer = st.text_input('MDVP : Shimmer')
#     with col1:
#         Shimmer_dB = st.text_input('MDVP : Shimmer(dB)')
#     with col2:
#         APQ3 = st.text_input('Shimmer : APQ3')
#     with col3:
#         APQ5 = st.text_input('Shimmer : APQ5')
#     with col1:
#         APQ = st.text_input('MDVP : APQ')
#     with col2:
#         DDA = st.text_input('Shimmer : DDA')
#     with col3:
#         NHR = st.text_input('NHR')
#     with col1:
#         HNR = st.text_input('HNR')
#     with col2:
#         RPDE = st.text_input('RPDE')
#     with col3:
#         DFA = st.text_input('DFA')
#     with col1:
#         spread1 = st.text_input('spread1')
#     with col2:
#         spread2 = st.text_input('spread2')
#     with col3:
#         D2 = st.text_input('D2')
#     with col1:
#         PPE = st.text_input('PPE')
#     # code for Prediction
#     parkinsons_diagnosis = ''
    
#     # creating a button for Prediction    
#     if st.button("Parkinson's Test Result") :
#         if (fo and fhi and flo and Jitter_percent and Jitter_Abs and RAP and PPQ and DDP and Shimmer and Shimmer_dB and APQ3 and APQ5 and APQ and DDA and NHR and HNR and spread1 and spread2 and D2 and PPE):
#             parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
#             st.write("Patient Name : ",Name)
#             st.write("Age : ",Age)
#             st.write("Gender : ",Gender)
#             if (parkinsons_prediction[0] == 1):
#                 st.error("The person has Parkinson's disease")
#             else:
#                 st.success("The person does not have Parkinson's disease 😊")
#             #st.success(parkinsons_diagnosis)
#         else :
#             st.warning("Please fill all details.")
    



        
 

# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu

# # loading the saved models
# st.set_page_config(page_title='Multi-disease Prediction',  layout = 'wide', initial_sidebar_state = 'auto')
# # favicon being an object of the same kind as the one you should provide st.image() with (ie. a PIL array for example) or a string (url or local file path)

# diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
# parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
# heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))



# # sidebar for navigation
# with st.sidebar:
    
#     selected = option_menu('Multi-Disease Prediction System',
                          
#                           ['Diabetes Prediction',
#                            'Heart Disease Prediction',
#                            'Parkinsons Prediction'
#                            ],
#                           icons=['activity','heart','person'],
#                           default_index=0)
    
    
# # Diabetes Prediction Page 
# if (selected == 'Diabetes Prediction'):
    
#     # page title
#     st.title('Diabetes Prediction using ML')
    
    
#     # getting the input data from the user
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         Name = st.text_input("Name of the patient")
#     with col2:
#         Age = st.text_input("Age")
#     with col3:
#         Gender = st.text_input("Gender")
    
#     with col1:
#         Pregnancies = st.text_input('Number of Pregnancies')
        
#     with col2:
#         Glucose = st.text_input('Glucose Level')
    
#     with col3:
#         BloodPressure = st.text_input('Blood Pressure value')
#     with col1:
#         SkinThickness = st.text_input('Skin Thickness value')
#     with col2:
#         Insulin = st.text_input('Insulin Level')
#     with col3:
#         BMI = st.text_input('BMI value')
#     with col1:
#         DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
#     # code for Prediction
#     diab_diagnosis = ''
#     # creating a button for Prediction
#     if st.button('Diabetes Test Result'):
#         if(Pregnancies and Glucose and BloodPressure and SkinThickness and Insulin and BMI and DiabetesPedigreeFunction and Age) : 
#             diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
#             #st.success("sd"+diab_diagnosis)
#             st.write("Patient Name : ",Name)
#             st.write("Age : ",Age)
#             st.write("Gender : ",Gender)
#             if (diab_prediction[0] == 1):
#                 diab_diagnosis = 'The person is diabetic '
#                 st.error(diab_diagnosis)
#             else:
#                 diab_diagnosis = 'The person is not diabetic 😊'
#                 st.success(diab_diagnosis)
#         else : 
#             st.warning("Please fill all details")
# # Heart Disease Prediction Page
# if (selected == 'Heart Disease Prediction'):
#     # page title
#     st.title('Heart Disease Prediction using ML')
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         Name = st.text_input("Name of the patient")
#     with col2:
#         age = st.text_input("Age")
#     with col3:
#         Gender = st.text_input("Gender")
#     with col1:
#         sex = st.text_input('Sex (1-F,0-M)')
#     with col2:
#         cp = st.text_input('Chest Pain types')
#     with col3:
#         trestbps = st.text_input('Resting Blood Pressure')
#     with col1:
#         chol = st.text_input('Serum Cholestoral in mg/dl')
#     with col2:
#         fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
#     with col3:
#         restecg = st.text_input('Resting Electrocardiographic results')
#     with col1:
#         thalach = st.text_input('Maximum Heart Rate achieved')
#     with col2:
#         exang = st.text_input('Exercise Induced Angina')
#     with col3:
#         oldpeak = st.text_input('ST depression induced by exercise')
#     with col1:
#         slope = st.text_input('Slope of the peak exercise ST segment')
#     with col2:
#         ca = st.text_input('Major vessels colored by flourosopy')        
#     #col1, col2= st.columns(2)
#     with col3:
#         thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
#     # code for Prediction
#     heart_diagnosis = ''
    
#     # creating a button for Prediction
    
#     if st.button('Heart Disease Test Result'):
        
#         if(age and sex and cp and trestbps and chol and fbs and restecg and thalach and exang and oldpeak and slope and ca and thal) : 
#             heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg),int(thalach),int(exang),float(oldpeak),int(slope),int(ca),int(thal)]])                          
#             st.write("Patient Name : ",Name)
#             st.write("Age : ",age)
#             st.write("Gender : ",Gender)
#             if (heart_prediction[0] == 1):
#                 st.error('The person is having heart disease')
#             else:
#                 st.success('The person does not have any heart disease 😊')
#             #st.success(heart_diagnosis)
#         else : 
#             st.warning("Please fill all details")

# # Parkinson's Prediction Page
# if (selected == "Parkinsons Prediction"):

#     # page title
#     st.title("Parkinson's Disease Prediction using ML")
#     col1, col2, col3 = st.columns(3)  
#     with col1:
#         Name = st.text_input("Name of the patient")
#     with col2:
#         Age = st.text_input("Age")
#     with col3:
#         Gender = st.text_input("Gender")
#     with col1:
#         fo = st.text_input('Multi-Dimensional Voice Program : (Hz)')
#     with col2:
#         fhi = st.text_input('Multi-Dimensional Voice Program :  (Hz)')
#     with col3:
#         flo = st.text_input('Multi-Dimensional Voice Program :   (Hz)')
#     with col1:
#         Jitter_percent = st.text_input('Multi-Dimensional Voice Program : Jitter(%)')
#     with col2:
#         Jitter_Abs = st.text_input('Multi-Dimensional Voice Program : Jitter(Abs)')
#     with col3:
#         RAP = st.text_input('MDVP : RAP')
#     with col1:
#         PPQ = st.text_input('MDVP : PPQ')
#     with col2:
#         DDP = st.text_input('Jitter : DDP')
#     with col3:
#         Shimmer = st.text_input('MDVP : Shimmer')
#     with col1:
#         Shimmer_dB = st.text_input('MDVP : Shimmer(dB)')
#     with col2:
#         APQ3 = st.text_input('Shimmer : APQ3')
#     with col3:
#         APQ5 = st.text_input('Shimmer : APQ5')
#     with col1:
#         APQ = st.text_input('MDVP : APQ')
#     with col2:
#         DDA = st.text_input('Shimmer : DDA')
#     with col3:
#         NHR = st.text_input('NHR')
#     with col1:
#         HNR = st.text_input('HNR')
#     with col2:
#         RPDE = st.text_input('RPDE')
#     with col3:
#         DFA = st.text_input('DFA')
#     with col1:
#         spread1 = st.text_input('spread1')
#     with col2:
#         spread2 = st.text_input('spread2')
#     with col3:
#         D2 = st.text_input('D2')
#     with col1:
#         PPE = st.text_input('PPE')
#     # code for Prediction
#     parkinsons_diagnosis = ''
    
#     # creating a button for Prediction    
#     if st.button("Parkinson's Test Result") :
#         if (fo and fhi and flo and Jitter_percent and Jitter_Abs and RAP and PPQ and DDP and Shimmer and Shimmer_dB and APQ3 and APQ5 and APQ and DDA and NHR and HNR and spread1 and spread2 and D2 and PPE):
#             parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
#             st.write("Patient Name : ",Name)
#             st.write("Age : ",Age)
#             st.write("Gender : ",Gender)
#             if (parkinsons_prediction[0] == 1):
#                 st.error("The person has Parkinson's disease")
#             else:
#                 st.success("The person does not have Parkinson's disease 😊")
#             #st.success(parkinsons_diagnosis)
#         else :
#             st.warning("Please fill all details.")
    



        
 
