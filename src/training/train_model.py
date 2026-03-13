import torch
import mlflow
from models.transformer_model import FlightTransformer
from preprocessing.preprocess_data import preprocess

X = preprocess()

X = torch.tensor(X,dtype=torch.float32)

y = torch.rand(len(X),1)

model = FlightTransformer(input_dim=X.shape[1])

loss_fn = torch.nn.MSELoss()

optimizer = torch.optim.Adam(model.parameters(),lr=0.001)

mlflow.set_experiment("flight_transformer")

with mlflow.start_run():

    for epoch in range(10):

        optimizer.zero_grad()

        output = model(X)

        loss = loss_fn(output,y)

        loss.backward()

        optimizer.step()

    mlflow.log_metric("loss",loss.item())

torch.save(model.state_dict(),"models/transformer_model.pt")