import json
from django.shortcuts import render,redirect
from .models import Stud_PD,Stud_Admn,Fee_Str,Fee_Record,Stud_Fees
from django.shortcuts import get_list_or_404,get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponse

@login_required(login_url="/accounts/login/")
def stud_pd_entry(request):

    if request.is_ajax():
        stud_pds = Stud_PD.objects.all()
        stud_admns = Stud_Admn.objects.all()
        usnList = []
        for s in stud_pds:
            usnList.append(s.USN)
        adNoList = []
        for a in stud_admns:
            adNoList.append(a.Adm_No)
        data = [usnList, adNoList]
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')

    if request.method == 'POST':
        form1 = forms.create_stud_pd(request.POST)
        form2 = forms.create_stud_admn(request.POST)
        if form1.is_valid()&form2.is_valid():
            instance1 = form1.save(commit=False)
            instance1.Added_by = request.user
            instance1.save()
            instance2 = form2.save(commit=False)
            try:
                fee_foreign = Fee_Str.objects.get(Course=request.POST['Course'],Branch=request.POST['Branch'],Adm_Year=request.POST['Adm_Year'],Adm_type=request.POST['Adm_Type'],Quota=request.POST['Quota'])          
            except:
                fee_foreign = Fee_Str.objects.get(Fid=1)
            else:
                instance2.Fid = fee_foreign 
            instance2.Sid = instance1      
            instance2.save()
            instance3 = Stud_Fees.objects.create(Adm_No_S=instance2,Total=fee_foreign.Total,Due=fee_foreign.Total)
            instance3.save()
            return redirect('details:list')
    else:    
        form1 = forms.create_stud_pd()
        form2 = forms.create_stud_admn()
    return render(request, 'entry/createstudpd.html',{'form1':form1,'form2':form2})

