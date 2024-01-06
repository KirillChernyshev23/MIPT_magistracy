import jax
from jax import nn
jax.config.update("jax_enable_x64", True)


def get_test_function(n):
    key = jax.random.PRNGKey(42)
    subkeys = jax.random.split(key, 3)
    W1 = jax.random.normal(subkeys[0], (n, n)) / n
    W2 = jax.random.normal(subkeys[1], (n, n)) / n
    W3 = jax.random.normal(subkeys[2], (10*n, n)) / n
    def test_function(x, *args):
        if type(x) == tuple:
            x = x[0]
        x = nn.sigmoid(W1 @ x) + x
        x = nn.sigmoid(W2 @ x) + x
        x = W3 @ x
        return x
    return test_function
