from django.shortcuts import render

# Create your views here.
def python(request):
    d={'a':100,'b':200,'c':150}
    return render(request,'python.html',d)
def sql(request):
    d={'name':'quaries','number':[1234567890]}
    return render(request,'sql.html',d)     