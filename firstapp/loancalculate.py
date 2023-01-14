import pickle
from pathlib import Path
threshold = {'Loan Status': 1.0, 'Current Loan Amount': 321266.0, 'Term': 1.0, 'Credit Score': 730.0,
             'Annual Income': 1378276.559842169, 'Years in current job': 6.0, 'Home Ownership': 1.0,
             'Purpose': 1.0, 'Monthly Debt': 16145.06, 'Years of Credit History': 17.0,
             'Number of Open Accounts': 10.0,
             'Number of Credit Problems': 0.0, 'Current Credit Balance': 208411.0, 'Maximum Open Credit': 475288.0,
             'Bankruptcies': 0.0, 'Tax Liens': 0.0}
importance = ['Credit Score', 'Current Loan Amount', 'Monthly Debt', 'Maximum Open Credit',
              'Current Credit Balance', 'Annual Income', 'Number of Open Accounts', 'Home Ownership']
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

staticdir = Path.joinpath(BASE_DIR, "static")
ran = Path.joinpath(staticdir, "../static/random")
randomf = pickle.load(open(ran, 'rb'))


def calculate(dummy,checked):
    global importance
    global threshold
    global randomf
    abcd=1
    flag = 0



    for run in range(1000):

        for i in importance:
            if checked[i] == 1:
                if i == 'Current Loan Amount' or i == 'Monthly Debt' or i == 'Maximum Open Credit' or i == 'Current Credit Balance' or i == 'Number of Open Accounts':
                    if float(dummy[i]) > threshold[i]:
                        dummy[i] = dummy[i] - threshold[i] / 1000
                        if randomf.predict(dummy) == 1:
                            print(f'yay got it itr {run}')
                            flag = 1
                            break

                else:
                    if i == 'Credit Score':
                        if float(dummy[i]) < threshold[i]:
                            dummy[i] = dummy[i] + threshold[i] / 1000
                            if randomf.predict(dummy) == 1:
                                print(f'yay got it itr {run}')
                                flag = 1
                                break
                    else:
                        if float(dummy[i]) < threshold[i]:
                            dummy[i] = dummy[i] + threshold[i] / 1000
                            if randomf.predict(dummy) == 1:
                                print(f'yay got it itr {run}')
                                flag = 1
                                break
        if flag == 1:
            break
    print(dummy)

    return dummy

