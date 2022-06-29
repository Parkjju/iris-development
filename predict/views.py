from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from sklearn import metrics
from sklearn.model_selection import train_test_split
from django.db.models import Q, Count
from .models import *
from django.core import serializers
import json

from accounts.models import *
from django.contrib.auth.decorators import login_required, permission_required

from django.core.paginator import Paginator

# 공공api -> json -> 머신러닝

# your project root => absolute path
path = "/Users/yoohajun/PycharmProjects/iris_development"

@login_required
def predict(request):
    # request => get auth user id
    u_id = request.user.id
    # Preduser = userid => pk
    user_data = PredUser.objects.filter(Q(user_id = u_id))
    # 해당 pk에 해당하는 객체 하나만
    preduser = user_data[0]
    # 위의 객체를 predict.html에 렌더링
    return render(request, 'predict.html', {'preduser' : preduser})

# request => django.auth.id
# user id => profile id
@login_required
def predict_chances(request, user_id):

    # user_id => preduser pk
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

        elif select_ml == 'dt' :
            model = pd.read_pickle(path + "/dt_model.pkl")
            model_name = 'Decision Tree'

        else :
            model = pd.read_pickle(path + "/knn_model.pkl")
            model_name = 'K-NeighborsClassifier'


        ml_param = str(model)
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

        # Make prediction
        result = model.predict(input_data)

        classification = result[0] # result의 0번째 인덱스에 저장이 되어 있음

        # db에 예측한 내용이 객체화되서 저장될 수 있게함
        PredResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length,
                                   petal_width=petal_width, classification=classification, ml_algorithm = model_name ,ml_param = str(model), username=username, user = user_detail)


        return JsonResponse({'result': classification, 'ml_algorithm': model_name,'sepal_length': sepal_length,
                             'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width, 'ml_param': ml_param},
                            safe=False)
        # json 형식으로 변수에 담아 client에 response해준다


@login_required
def view_results(request):
    # Submit prediction and show all
    username = str(request.user.username)
    dataset = PredResults.objects.filter(Q(username = username))
    # data = {"dataset": PredResults.objects.all()}
    data = PredResults.objects.filter(Q(username = username))

    setosa = data.filter(Q(classification__contains= 'setosa'))
    versicolor = data.filter(Q(classification__contains= 'versicolor'))
    virginica = data.filter(Q(classification__contains= 'virginica'))

    setosa_count = setosa.count()
    versicolor_count = versicolor.count()
    virginica_count = virginica.count()

    return render(request, "results.html", {"dataset" : dataset,
                                            'setosa_count': setosa_count,
                                            'versicolor_count': versicolor_count,
                                            'virginica_count': virginica_count
                                            })
# admin dashboard
@login_required
@permission_required('is_superuser')
def admin_results(request):

    # admin dashboard table with paginator
    dataset_all = PredResults.objects.all().order_by('user_id')
    page = int(request.GET.get('p', 1)) # 없으면 1로 지정
    paginator = Paginator(dataset_all, 5) # 한 페이지 당 몇개 씩 보여줄 지 지정
    dataset = paginator.get_page(page)

    # barchart
    data = PredResults.objects

    setosa = data.filter(Q(classification__contains= 'setosa'))
    versicolor = data.filter(Q(classification__contains= 'versicolor'))
    virginica = data.filter(Q(classification__contains= 'virginica'))

    setosa_count = setosa.count()
    versicolor_count = versicolor.count()
    virginica_count = virginica.count()

    svc = data.filter(Q(ml_algorithm__contains= 'Support Vector Machine'))
    knn = data.filter(Q(ml_algorithm__contains= 'K-NeighborsClassifier'))
    dt = data.filter(Q(ml_algorithm__contains= 'Decision Tree'))

    svc_count = svc.count()
    knn_count = knn.count()
    dt_count = dt.count()

    # count by user name
    predcounts = PredUser.objects.all().annotate(pred_count = Count('predresults'))

    # Preduser가 참조하는 User의 username을 가져옴 (일종의 조인)
    data_dict = []
    for pred in predcounts:
        item = {"group": pred.user.username, "value": pred.pred_count}
        data_dict.append(item)

    json_dict = dict()
    json_dict['data'] = data_dict
    # print(data_dict)

    temp = json.dumps(json_dict) # error : Object of type User is not JSON serializable
    jsonData = json.dumps(temp)
    print(jsonData)
    print(type(jsonData))

    return render(request, "admin_results.html", {'setosa_count':setosa_count,
                                             'versicolor_count':versicolor_count,
                                             'virginica_count':virginica_count,
                                              'svc_count': svc_count,
                                              'knn_count': knn_count,
                                              'dt_count': dt_count,
                                             "dataset": dataset,
                                              "predcounts" : predcounts,
                                              "data_dict": data_dict,
                                              "jsonData" : jsonData
                                             })



@login_required
def edit(request, id):
    post = PredResults.objects.get(id = id)
    context = {'post' : post}
    return render(request, 'p_edit.html', context)

@login_required
def update(request, id):
    # update도 id 하나만 하기 때문에
    post = PredResults.objects.get(id=id)
    post.ml_algorithm = request.POST['ml_algorithm']
    post.ml_param = request.POST['ml_param']
    post.save()
    return redirect('predict:results') #redirect를 통해 'results' name url로 이동


@csrf_exempt
@login_required
def delete(request, id):
    post = PredResults.objects.get(id=id)
    post.delete() # 성공 시
    return redirect('predict:results') # 이 부분 redirection


@login_required
def view_visual(request):
    return render(request, "scatter_plot.html")


@login_required
def view_boxplot(request) :
    return render(request, "box_plot.html")


@login_required
def view_barchart(request) :
    return render(request, "bar_chart.html")