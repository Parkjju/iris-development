## 프로젝트 소개 - 내 꽃을 찾아줘 🌸

## Iris Github

### 5.15 -> iris initial commit

__requirement__

```python
pip install uptodate
```

```python
python 3.9
django version 4

conda install asgiref
conda install pandas
conda install scikit-learn
```

### 5.16
- 머신러닝 알고리즘을 선택할 수 있게 기능 추가
- result 스택에 머신러닝 이름과 파라미터 구분 

### 5.22

- 우리가 사용하는 데이터에 fit, 그리고 legend 추가
- but 아직 interactive 하지는 않음

### 6.2
로그아웃 상태에서 프로필 업데이트 접근할 경우 에러 뜨는 것 빼고는 구현 완료했습니다

+ 로그 아웃 상태에서의 각 링크 별 예외처리가 필요할 것 같습니다
---------


장고를 이용한 **붖꽃 예측 웹 어플리케이션을 제작합니다.**

## 필요 스택

-   iris는 정말 머신러닝 이용하기 간단한 좋은 데이터셋
-   머신러닝 알고리즘 (필요한 알고리즘만)
-   Django
-   d3.js 데이터 시각화 라이브러리
    -   d3 라이브러리로 할 수 있는 시각화 종류
    -   [https://hamait.tistory.com/242](https://hamait.tistory.com/242)
    -   [https://hamait.tistory.com/335?category=140423](https://hamait.tistory.com/335?category=140423)
-   부트스트랩
-   백엔드에 초점을 맞춘 프로젝트입니다.

### **데이터셋 : IRIS 데이터 셋**

![Untitled](./image/Untitled.png)

`아이리스 데이터 셋`**이란?**

-   데이터 분석 입문으로 사용하기 좋은 데이터 셋
-   3가지 종류의 붖꽃 종류를 꽃의 길이를 이용해 예측할 수 있는 데이터 셋 (setosa, versicolur, virginica)

## Reference

1. [붖꽃 예측 클론 코딩](https://www.youtube.com/watch?v=6aSf0VM24DM)
2. [D3.js](https://www.youtube.com/watch?v=TOJ9yjvlapY&t=247s)

추후 구현 기능에 따라 README 내용이 추가될 예정입니다 :)

## 프로젝트 세팅 절차

```text
주의 : 반드시 iris폴더 아래에 secrets.json 파일을 생성해야합니다.
```

```json
{
    "SECRET_KEY": "배포해드린 secrets.json 파일 키값"
}
```


