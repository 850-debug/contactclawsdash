def apply_filters(df, industry, province, keyword):

    if industry:
        df = df[df["industry"].str.contains(industry, case=False)]

    if province:
        df = df[df["province"] == province]

    if keyword:
        df = df[df.apply(
            lambda row: keyword.lower() in str(row).lower(),
            axis=1
        )]

    return df