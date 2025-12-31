import pandas as pd

df = pd.read_csv("seoul_library_202511.csv", encoding="utf-8")
loan_counts = df['도서명'].value_counts()
top10_books = loan_counts.head(10)

top10_df = top10_books.reset_index()
top10_df.columns = ['도서명', '대출건수']
print(top10_df)
