import torch
# import torchaudio

# x = torch.randn(2, 3)
# print("x:", x)
# print("x shape:", x.shape)

# y = torch.cat([x, x],dim=0)
# print("y:", y)
# print("y shape:", y.shape)

x = torch.randn(2,3)
print("x:", x, "shape:", x.shape)
# y = torch.unsqueeze(x,2)
y = x.unsqueeze(2) # 2 ways of implementing the unsqueeze
print("unsqueezed  x:", y)
print("unsqueezed shape:", y.shape)