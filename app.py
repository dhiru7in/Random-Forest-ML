from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.user_input import UserInput
from model.predict import predict_output,model,MODEL_VERSION
from Schema.prediction_response import PredictionResponse
    
app = FastAPI()
#This is readable by humnan
@app.get("/")
def home():
    return {"message":"Insurance prediction FAST API"}

#this is readble by machine like AWS/Kubernets etcs.
@app.get("/health")
def health_check():
    return {
        "status":"OK",
        "Version":MODEL_VERSION,
        "Model_Loaded":model is not None
            }

@app.post("/predict",response_model=PredictionResponse)
def predict_premium(data: UserInput):

    UserInput = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction=predict_output(UserInput)

        return JSONResponse(status_code=200, content={'Response': prediction})

    except Exception as e:

        return JSONResponse(status_code=500,content=str(e))




