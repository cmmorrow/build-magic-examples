from pathlib import Path
import pickle
from decimal import Decimal
import sys
from unicodedata import decimal

import numpy as np
import pandas as pd
import pyarrow.feather as feather
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet


def load(filename: Path) -> pd.DataFrame:
    return feather.read_feather(str(filename))


def save_model(model, filename):
    with open(Path(filename), 'wb') as file:
        pickle.dump(model, file)


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def train_model(df: pd.DataFrame, alpha: Decimal, l1_ratio: Decimal):
    train, test = train_test_split(df, test_size=0.25, train_size=0.75)
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    lr = ElasticNet(alpha=float(alpha), l1_ratio=float(l1_ratio))
    lr.fit(train_x, train_y)

    predicted_qualities = lr.predict(test_x)
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)
    print(f"RMSE: {rmse}")
    print(f" MAE: {mae}")
    print(f"  R2: {r2}")

    return lr


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Parameters file path, alpha, and l1_ratio required.")
        sys.exit(1)
    try:
        fn = Path(sys.argv[1]).resolve()
    except Exception:
        print(f"Cannot load file.")
        sys.exit(1)
    alpha = Decimal(sys.argv[2])
    l1_ratio = Decimal(sys.argv[3])
    data = load(fn)
    model = train_model(data, alpha, l1_ratio)
    pickle_file = f"{fn.stem}.pickle"
    try:
        save_model(model, pickle_file)
    except Exception:
        print(f"Could not save {pickle_file}")
