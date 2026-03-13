import mlflow

mlflow.set_tracking_uri("http://localhost:5000")

mlflow.set_experiment("aviation_ml")

with mlflow.start_run():

    mlflow.log_param("model","transformer")
    mlflow.log_metric("rmse",0.24)