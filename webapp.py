import streamlit as st
import joblib,os
import numpy as np
### NLP Pkgs
#import spacy

###Wordcloud

###Vectorizer
news_vectorizer = open("pickled_files/news_vectorizer.pickle", "rb")
news_cv = joblib.load(news_vectorizer)

###Load Models
def load_prediction_models(model_file):
    loaded_models = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_models

st.title("Fake News Classifier Machine Learning App")
st.subheader("NLP and ML App with Streamlit")

def main():
    ###News Classifier App with Streamlit """
    #st.title("Fake News Classifier ML App")
    #st.subheader("NLP and ML App with Streamlit")

    activities = ["Prediction"]
    
    #choice = st.sidebar.selectbox("Choose Activity", activities)
    
   # if choice == 'Prediction':
st.info("Paste an Article Below to Find out Whether or Not it is Real or Fake")
        
news_text = st.text_area("Enter Text", "Type Here")
        
all_ml_models = ["LR", "NB", "RFOREST", "VC"]
model_choice = st.selectbox("Choose ML Model", all_ml_models)
prediction_labels = {'fake': 0, 'real': 1}
if st.button("Classify"):
    st.text("Original test ::\n{}".format(news_text))
    vect_text = news_cv.transform([news_text]).toarray()
    if model_choice == 'LR':
        predictor = load_prediction_models("pickled_files/streamlit_lr_model.pickle")
        raw_predictions = predictor.predict_proba(vect_text)[0][0]
        predictions = str(predictor.predict_proba(vect_text)[0][0])
        class_predictions = np.where(raw_predictions > .65, 'Fake', 'Real') 
        st.write(str(class_predictions))
    if model_choice == 'NB':
        predictor = load_prediction_models("pickled_files/streamlit_nb_model.pickle")
        predictions = str(predictor.predict_proba(vect_text)[0][0])
        st.write(predictions)
    if model_choice == 'RFOREST':
        predictor = load_prediction_models("pickled_files/streamlit_rf_model.pickle")
        predictions = str(predictor.predict_proba(vect_text)[0][0])
        st.write(predictions)
    if model_choice == 'VC':
        predictor = load_prediction_models("pickled_files/streamlit_vc_model.pickle")
        predictions = str(predictor.predict_proba(vect_text)[0][0])
        st.write(predictions)
        
    
if __name__ == '__main__':
    main()