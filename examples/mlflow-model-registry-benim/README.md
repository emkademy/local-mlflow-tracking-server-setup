
### Docker setup

```bash
docker run --rm -it --ipc host -p 1234:1234 \
           --network mlflow-tracking-server_default \
           -v $PWD:/app \
           -v mlflow-tracking-server_artifact-store:/artifact-store \
           continuumio/anaconda3 bash
```

