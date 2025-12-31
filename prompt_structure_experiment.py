import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("news_processed.csv")

# 첫 번째 기사 선택
article = df.iloc[0]

title = article["title"]
content = article["content"]
published_at = article["published_at"]

print("제목:", title)
print("작성 시간:", published_at)
print("본문:\n", content)
