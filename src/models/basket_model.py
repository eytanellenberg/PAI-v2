from sklearn.ensemble import RandomForestRegressor


def fit_basket_model(X, y):
    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=5,
        random_state=42,
    )
    model.fit(X, y)
    return model
