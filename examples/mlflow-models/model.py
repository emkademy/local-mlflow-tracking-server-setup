import mlflow.pyfunc

import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator
from sklearn.feature_extraction.text import CountVectorizer


class SentimentDetector(mlflow.pyfunc.PythonModel):
    def __init__(self, vectorizer: CountVectorizer, model: BaseEstimator) -> None:
        self.vectorizer = vectorizer
        self.model = model

    def predict(self, context, input_df: pd.DataFrame) -> np.ndarray:
        inputs = self.vectorizer.transform(input_df["review"])
        return self.model.predict(inputs)

#  # Construct and save the model
#  model_path = "add_n_model"
#  add5_model = AddN(n=5)
#  mlflow.pyfunc.save_model(path=model_path, python_model=add5_model)
#
#  # Load the model in `python_function` format
#  loaded_model = mlflow.pyfunc.load_model(model_path)
#
#  # Evaluate the model
#  import pandas as pd
#  model_input = pd.DataFrame([range(10)])
#  model_output = loaded_model.predict(model_input)
#  assert model_output.equals(pd.DataFrame([range(5, 15)]))
#
