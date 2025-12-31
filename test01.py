import pandas as pd

df = pd.read_csv("seoul_library_202511.csv", encoding = "utf-8")
'''
#############
#도전문제 1
topTen = df["도서명"].value_counts().head(10)
topTen = topTen.reset_index()
topTen.columns = ["도서명", "대출건수"]
topTen.to_csv("top10_books_by_loan.csv", encoding="utf-8", index=False)
'''

#############
#도전문제 2
a = df.groupby("주제분류번호").agg({"도서명":"count"})
b = df["주제분류번호"].value_counts()
print(a)
print(b)
