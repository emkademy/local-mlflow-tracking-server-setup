import mlflow
import numpy as np


logged_model = 'runs:/c47358e1dba5464089591dbd091a2bac/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
random_data = np.random.randn(1, 87931)
prediction = loaded_model.predict(random_data)
print(prediction)
