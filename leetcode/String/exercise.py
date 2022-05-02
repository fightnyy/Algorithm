from torch import nn

from models.layers.scale_dot_product_attention import ScaleDotProductAttention


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_head):
        super(MultiHeadAttention, self).__init__()
        self.attn = ScaleDotProductAttention()
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.head = n_head
        self.w_concat = nn.Linear(d_model, d_model)

    def forward(self, q, k, v, mask=None):
        # 1. dot product with weight matrices
        query = self.w_q(q)
        key = self.w_k(k)
        value = self.w_v(v)

        d_query = self.split(query)
        d_key = self.split(key)
        d_value = self.split(value)
        # 5. visualize attention map
        # TODO : we should implement visualization
        out, score = self.attention(d_query, d_key, d_value, mask=mask)
        return out

    def split(self, tensor):
        """
        split tensor by number of head
        :param tensor: [batch_size, length, d_model]
        :return: [batch_size, head, length, d_tensor]
        """
        batch, seq_len, n_dim = tensor.size()
        d_head = n_dim // self.head
        tensor = tensor.view(batch, self.head, seq_len, d_head)
        # it is similar with group convolution (split by number of heads)

        return tensor

    def concat(self, tensor):
        """
        inverse function of self.split(tensor : torch.Tensor)
        :param tensor: [batch_size, head, length, d_tensor]
        :return: [batch_size, length, d_model]
        """
        batch, head, length, d_tensor = tensor.size()
        n_dim = head * d_tensor
        tensor = tensor.view(batch, length, n_dim)
        return tensor
