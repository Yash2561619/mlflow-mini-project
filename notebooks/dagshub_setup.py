import dagshub
import mlflow

dagshub.init(repo_owner='Yash2561619', repo_name='mlflow-mini-project', mlflow=True)
mlflow.set_tracking_uri('https://dagshub.com/Yash2561619/mlflow-mini-project.mlflow')

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)