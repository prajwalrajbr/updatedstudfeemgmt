from django.shortcuts import render
from entry.models import Stud_PD, Stud_Admn, Fee_Record, Stud_Fees
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def stud_list(request):
    class data:
        def __init__(self,name,usn,due,total):
            self.Sname=name
            self.USN=usn
            self.Due=due
            self.Total=total
    if request.method=='POST':
        text=request.POST['search']
        search = []
        if text:
            match = Stud_PD.objects.filter(Q(Sname__icontains=text) |
                                         Q(USN__icontains=text)    
                                        ) 
            if match!=None:
                for s in match:
                    try:
                        stud_ad = Stud_Admn.objects.get(Sid=s.Sid)
                    except Exception as e:
                        continue
                    finally:
                        stud_fee = Stud_Fees.objects.get(Adm_No_S=stud_ad.Adm_No)
                        search.append(data(s.Sname,s.USN,stud_fee.Due,stud_fee.Total))
                return render(request, 'details/stud_list.html',{'search':search,'text':text})       
        else:
            return HttpResponseRedirect('/details/')
    else:
        datalist = []
        stud_pds = Stud_PD.objects.all()
        for s in stud_pds:
            try:
                stud_ad = Stud_Admn.objects.get(Sid=s.Sid)
            except Exception as e:
                continue
            finally:
                stud_fee = Stud_Fees.objects.get(Adm_No_S=stud_ad.Adm_No)
                datalist.append(data(s.Sname,s.USN,stud_fee.Due,stud_fee.Total))
        return render(request, 'details/stud_list.html', {'datalist':datalist})

@login_required(login_url="/accounts/login/")
def stud_details(request,usn):
    stud_pd = Stud_PD.objects.get(USN=usn)
    stud_ad = Stud_Admn.objects.get(Sid=stud_pd.Sid)
    return render(request, 'details/stud_details.html', {'stud_pd':stud_pd, 'stud_ad':stud_ad})

@login_required(login_url="/accounts/login/")
def fee_record(request):   
    if request.method=='POST':
        text=request.POST['search']
        if text:
            match=Fee_Record.objects.filter(Q(Stud_Fee_ID__Adm_No_S__Adm_No__icontains=text) |
                                            Q(Added_by__username__icontains=text) |
                                            Q(Date_Paid__icontains=text)
                                            ) 
            if match!=None:
                return render(request, 'details/fee_record.html',{'search':match,'text':text})
        else:
            return HttpResponseRedirect('/details/fee-record/')
    else:
        fee_rcd=Fee_Record.objects.all()
        return render(request,'details/fee_record.html',{'fee_rcd':fee_rcd})