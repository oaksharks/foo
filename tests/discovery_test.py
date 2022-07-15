import numpy as np
import pandas as pd

from ylearn.causal_discovery import CausalDiscovery
from ylearn.exp_dataset.gen import gen


def test_ndarray():
    X1 = gen()
    # X1 = pd.DataFrame(X1, columns=[f'x{i}' for i in range(X1.shape[1])])
    cd = CausalDiscovery(hidden_layer_dim=[3])
    est = cd(X1, threshold=0.01)
    print(est)
    assert isinstance(est, np.ndarray)
    assert est.shape[0] == est.shape[1]

    m = cd.matrix2dict(est)
    assert isinstance(m, dict)

    m = cd.matrix2df(est)
    assert isinstance(m, pd.DataFrame)


def test_dataframe():
    X1 = gen()
    X1 = pd.DataFrame(X1, columns=[f'x{i}' for i in range(X1.shape[1])])
    cd = CausalDiscovery(hidden_layer_dim=[3])
    est = cd(X1, threshold=0.01)
    print(est)
    assert isinstance(est, pd.DataFrame)
    assert est.columns.to_list() == X1.columns.to_list()
    assert est.shape[0] == est.shape[1]


def test_return_dict():
    X1 = gen()
    cd = CausalDiscovery(hidden_layer_dim=[3])
    est = cd(X1, threshold=0.01, return_dict=True)
    print(est)
    assert isinstance(est, dict)
