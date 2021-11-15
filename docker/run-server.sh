#!/bin/bash

mlflow server \
    --backend-store-uri $BACKEND_STORE_URI \
    --default-artifact-root $ARTIFACT_STORE \
    --host $MLFLOW_HOST \
    --port $MLFLOW_PORT
