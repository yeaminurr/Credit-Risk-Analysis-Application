from django.shortcuts import render , redirect
from django.http import HttpResponse
import pandas as pd

import numpy as np

from firstapp import form
import sklearn
import pickle
import sys, os
from pathlib import Path
from .loancalculate import calculate
import pickle
#base = os.path.dirname(os.path.abspath())
from pathlib import Path
# from loancalculate import calculator
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#tempdir = BASE_DIR.joinpath()
staticdir = Path.joinpath(BASE_DIR,"static")
ran = Path.joinpath(staticdir, "../static/random")
from django.core.files.storage import FileSystemStorage



# Create your views here.
realdata = dict()
recommendation=dict()
actual = dict()

medianfill = {
 'Current Loan Amount': 11760447.389459714,
 'Term': 0.7220800000000349,
 'Credit Score': 1076.4560893556354,
 'Annual Income': 1378276.5598425677,
 'Years in current job': 5.892355238155139,
 'Home Ownership': 0.9421200000000357,
 'Purpose': 1.3534635340285428,
 'Monthly Debt': 18472.41233580006,
 'Years of Credit History': 18.19914099999905,
 'Number of Open Accounts': 11.12853000000053,
 'Number of Credit Problems': 0.16831000000000476,
 'Current Credit Balance': 294637.3823500047,
 'Maximum Open Credit': 760798.3817476183,
 'Bankruptcies': 0.11774018998757532,
 'Tax Liens': 0.029312931293129337}

def index(request):
    return render(request,'firstapp/bootstrap final.html')
def front(request):
    return HttpResponse("first page")
# def user(request):
#     return render(request,'firstapp/newfile.html')
flag = True
def userinput(request):
    global flag
    global medianfill
    global actual
    # print("pihan joss")
    #
    # frm = form.NameForm()
    # if request.method == 'POST':
    #     print("post hoise")
    #     frm = form.NameForm(request.POST)
    #     if frm.is_valid():
    #         #z=frm.cleaned_data['Annual_Income']
    #         #HttpResponse("first page",z)
    #         print("income", frm.cleaned_data['AnnualIncome'])
    #         print('job', frm.cleaned_data['Years_in_current_job'])
    #         print('ABCD')
    #     else:
    #         print("false")
    #
    #

    context = {'myflag':flag}
    if request.method == 'POST':
        flag = True
        count = 0
        #print('ashchi')
        actual['Credit Score'] = request.POST.get('Credit Score')
        actual["Annual Income"] = request.POST.get('Annual Income')
        actual["Years in current job"] = request.POST.get('Years in current job')
        actual["Home Ownership"] = request.POST.get('Home Ownership')
        actual["Monthly Debt"] = request.POST.get('Monthly Debt')
        actual["Purpose"] = request.POST.get('Purpose')
        actual["Term"] = request.POST.get('Term')
        actual["Years of Credit History"] = request.POST.get('Years of Credit History')
        actual["Number of Open Accounts"] = request.POST.get('Number of Open Accounts')
        actual["Current Credit Balance"] = request.POST.get('Current Credit Balance')
        actual["Maximum Open Credit"] = request.POST.get('Maximum Open Credit')
        actual["Current Loan Amount"] = request.POST.get('Current Loan Amount')

        #print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        #print(request.POST.get('Home Ownership'))
        #print(request.POST.get('Annual Income'))
        for key in actual.keys():
            if actual[key] == "" or actual[key] == 'Select' or actual[key] == None:
                count = count+1
                pass
            else:
                try:
                    medianfill[key] = float(actual[key])
                except:
                    flag=False
        if flag==True and count<10:
            return redirect('/firstapp/result/')
        else:
            flag = False
        context['myflag'] = flag




    return render(request, 'firstapp/bootsrapth.html',context)
nimprove = dict()

def result(request):
    global recommendation
    global nimprove

    global medianfill
    #print('aaaaaaaaaaaaaaaaaaaaaaaaaa')
    #print(medianfill)
    #print(medianfill)
    staticdir = Path.joinpath(BASE_DIR, "static")
    ran = Path.joinpath(staticdir, "../static/random")
    random = pickle.load(open(ran, 'rb'))


    mydata = pd.DataFrame(medianfill, index=[0])
    randomf_predictions = dict()
    randomf_predictions['pred'] = random.predict(mydata)
    new = dict()
    for keys in medianfill.keys():
        nkey =keys
        nkey = nkey.replace(" ","_")
        new[nkey]= medianfill[keys]

    #print(new["Annual_Income"])
    # a = dict()
    # b = dict()
    #
    # a['ajaira'] = "ami ajaira"
    # b['joss'] = 'ami joss'
    # z ={'one':a, 'two':b}
    improve = dict()

    for i in medianfill.keys():
        improve[i]=0
    #print(improve)
    if request.method == 'POST':
        # flag = True
        # count = 0
        #print('ekhaneo ashchi')
        improve['Credit Score'] = request.POST.get('Credit Score')
        improve["Annual Income"] = request.POST.get('Annual Income')
        improve["Home Ownership"] = request.POST.get('Home Ownership')
        improve["Monthly Debt"] = request.POST.get('Monthly Debt')
        improve["Number of Open Accounts"] = request.POST.get('Number of Open Accounts')
        improve["Current Credit Balance"] = request.POST.get('Current Credit Balance')
        improve["Maximum Open Credit"] = request.POST.get('Maximum Open Credit')
        improve["Current Loan Amount"] = request.POST.get('Current Loan Amount')

        for i in improve.keys():
            if improve[i] == None:
                improve[i] = 0
            else:
                improve[i] = int(improve[i])
        nimprove=improve
        #mycalculator = calculator()
        newdata=calculate(mydata,improve)
        #print(newdata)

        #print(improve)
        recommendation = newdata.to_dict('index')
        recommendation = recommendation[0]
        return redirect('/firstapp/recommendation/')

    return render(request, 'firstapp/result.html',randomf_predictions)



def after_result(request):
    #nimprove is the values of tick marks, that user wanted to Upgrade
    #recommendation is the uograded Result
    #medianFill is the userinput
    #final result is the suggestion
    finalresult = dict()
    global nimprove
    global recommendation
    global medianfill
    try:
        del recommendation['Bankruptcies']
        del recommendation['Number of Credit Problems']
        del recommendation['Tax Liens']
        del recommendation['Purpose']

    except:
        pass
    #print("recom", recommendation)
    for k,v in recommendation.items():
        if k=="Home Ownership" or k=="Number of Open Accounts" or k=='Credit Score':
            recommendation[k]=round(recommendation[k])

        else:
            recommendation[k] = round(recommendation[k],2)

    print("recommendations",recommendation)

    #print('keys',recommendation.keys())
    for k,v in recommendation.items():
        temp = v - medianfill[k]
        finalresult[k]= round(temp,2)
        print(k,v,medianfill[k])

    #print("final", finalresult)

    # print(medianfill)
    # #print(nimprove)
    # #print(recommendation)
    # print(finalresult)


    data= {'actual':medianfill,'recommendation':recommendation,'improve':nimprove,'finalresult':finalresult}

    z={"a":1}
    return render(request, 'firstapp/after result.html', data)

#Thesis done
