# xlsx to json

�ٱ��� ��� ������ ���� ���� ������ ��ũ��Ʈ�Դϴ�.

- `main.py`�� ���� ������ �ִ� ��� `xlsx` Ȯ������ ���� ���� ��� ��Ʈ�� `json`���� ��ȯ�մϴ�.

- A���� ������ ��� ���� 1��° ���� ���������� ���˴ϴ�. ������� �ش� �̸��� ���� ���� �� `sheetname.json`�� ���·� ����˴ϴ�.


- A���� ���� ��Ʈ�� ��� ������ key�� ���˴ϴ�. B�� ���Ĵ� �� ���� A���� key�� ���� �̷�� value�μ� ���� �� ���� `json`���Ϸ� ����˴ϴ�.




## Examples

### Input (`sample.xlsx`)

```
.
������ sample.xlsx         # file to convert 
������ main.py
```

#### `sample.xlsx - sheet1`


| |   A   |      B      |       C       |
|-|:-----:| :-------: | :-----------: |
|1|       |     EN      |      KR       |
|2| key1  | first  text | ù ��° �ؽ�Ʈ |
|3| key2  | second text | �� ��° �ؽ�Ʈ |



### Output
```
.
������ EN             
��   ������ sheet1.json
������ KR
��   ������ sheet1.json    
������ sample.xlsx         # file to convert 
������ main.py
```

#### `EN/sheet1.json`
```
{"key1":"first text","key2":"second text"}
```
#### `KR/sheet1.json`
```
{"key1":"ù ��° �ؽ�Ʈ","key2":"�� ��° �ؽ�Ʈ"}
```