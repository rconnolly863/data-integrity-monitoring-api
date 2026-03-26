import pandas as pd

def compare_data():
    df1 = pd.read_csv("data/source_a.csv")
    df2 = pd.read_csv("data/source_b.csv")

    issues = []

    # Amount mismatch
    for i in range(len(df1)):
        if df1.loc[i, "amount"] != df2.loc[i, "amount"]:
            issues.append({
                "id": int(df1.loc[i, "id"]),
                "issue": "Amount mismatch",
                "source_a": int(df1.loc[i, "amount"]),
                "source_b": int(df2.loc[i, "amount"])
            })

    # Missing rows check
    ids_a = set(df1["id"])
    ids_b = set(df2["id"])

    missing_in_b = ids_a - ids_b
    missing_in_a = ids_b - ids_a

    for id_val in missing_in_b:
        issues.append({
            "id": int(id_val),
            "issue": "Missing in source_b"
        })

    for id_val in missing_in_a:
        issues.append({
            "id": int(id_val),
            "issue": "Missing in source_a"
        })

    return issues