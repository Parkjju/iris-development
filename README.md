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

장고를 이용한 **붖꽃 예측 웹 어플리케이션을 제작합니다.**

이번 프로젝트를 통해 저희는

1. 장고에서 csv 다루기와 머신러닝을 돌려볼 수 있는 경험을 쌓고
2. 깃헙을 통한 협업 경험을 딥하게 얻고
3. 장고 CRUD를 단기간 내에 체득합니다.

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

1. `git pull origin main`을 통해 레포지토리 변경 사항들을 비주얼 스튜디오 코드로 (로컬) 가져옵니다.
2. 비주얼 스튜디오 코드에서 터미널을 열고, `python -m venv myvenv`로 파이썬 가상환경을 설치합니다.
    - 현재 `.gitignore` 파일에 `myvenv`라는 이름의 폴더를 목록에 추가해두었기 때문에 깃에서 해당 폴더는 인식하지 않습니다.
3. 비주얼 스튜디오 코드 터미널에서 윈도우는 `source myvenv/Scripts/activate`, MacOS는 `source myvenv/bin/activate`를 입력하여 가상환경을 실행합니다.
4. `pip install django`를 터미널에 입력합니다. (장고 프레임워크를 설치합니다.)
5. `cd iris`를 터미널에 입력하여 터미널 작업 위치를 `iris` 폴더로 이동합니다.
6. `python manage.py migrate`를 입력합니다.
7. `python manage.py runserver`를 입력하여 로컬 호스트에서 장고 서버가 돌아가는지 확인합니다.

## 레포지토리 커밋내역 최신화 흐름

1. Parkjju/iris-development (원본 레포지토리)에 변경사항이 커밋으로 쌓입니다.
2. fork한 본인 계정의 레포지토리로 이동, `Fetch and Merge`를 통해 원본 레포지토리의 커밋들을 가져옵니다.
3. fork한 본인 계정의 레포지토리에 쌓인 새로운 커밋들을 비주얼 스튜디오 코드에서 `git pull origin main`을 통해 끌고 옵니다.
4. 커밋 최신화 완료!

## 새로운 작업사항 반영하기

1. 먼저 원본 레포지토리인 Parkjju/iris-development 레포지토리로 이동하여 Issue탭으로 이동합니다.
2. 적당한 코멘트와 디스크립션으로 **자신이 할 작업 내역들을 정리하여 업로드합니다.**
3. 커밋 내역들이 최신화 되어 있으면 이때부터 비주얼 스튜디오 코드 (로컬 환경)에서 본격적인 기능 구현을 진행합니다.
4. 기능 구현을 마치고 `git add ......` `git commit -m "커밋메세지, 신경써서 써주세요!!!"`, `git push origin main`으로 fork 레포지토리에 커밋들을 푸시해줍니다.
5. 깃헙 홈페이지에서 fork한 레포지토리로 이동하여 Contribute 버튼을 클릭합니다.
6. Open Pull Request 버튼을 클릭하여 Parkjju/iris-development 레포지토리로 새로 구현한 기능을 보내줍니다.
7. 코드리뷰 진행 후 Merge하여 원본 레포지토리에 새로운 변경사항을 반영해줍니다.
