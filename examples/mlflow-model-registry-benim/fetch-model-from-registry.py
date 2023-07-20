import mlflow
import mlflow.pyfunc
import numpy as np
import pandas as pd


mlflow.set_tracking_uri("http://mlflow-tracking-server:5000")


model_name = "demo-model"
model_version = 1

model = mlflow.pyfunc.load_model(
    model_uri=f"models:/{model_name}/{model_version}"
)

df = pd.DataFrame({"review": ["Hi! How are you?"]})
predictions = model.predict(df)
print(predictions)
