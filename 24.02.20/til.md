```
dart_list = dart.list('377480', start='2023-01-01', end='2023-08-14', kind='A', final=False)
```
dart의 리스트에서 377480 코드에 해당하는 마음AI 기업의 23.01.01 부터 23.08.14 까지의 공시를 검색해오겠다는 의미로 final은 최종보고서만 가져올지 잠정보고서까지 가져올지에 대한 부분으로 final=True면 최종보고서 데이터만 가져옴 kind는 어떤 종류인거 같은데 잘은 모르게썽 ㅎ

```
def extract_refine_text(html_string):
    # Remove CSS styles
    no_css = re.sub('<style.*?</style>', '', html_string, flags=re.DOTALL)

    # Remove Inline CSS
    no_inline_css = re.sub('\..*?{.*?}', '', no_css, flags=re.DOTALL)

    # Remove specific undesired strings
    no_undesired = re.sub('\d{4}[A-Za-z0-9_]*" ADELETETABLE="N">', '', no_inline_css)

    # Remove HTML tags
    no_tags = re.sub('<[^>]+>', ' ', no_undesired)

    # Remove special characters and whitespaces
    cleaned = re.sub('\s+', ' ', no_tags).strip()

    # Remove the □ character
    no_square = re.sub('□', '', cleaned)

    # Replace \' with '
    final_text = re.sub(r"\\'", "'", no_square)

    return final_text
```
받아온 데이터중에 복잡한 html태그나 기호들을 떼고 필요한 정보만 가져오기 위해 
텍스트 전처리하는 과정 (주석을 잘 볼것)
```
import FinanceDataReader as fdr
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import sys

# 아래 두 코드만으로도 주식정보를 가지고 온다.
df_krx = fdr.StockListing('KRX')
df_krx.to_csv('stockList.csv', mode='w', encoding='utf-8-sig')

# 이름으로 코드를 찾기위한 단순한 함수
def codeFromName(name):
    nameList=list(df_krx['Name'])
    return df_krx['Symbol'][nameList.index(name)]
----------------------------------------------------------------
dayBfNum        = 1000
strToday        = (datetime.datetime.today()).strftime("%Y%m%d")
strFromDay      = (datetime.datetime.today()-datetime.timedelta(dayBfNum)).strftime("%Y%m%d")
strShowFromDay  = (datetime.datetime.today()-datetime.timedelta(365)).strftime("%Y%m%d")
```
- list(df_krx['Name'])은 'Name' 열의 값을 리스트로 변환
- nameList.index(name)는 입력된 name이 nameList 리스트에서 처음으로 나타나는 위치(인덱스)를 찾음.
- df_krx['Symbol'][...]은 'Symbol' 열에서 특정 인덱스에 해당하는 값을 찾음. 
- 여기서는 name에 해당하는 기업의 심볼(즉, 주식 코드)을 찾기 위해 사용됨.

> 결국, 이 함수는 주어진 기업 이름에 해당하는 주식 코드를 df_krx 데이터프레임에서 찾아 반환
---------------------------------------------------------------------------
- dayBfNum = 1000: 오늘로부터 거슬러 올라갈 일수를 정의함. 여기서는 1000일을 나타냄.
- strToday = (datetime.datetime.today()).strftime("%Y%m%d"): 오늘 날짜를 "YYYYMMDD" 형식의 문자열로 변환. 예를 들어, "20240220"과 같이 표현됨.
- strFromDay = 오늘 날짜에서 dayBfNum만큼 일수를 빼서 과거의 날짜를 계산하고, 그 결과를 "YYYYMMDD" 형식의 문자열로 변환. 이는 오늘로부터 1000일 전의 날짜를 나타냄.
- strShowFromDay = 오늘 날짜에서 365일(1년)을 빼서 과거의 날짜를 계산하고, 그 결과를 "YYYYMMDD" 형식의 문자열로 변환. 이는 오늘로부터 1년 전의 날짜를 나타냄.



위에서 mode='w'의 의미 설명 

파이썬에서 파일을 다룰 때 사용할 수 있는 주요 모드:
- 'r': 읽기 전용 모드. 파일이 존재하지 않으면 오류가 발생
- 'w': 쓰기 전용 모드. 파일이 이미 존재하는 경우 해당 파일의 내용을 삭제하고 처음부터 씁니다. 파일이 존재하지 않으면 새 파일을 생성
- 'a': 파일 추가 모드. 파일이 이미 존재하는 경우, 파일의 끝에서부터 새로운 데이터를 추가합니다. 파일이 존재하지 않으면 새 파일을 생성
- 'x': 배타적 생성 모드. 파일이 이미 존재하지 않을 때만 새 파일을 생성합니다. 파일이 이미 존재하는 경우 오류가 발생

또한, 이 모드 문자 뒤에 +를 추가하여 읽기와 쓰기를 동시에 할 수 있는 모드로 설정할 수 있음. (예: 'r+', 'w+', 'a+'). 예를 들어, 'w+' 모드는 파일을 쓰기 위해 열고, 파일이 이미 존재하는 경우 내용을 삭제한 후 새로운 내용을 쓸 수 있으며, 파일에 대해 읽기도 가능

```
import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

# 데이터프레임 출력
print(df)
```
판다스의 데이터프레임 객체 생성기능이 궁금해져 무작위의 데이터를 가지고 2차원 배열을 생성해보았다. 
```
    Name  Age      City
0   John   28  New York
1   Anna   34     Paris
2  Peter   29    Berlin
3  Linda   32    London
```

그랬더니 위와 같은 배열이 생성된 것을 확인할 수 있다. 