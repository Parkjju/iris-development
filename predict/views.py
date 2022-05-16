from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults

# your project absolute path
path = "/Users/yoohajun/PycharmProjects/iris_development"

def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client(input)
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))

        select_ml = str(request.POST.get('select_ml'))


        # Unpickle model using pandas
        # model = pd.read_pickle(path + "/new_model.pkl")

        if select_ml == 'svc' :
            model = pd.read_pickle(path + "/svc_model.pkl")
            model_name = 'Support Vector Machine'
        else :
            model = pd.read_pickle(path + "/knn_model.pkl")
            model_name = 'K-NeighborsClassifier'

        # dt_model = pd.read_pickle(path + "/dt_model.pkl")

        ml_param = str(model)

        # Make prediction
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])

        classification = result[0] # result의 0번째 인덱스에 저장이 되어 있음


        # db에 예측한 내용이 객체화되서 저장될 수 있게함
        PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                   petal_width=petal_width, classification=classification, ml_algorithm = model_name ,ml_param = str(model) )

        return JsonResponse({'result': classification, 'ml_algorithm': model_name,'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width, 'ml_param': ml_param},
                            safe=False)
        # json 형식으로 변수에 담아 client에 response해준다

def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
