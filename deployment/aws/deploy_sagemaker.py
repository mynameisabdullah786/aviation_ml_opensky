import sagemaker
from sagemaker.pytorch import PyTorchModel

model = PyTorchModel(
    model_data="s3://bucket/model.tar.gz",
    role="SageMakerRole",
    entry_point="inference.py"
)

predictor = model.deploy(
    instance_type="ml.m5.large",
    initial_instance_count=1
)