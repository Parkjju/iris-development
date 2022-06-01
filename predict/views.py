from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from django.db.models import Q, Count
from .models import *
from django.core import serializers

from accounts.models import *

# 교수님 피드백 : csv -> github -> api 형식 -> ajax -> 뷰

# 공공api -> json -> 머신러닝

# your project absolute path
path = "/Users/yoohajun/PycharmProjects/iris_development"

def predict(request):
    return render(request, 'predict.html')

def predict_chances(request, user_id):

    user_detail = get_object_or_404(PredUser, pk=user_id)

    if request.POST.get('action') == 'post':

        # Receive data from client(input)
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        select_ml = str(request.POST.get('select_ml'))
        username = str(request.user.username)

        if select_ml == 'svc' :
            model = pd.read_pickle(path + "/svc_model.pkl")
            model_name = 'Support Vector Machine'
        else :
            model = pd.read_pickle(path + "/knn_model.pkl")
            model_name = 'K-NeighborsClassifier'

        # dt_model = pd.read_pickle(path + "/dt_model.pkl")

        ml_param = str(model)
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

        # Make prediction
        result = model.predict(input_data)

        # print(metrics.accuracy_score(model._y, result))
        # score = model.score(input_data, result)

        classification = result[0] # result의 0번째 인덱스에 저장이 되어 있음

        # db에 예측한 내용이 객체화되서 저장될 수 있게함
        PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                   petal_width=petal_width, classification=classification, ml_algorithm = model_name ,ml_param = str(model), username=username, user = user_detail)


        return JsonResponse({'result': classification, 'ml_algorithm': model_name,'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width, 'ml_param': ml_param},
                            safe=False)
        # json 형식으로 변수에 담아 client에 response해준다



def view_results(request):
    # Submit prediction and show all
    username = str(request.user.username)
    data = {"dataset": PredResults.objects.filter(Q(username = username))}

    # data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)

def view_visual(request):
    return render(request, "scatter_plot.html")

def view_boxplot(request) :
    return render(request, "box_plot.html")

def view_piechart(request) :

    username = str(request.user.username)
    data = PredResults.objects.filter(Q(username = username))

    setosa = data.filter(Q(classification__contains= 'setosa'))
    versicolor = data.filter(Q(classification__contains= 'versicolor'))
    virginica = data.filter(Q(classification__contains= 'virginica'))

    # setosa = PredResults.objects.filter(Q(classification__contains= 'setosa'))
    # versicolor = PredResults.objects.filter(Q(classification__contains= 'versicolor'))
    # virginica = PredResults.objects.filter(Q(classification__contains= 'virginica'))

    setosa_count = setosa.count()
    versicolor_count = versicolor.count()
    virginica_count = virginica.count()

    return render(request, "pie_chart.html", {'setosa_count':setosa_count,
                                              'versicolor_count':versicolor_count,
                                              'virginica_count':virginica_count})


def view_barchart(request) :
    return render(request, "bar_chart.html")