@login_required(login_url="/accounts/login/")
def update_stud_fee(request,usn): 

    if request.is_ajax():
        stud_pd = Stud_PD.objects.get(USN=usn)
        stud_ad = Stud_Admn.objects.get(Sid=stud_pd.Sid)
        fee_str = Fee_Str.objects.get(Fid=str(stud_ad.Fid))
        stud_fee = Stud_Fees.objects.get(Adm_No_S=stud_ad.Adm_No)
        data = json.dumps(stud_fee.Due)
        return HttpResponse(data, content_type='application/json')

    if request.method == 'POST':
        stud_pd = Stud_PD.objects.get(USN=usn)
        stud_ad = Stud_Admn.objects.get(Sid=stud_pd.Sid)
        fee_str = Fee_Str.objects.get(Fid=str(stud_ad.Fid))
        stud_fee = Stud_Fees.objects.get(Adm_No_S=stud_ad.Adm_No)
        try:
            amt=int(request.POST.get('amt',0))
        except:
            amt=0
        if(amt):
            if amt>0:
                if amt<=stud_fee.Due:
                    if(amt):
                        if stud_fee.Apti_1_Paid!=fee_str.Apti_1:
                            if amt>=fee_str.Apti_1:
                                stud_fee.Apti_1_Paid=fee_str.Apti_1
                                amt=amt-fee_str.Apti_1
                            elif (amt+stud_fee.Apti_1_Paid)>=fee_str.Apti_1:
                                amt=amt+stud_fee.Apti_1_Paid-fee_str.Apti_1
                                stud_fee.Apti_1_Paid=fee_str.Apti_1
                            else:
                                stud_fee.Apti_1_Paid+=amt
                                amt=0 
                            
                    if(amt):
                        if stud_fee.Tech_2_Paid!=fee_str.Tech_2:
                            if amt>=fee_str.Tech_2:
                                stud_fee.Tech_2_Paid=fee_str.Tech_2
                                amt=amt-fee_str.Tech_2
                            elif (amt+stud_fee.Tech_2_Paid)>=fee_str.Tech_2:
                                amt=amt+stud_fee.Tech_2_Paid-fee_str.Tech_2
                                stud_fee.Tech_2_Paid=fee_str.Tech_2
                            else :
                                stud_fee.Tech_2_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Book_3_Paid!=fee_str.Book_3:
                            if amt>=fee_str.Book_3:
                                stud_fee.Book_3_Paid=fee_str.Book_3
                                amt=amt-fee_str.Book_3
                            elif (amt+stud_fee.Book_3_Paid)>=fee_str.Book_3:
                                amt=amt+stud_fee.Book_3_Paid-fee_str.Book_3
                                stud_fee.Book_3_Paid=fee_str.Book_3
                            else:
                                stud_fee.Book_3_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.IndP_4_Paid!=fee_str.IndP_4:
                            if amt>=fee_str.IndP_4:
                                stud_fee.IndP_4_Paid=fee_str.IndP_4
                                amt=amt-fee_str.IndP_4
                            elif (amt+stud_fee.IndP_4_Paid)>=fee_str.IndP_4:
                                amt=amt+stud_fee.IndP_4_Paid-fee_str.IndP_4
                                stud_fee.IndP_4_Paid=fee_str.IndP_4
                            else:
                                stud_fee.IndP_4_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.IndV_5_Paid!=fee_str.IndV_5:
                            if amt>=fee_str.IndV_5:
                                stud_fee.IndV_5_Paid=fee_str.IndV_5
                                amt=amt-fee_str.IndV_5
                            elif (amt+stud_fee.IndV_5_Paid)>=fee_str.IndV_5:
                                amt=amt+stud_fee.IndV_5_Paid-fee_str.IndV_5
                                stud_fee.IndV_5_Paid=fee_str.IndV_5
                            else:
                                stud_fee.IndV_5_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Inte_6_Paid!=fee_str.Inte_6:
                            if amt>=fee_str.Inte_6:
                                stud_fee.Inte_6_Paid=fee_str.Inte_6
                                amt=amt-fee_str.Inte_6
                            elif (amt+stud_fee.Inte_6_Paid)>=fee_str.Inte_6:
                                amt=amt+stud_fee.Inte_6_Paid-fee_str.Inte_6
                                stud_fee.Inte_6_Paid=fee_str.Inte_6
                            else:
                                stud_fee.Inte_6_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Libr_7_Paid!=fee_str.Libr_7:
                            if amt>=fee_str.Libr_7:
                                stud_fee.Libr_7_Paid=fee_str.Libr_7
                                amt=amt-fee_str.Libr_7
                            elif (amt+stud_fee.Libr_7_Paid)>=fee_str.Libr_7:
                                amt=amt+stud_fee.Libr_7_Paid-fee_str.Libr_7
                                stud_fee.Libr_7_Paid=fee_str.Libr_7
                            else:
                                stud_fee.Libr_7_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Semi_8_Paid!=fee_str.Semi_8:
                            if amt>=fee_str.Semi_8:
                                stud_fee.Semi_8_Paid=fee_str.Semi_8
                                amt=amt-fee_str.Semi_8
                            elif (amt+stud_fee.Semi_8_Paid)>=fee_str.Semi_8:
                                amt=amt+stud_fee.Semi_8_Paid-fee_str.Semi_8
                                stud_fee.Semi_8_Paid=fee_str.Semi_8
                            else:
                                stud_fee.Semi_8_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Soft_9_Paid!=fee_str.Soft_9:
                            if amt>=fee_str.Soft_9:
                                stud_fee.Soft_9_Paid=fee_str.Soft_9
                                amt=amt-fee_str.Soft_9
                            elif (amt+stud_fee.Soft_9_Paid)>=fee_str.Soft_9:
                                amt=amt+stud_fee.Soft_9_Paid-fee_str.Soft_9
                                stud_fee.Soft_9_Paid=fee_str.Soft_9
                            else:
                                stud_fee.Soft_9_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Conf_10_Paid!=fee_str.Conf_10:
                            if amt>=fee_str.Conf_10:
                                stud_fee.Conf_10_Paid=fee_str.Conf_10
                                amt=amt-fee_str.Conf_10
                            elif (amt+stud_fee.Conf_10_Paid)>=fee_str.Conf_10:
                                amt=amt+stud_fee.Conf_10_Paid-fee_str.Conf_10
                                stud_fee.Conf_10_Paid=fee_str.Conf_10
                            else:
                                stud_fee.Conf_10_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Subj_11_Paid!=fee_str.Subj_11:
                            if amt>=fee_str.Subj_11:
                                stud_fee.Subj_11_Paid=fee_str.Subj_11
                                amt=amt-fee_str.Subj_11
                            elif (amt+stud_fee.Subj_11_Paid)>=fee_str.Subj_11:
                                amt=amt+stud_fee.Subj_11_Paid-fee_str.Subj_11
                                stud_fee.Subj_11_Paid=fee_str.Subj_11
                            else:
                                stud_fee.Subj_11_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Spor_12_Paid!=fee_str.Spor_12:
                            if amt>=fee_str.Spor_12:
                                stud_fee.Spor_12_Paid=fee_str.Spor_12
                                amt=amt-fee_str.Spor_12
                            elif (amt+stud_fee.Spor_12_Paid)>=fee_str.Spor_12:
                                amt=amt+stud_fee.Spor_12_Paid-fee_str.Spor_12
                                stud_fee.Spor_12_Paid=fee_str.Spor_12
                            else:
                                stud_fee.Spor_12_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Tran_13_Paid!=fee_str.Tran_13:
                            if amt>=fee_str.Tran_13:
                                stud_fee.Tran_13_Paid=fee_str.Tran_13
                                amt=amt-fee_str.Tran_13
                            elif (amt+stud_fee.Tran_13_Paid)>=fee_str.Tran_13:
                                amt=amt+stud_fee.Tran_13_Paid-fee_str.Tran_13
                                stud_fee.Tran_13_Paid=fee_str.Tran_13
                            else:
                                stud_fee.Tran_13_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Tuti_14_Paid!=fee_str.Tuti_14:
                            if amt>=fee_str.Tuti_14:
                                stud_fee.Tuti_14_Paid=fee_str.Tuti_14
                                amt=amt-fee_str.Tuti_14
                            elif (amt+stud_fee.Tuti_14_Paid)>=fee_str.Tuti_14:
                                amt=amt+stud_fee.Tuti_14_Paid-fee_str.Tuti_14
                                stud_fee.Tuti_14_Paid=fee_str.Tuti_14
                            else:
                                stud_fee.Tuti_14_Paid+=amt
                                amt=0

                    if(amt):
                        if stud_fee.Volu_15_Paid!=fee_str.Volu_15:
                            if amt>=fee_str.Volu_15:
                                stud_fee.Volu_15_Paid=fee_str.Volu_15
                                amt=amt-fee_str.Volu_15
                            elif (amt+stud_fee.Volu_15_Paid)>=fee_str.Volu_15:
                                amt=amt+stud_fee.Volu_15_Paid-fee_str.Volu_15
                                stud_fee.Volu_15_Paid=fee_str.Volu_15
                            else:
                                stud_fee.Volu_15_Paid+=amt
                                amt=0
                                
                    stud_fee.Paid=stud_fee.Apti_1_Paid+stud_fee.Tech_2_Paid+stud_fee.Book_3_Paid+stud_fee.IndP_4_Paid+stud_fee.IndV_5_Paid+stud_fee.Inte_6_Paid+stud_fee.Libr_7_Paid+stud_fee.Semi_8_Paid+stud_fee.Soft_9_Paid+stud_fee.Conf_10_Paid+stud_fee.Subj_11_Paid+stud_fee.Spor_12_Paid+stud_fee.Tran_13_Paid+stud_fee.Tuti_14_Paid+stud_fee.Volu_15_Paid
                    due=stud_fee.Due
                    stud_fee.Due=stud_fee.Total-stud_fee.Paid
                    due-=stud_fee.Due
                    stud_fee.save()

                    if due:
                        fee_record = Fee_Record.objects.create(Stud_Fee_ID=stud_fee,Fee_Paid=due,Added_by=request.user)
                        fee_record.save()       
        
        else:           
        
            paid1=request.POST.get('paid1',False)
            if paid1:
                stud_fee.Apti_1_Paid=fee_str.Apti_1
            paid2=request.POST.get('paid2',False)
            if paid2:
                stud_fee.Tech_2_Paid=fee_str.Tech_2
            paid3=request.POST.get('paid3',False)
            if paid3:
                stud_fee.Book_3_Paid=fee_str.Book_3
            paid4=request.POST.get('paid4',False)
            if paid4:
                stud_fee.IndP_4_Paid=fee_str.IndP_4
            paid5=request.POST.get('paid5',False)
            if paid5:
                stud_fee.IndV_5_Paid=fee_str.IndV_5
            paid6=request.POST.get('paid6',False)
            if paid6:
                stud_fee.Inte_6_Paid=fee_str.Inte_6
            paid7=request.POST.get('paid7',False)
            if paid7:
                stud_fee.Libr_7_Paid=fee_str.Libr_7
            paid8=request.POST.get('paid8',False)
            if paid8:
                stud_fee.Semi_8_Paid=fee_str.Semi_8
            paid9=request.POST.get('paid9',False)
            if paid9:
                stud_fee.Soft_9_Paid=fee_str.Soft_9
            paid10=request.POST.get('paid10',False)
            if paid10:
                stud_fee.Conf_10_Paid=fee_str.Conf_10
            paid11=request.POST.get('paid11',False)
            if paid11:
                stud_fee.Subj_11_Paid=fee_str.Subj_11
            paid12=request.POST.get('paid12',False)
            if paid12:
                stud_fee.Spor_12_Paid=fee_str.Spor_12
            paid13=request.POST.get('paid13',False)
            if paid13:
                stud_fee.Tran_13_Paid=fee_str.Tran_13
            paid14=request.POST.get('paid14',False)
            if paid14:
                stud_fee.Tuti_14_Paid=fee_str.Tuti_14
            paid15=request.POST.get('paid15',False)
            if paid15:
                stud_fee.Volu_15_Paid=fee_str.Volu_15
            
            stud_fee.Paid=stud_fee.Apti_1_Paid+stud_fee.Tech_2_Paid+stud_fee.Book_3_Paid+stud_fee.IndP_4_Paid+stud_fee.IndV_5_Paid+stud_fee.Inte_6_Paid+stud_fee.Libr_7_Paid+stud_fee.Semi_8_Paid+stud_fee.Soft_9_Paid+stud_fee.Conf_10_Paid+stud_fee.Subj_11_Paid+stud_fee.Spor_12_Paid+stud_fee.Tran_13_Paid+stud_fee.Tuti_14_Paid+stud_fee.Volu_15_Paid
            due=stud_fee.Due
            stud_fee.Due=stud_fee.Total-stud_fee.Paid
            due-=stud_fee.Due
            stud_fee.save()
            if due:
                fee_record = Fee_Record.objects.create(Stud_Fee_ID=stud_fee,Fee_Paid=due,Added_by=request.user)
                fee_record.save()

         
    else:   
        stud_pd = Stud_PD.objects.get(USN=usn)
        stud_ad = Stud_Admn.objects.get(Sid=stud_pd.Sid)
        fee_str = Fee_Str.objects.get(Fid=str(stud_ad.Fid))
        stud_fee = Stud_Fees.objects.get(Adm_No_S=stud_ad.Adm_No)
    fee={
        'fee1':fee_str.Apti_1-stud_fee.Apti_1_Paid,
        'fee2':fee_str.Tech_2-stud_fee.Tech_2_Paid,
        'fee3':fee_str.Book_3-stud_fee.Book_3_Paid,
        'fee4':fee_str.IndP_4-stud_fee.IndP_4_Paid,
        'fee5':fee_str.IndV_5-stud_fee.IndV_5_Paid,
        'fee6':fee_str.Inte_6-stud_fee.Inte_6_Paid,
        'fee7':fee_str.Libr_7-stud_fee.Libr_7_Paid,
        'fee8':fee_str.Semi_8-stud_fee.Semi_8_Paid,
        'fee9':fee_str.Soft_9-stud_fee.Soft_9_Paid,
        'fee10':fee_str.Conf_10-stud_fee.Conf_10_Paid,
        'fee11':fee_str.Subj_11-stud_fee.Subj_11_Paid,
        'fee12':fee_str.Spor_12-stud_fee.Spor_12_Paid,
        'fee13':fee_str.Tran_13-stud_fee.Tran_13_Paid,
        'fee14':fee_str.Tuti_14-stud_fee.Tuti_14_Paid,
        'fee15':fee_str.Volu_15-stud_fee.Volu_15_Paid,
        
    }

    return render(request, 'entry/updatestudfee.html',{'stud_ad':stud_ad,'fee_str':fee_str,'stud_pd':stud_pd,'stud_fee':stud_fee,'fee':fee})


@login_required(login_url="/accounts/login/")
def delete_stud_pd(request,usn):
    stud_pd=Stud_PD.objects.get(USN=usn)
    if request.method=="POST":
        stud_pd.delete()
        return redirect('details:list')
    else:
        return render(request,'entry/deletestudpd.html',{'stud_pd':stud_pd})
