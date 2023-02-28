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
    df = df.iloc[10:62, 1:8]
    df = df.rename(columns={df.columns[0]: "id", df.columns[1]: "ho", df.columns[2]: "ten", df.columns[3]: "tuoi",
                            df.columns[4]: "toan",
                            df.columns[5]: "ly", df.columns[6]: "hoa"})

    df['diem trung binh'] = (df['toan'] + df['ly'] + df['hoa']) / 3
    df['xep loai'] = df['diem trung binh'].apply(lambda x: "gioi" if x >= 8 else "kha" if x >= 6.5 else "trung binh")

    medium = 0
    good = 0
    rather = 0

    for index in df.index:
        if df['diem trung binh'][index] >= 8:
            good += 1
        elif df['diem trung binh'][index] >= 6.5:
            rather += 1
        else:
            medium += 1

    print(good, medium, rather)

average(readFile)
