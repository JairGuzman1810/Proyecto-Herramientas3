import pandas as pd
from sklearn.ensemble import RandomForestClassifier
model = "matches_rollig.csv"
matches_rolling = pd.read_csv(model)


predictorsv1 = ["venue_code", "opp_code", "hour", "day_code"]
cols = ["gf", "ga", "sh", "sot", "dist", "fk", "pk", "pkatt"]
new_cols = [f"{c}_rolling" for c in cols]
predictorsv2 = predictorsv1 + new_cols


def make_predictionsv1(data):
    rf = RandomForestClassifier(n_estimators=50, min_samples_split=10, random_state=1)
    train = matches_rolling[matches_rolling["date"] < '2022-01-01']
    rf.fit(train[predictorsv1], train["target"])
    pred = rf.predict(data[predictorsv1])
    return pred

def make_predictionsv2(data):
    rfv2 = RandomForestClassifier(n_estimators=50, min_samples_split=10, random_state=1)
    trainv2 = matches_rolling[matches_rolling["date"] < '2022-01-01']
    rfv2.fit(trainv2[predictorsv2], trainv2["target"])
    predv2 = rfv2.predict(data[predictorsv2])
    return predv2