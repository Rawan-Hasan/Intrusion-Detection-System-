import joblib
import pandas as pd

def load_model(model_name):
    model = joblib.load(f"models/{model_name}_model.joblib")
   
   
    return model

def preprocess_input(input_data, selected_features):
    df = pd.DataFrame([input_data])
    df = df[selected_features]
   
    return df
