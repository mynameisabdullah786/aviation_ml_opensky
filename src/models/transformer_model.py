import torch
import torch.nn as nn

class FlightTransformer(nn.Module):

    def __init__(self,input_dim,model_dim=64,heads=4,layers=2):

        super().__init__()

        self.embedding = nn.Linear(input_dim,model_dim)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=model_dim,
            nhead=heads
        )

        self.transformer = nn.TransformerEncoder(
            encoder_layer,
            num_layers=layers
        )

        self.fc = nn.Linear(model_dim,1)

    def forward(self,x):

        x = self.embedding(x)

        x = self.transformer(x)

        x = x.mean(dim=1)

        return self.fc(x)