import pandas as pd

readFile = pd.read_excel("input.xlsx")


def sortByName(file):
    df = file
    df = df.iloc[10:62, 1:8]
    df = df.rename(columns={df.columns[0]: "id", df.columns[1]: "ho", df.columns[2]: "ten", df.columns[3]: "tuoi",
                            df.columns[4]: "toan",
                            df.columns[5]: "ly", df.columns[6]: "hoa"})

    df = df.sort_values(by=["ten"])
    print(df)


# sortByName(readFile)


def average(file):
    df = file
    df = df.iloc[10:62, 5:8]
    # df = df.rename(columns={df.columns[0]: "id", df.columns[1]: "ho", df.columns[2]: "ten", df.columns[3]: "tuoi",
    #                         df.columns[4]: "toan",
    #                         df.columns[5]: "ly", df.columns[6]: "hoa"})
    print(pd.DataFrame(df).mean(axis=0))


average(readFile)
