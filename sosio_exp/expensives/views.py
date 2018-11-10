from django.shortcuts import render
from .models import friendsInfo,moneyInfo
# Create your views here.


def savesfrnds(request):
    name = request.POST.get("name")
    cno = request.POST.get("cno")
    val = friendsInfo.objects.filter(cno=cno)
    if val:
        return render(request, "addfriends.html", {"mes": "already register"})
    else:
        res = friendsInfo.objects.filter(name=name)
        if res:
            return render(request, "addfriends.html", {"mes": "change user name"})
        else:
            na = friendsInfo(name=name, cno=cno)
            na.save()
            return render(request, "addfriends.html", {"mes": "saved success"})


def showfriends(request):
    no = request.POST.get("del")
    if no:
        friendsInfo.objects.filter(cno=no).delete()
    f1 = friendsInfo.objects.all()
    return render(request, "addmny.html", {"mes": f1})


def savemny(request):
    frnds = request.POST.getlist("friends")
    amnt = request.POST.get("amnt")
    purpose = request.POST.get("purpose")
    date = request.POST.get("date")
    lenght = len(frnds)
    g2 = (int(amnt) /lenght)
    print(g2)
    i = 0
    for x in frnds:
        d1 = moneyInfo(name=frnds[i], expensive=g2,date=date,purpose=purpose)
        d1.save()
        i += 1
    return showfriends(request)


def showmny(request):
    frnds = friendsInfo.objects.all()
    return render(request, "showmny.html", {"mes": frnds})


def showingdata(request):
    frnd = friendsInfo.objects.all()
    frnds = request.POST.get("friends")
    fr1 = moneyInfo.objects.filter(name=frnds)
    return render(request, "showmny.html", {"det": fr1, "mes": frnd})


def deletemny(request):
    no = request.POST.get("del")
    moneyInfo.objects.filter(id=no).delete()
    frnd = friendsInfo.objects.all()
    return render(request, "showmny.html", {"mes": frnd})


def deletalldata(request):
    moneyInfo.objects.all().delete()
    friendsInfo.objects.all().delete()
    return render(request, "index.html")