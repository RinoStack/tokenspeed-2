import torch

class TokenSpeed:
    def __init__(self, model_path):
        self.model = torch.load(model_path)
    
    def generate(self, prompt):
        # Fast inference
        return self.model.generate(prompt)