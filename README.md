# xlsx to json

다국어 대사 관리를 위해 만든 간단한 스크립트입니다.

- `main.py`와 같은 폴더에 있는 모든 `xlsx` 확장자의 파일 내의 모든 시트를 `json`으로 변환합니다.

- A열을 제외한 모든 열의 1번째 행은 폴더명으로 사용됩니다. 결과물은 해당 이름의 폴더 생성 후 `sheetname.json`의 형태로 저장됩니다.


- A열은 현재 시트의 모든 열에서 key로 사용됩니다. B열 이후는 각 열이 A열의 key에 쌍을 이루는 value로서 각각 한 개의 `json`파일로 저장됩니다.




## Examples

### Input (`sample.xlsx`)

```
.
├── sample.xlsx         # file to convert 
└── main.py
```

#### `sample.xlsx - sheet1`


| |   A   |      B      |       C       |
|-|:-----:| :-------: | :-----------: |
|1|       |     EN      |      KR       |
|2| key1  | first  text | 첫 번째 텍스트 |
|3| key2  | second text | 두 번째 텍스트 |



### Output
```
.
├── EN             
│   └── sheet1.json
├── KR
│   └── sheet1.json    
├── sample.xlsx         # file to convert 
└── main.py
```

#### `EN/sheet1.json`
```
{"key1":"first text","key2":"second text"}
```
#### `KR/sheet1.json`
```
{"key1":"첫 번째 텍스트","key2":"두 번째 텍스트"}
```