import torch

device = torch.device("mps")

print(torch.backends.mps.is_available())
print(torch.backends.mps.is_built())
