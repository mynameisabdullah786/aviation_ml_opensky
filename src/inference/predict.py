import torch
from models.transformer_model import FlightTransformer

def load_model():

    model = FlightTransformer(input_dim=6)

    model.load_state_dict(
        torch.load("models/transformer_model.pt")
    )

    model.eval()

    return model