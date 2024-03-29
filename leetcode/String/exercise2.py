"""
@author : Hyunwoong
@when : 2019-10-22
@homepage : https://github.com/gusdnd852
"""
import math

from torch import nn


class ScaleDotProductAttention(nn.Module):
    """
    compute scale dot product attention
    Query : given sentence that we focused on (decoder)
    Key : every sentence to check relationship with Query(encoder)
    Value : every sentence same with Key (encoder)
    """

    def __init__(self):
        super(ScaleDotProductAttention, self).__init__()
        self.softmax = nn.Softmax()

    def forward(self, q, k, v, mask=None, e=1e-12):
        # input is 4 dimension tensor
        # [batch_size, head, length, d_tensor]
        batch, n_head, seq_len, d_tensor = v.size()

        k_t = k.view(batch, n_head, d_tensor, seq_len)
        # 1. dot product Query with Key^T to compute similarity
        attn_score = q.matmul(k_t) / math.sqrt(d_tensor)

        # 2. apply masking (opt)
        if mask is not None:
            score = attn_score.masked_fill(mask == 0, -e)

        # 3. pass them softmax to make [0, 1] range
        score = self.softmax(score)

        # 4. multiply with Value
        v = score @ v

        return v, score
