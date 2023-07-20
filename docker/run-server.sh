#!/bin/bash


# In this script we are going to run the mlflow tracking server with the backend store and artifact store
# we defined earlier. So, this will be a very simple script.

mlflow server \
    --backend-store-uri "${MLFLOW_BACKEND_STORE}" \
    --default-artifact-root "${MLFLOW_ARTIFACT_STORE}" \
    --host 0.0.0.0 \
    --port "${LOCAL_DEV_MLFLOW_SERVER_PORT}"

# Now, finally, let's create a Make file, then build our Docker image
