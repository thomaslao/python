from bs4 import BeautifulSoup
content="""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<title>網頁解析</title>
<meta charset="utf-8">
</head>
<body>

<h1 style="color:rgb(255, 199, 125);">優質大學推薦</h1>
<a href="https://www.ntu.edu.tw/">臺灣大學校網</a>
<h1 style="color:rgb(126, 168, 168);">優質高中推薦</h1>
<a href="http://www.kshs.kh.edu.tw/">高雄中學校網</a>

<h3 style="background-color:green; color:yellow; font-family:Segoe Script; border:3px #000000 solid;">勵志名句</h1>
一分努力~~ 一分收獲~~
金誠所至~~ 金石為開~~
</body>
</html>
"""
bs=BeautifulSoup(content,"html.parser")
print("網頁標題屬性")
print(bs.find("body"))