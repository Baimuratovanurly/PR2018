
# coding: utf-8

# In[ ]:
from ipywidgets import interact_manual
def pro(a, b):
    return a*b*0.001
def percent(a):
    return a*0.01
pyDatalog.create_terms('employee, net_salary, tax_rate')
@interact_manual
def get_input(name='User', salary=100, time = 1):
    employee[name]=salary*time
    per = 0.03*employee[name]
    tax_rate[name] = pro(employee[name], per)
    net_salary[X] = employee[X]*(1-percent(tax_rate[X]))
    print(net_salary[X].in_(range(700)) & (net_salary[X] >50) )
    print(net_salary[X]==Y)

