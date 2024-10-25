from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate
from datetime import date,datetime
from django.db.models import Q
# Create your views here.
def index(request):
    if request.POST:
        a_no=request.POST['aadhar']
        # print(a_no,'a_no,,,,,,,,,,,')
        return redirect('/guest-view-criminal?aadhar_data='+a_no)
    return render(request,'index.html')
def guest_view_criminal(request):
    data=request.GET['aadhar_data']
    # print(data,'data,,,,,,,,,,,,')
    criminal=Prisoner.objects.filter(Q(aadhar__contains=data))
    return render(request,'guest_view_criminal.html',{"criminal":criminal})
def users_login(request):
    if request.POST:
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user is not None:
            if user.user_type=='admin':
                msg='Welcome to admin dashboard'
                messages.info(request,msg)
                return redirect('/admin-dashboard',{"message":messages.get_messages(request)})
            elif user.user_type=='police':
                request.session['pid']=user.id
                msg='Welcome to police dashboard'
                messages.info(request,msg)
                return redirect('/police_dashboard')
            elif user.user_type=='jailor':
                request.session['jid']=user.id
                msg='Welcome to jailor dashboard'
                messages.info(request,msg)
                return redirect('/jailor-dashboard',{"message":messages.get_messages(request)})
            else:
                pass
        else:
            pass
    return render(request,'users-login.html')
#admin
def admin_dashboard(request):
    return render(request,'admin/admin_dashboard.html')
def admin_approve_police(request):
    police_list=PoliceReg.objects.filter(policelog__is_active=0,p_status='Pending')
    # print(police_list,'policelist###')
    return render(request,'admin/admin_approve_police.html',{"polices":police_list})
def admin_approve_allpolice(request):
    today=date.today()
    police_status=PoliceReg.objects.filter(p_status='Pending').update(p_status="Approved",doj=str(today))
    police_log=Login.objects.filter(is_active=0,user_type="police").update(is_active=1)
    return redirect('/admin-approve_police')
def admin_approve_singlepolice(request):
    today=date.today()
    pid=request.GET.get('pid')
    police=PoliceReg.objects.get(id=pid)
    plog=police.policelog.id
    policereg=PoliceReg.objects.filter(id=pid).update(p_status="Approved",doj=str(today))
    policelog=Login.objects.filter(id=plog).update(is_active=1)

    # print('police.policelog_______________')
    return redirect("/admin-approve_police")
def admin_reject_singlepolice(request):
    pid=request.GET.get('pid')
    police=PoliceReg.objects.get(id=pid)
    plog=police.policelog.id
    policereg=PoliceReg.objects.filter(id=pid).delete()
    policelog=Login.objects.filter(id=plog).delete()

    return redirect('/admin-approve_police')
def admin_view_police(request):
    police_list=PoliceReg.objects.filter(policelog__is_active=1)
    return render(request,'admin/admin_view_police.html',{"polices":police_list})

def admin_view_jailor(request):
    jailor=Login.objects.get(user_type='jailor')
    return render(request,'admin/admin_view_jailor.html',{'jailor':jailor})
def admin_view_criminals(request):
    prisoners=Prisoner.objects.all()
    if request.POST:
        filter_date=request.POST['date']
        # print(filter_date,'filter_date,,,,,,,,,,,,')
        year=filter_date.split('-')[0]
        month=filter_date.split('-')[1]
        # print(year,month,'monthsplitted,,,,,,,,,,,,')
        format=year+"-"+month+'-'
        prisoners=Prisoner.objects.filter(Q(from_date__contains=format))
        return render(request,'admin/admin_view_criminals.html',{'prisoners':prisoners})
    return render(request,'admin/admin_view_criminals.html',{'prisoners':prisoners})
def admin_view_prisoner_detailed(request):
    id=request.GET['prisoner_id']
    prisoner=Prisoner.objects.get(id=id)
    duties=Duty.objects.filter(prison_id=id)
    remarks=Remarks.objects.filter(prison_id=id)
    if request.POST:
            filterdate = request.POST["filterdate"]
            if filterdate:
                duties=Duty.objects.filter(Q(prison__id=id) & Q(created_date = filterdate))    
    return render(request,'admin/admin_view_prisoner_detailed.html',{"prisoner":prisoner,"duties":duties,"remarks":remarks})
def admin_view_police_duty(request):
    id=request.GET.get('id')
    duties=Duty.objects.filter(police_id=id)
    if request.POST:
        filterdate = request.POST["filterdate"]
        if filterdate:
            duties=Duty.objects.filter(Q(police_id=id) & Q(created_date = filterdate))             
    return render(request,'admin/admin_view_police_duty.html',{"duties":duties})
def admin_visitor_list(request):
    visitors=Visitor.objects.all()
    if request.POST:
            filterdate = request.POST["filterdate"]
            if filterdate:
                visitors=Visitor.objects.filter(created_date = filterdate)
    return render(request,'admin/admin_visitor_list.html',{'visitors':visitors})
#jailor
def jailor_dashboard(request):
    return render(request,'jailor/jailor_dashboard.html')
def jailor_add_prisoner(request):
    crimes_str=''
    if request.POST:
        first=request.POST['fname']
        last=request.POST['lname']
        address=request.POST['address']
        phone=request.POST['phone']
        aadhar=request.POST['aadhar']
        image=request.FILES['pimage']
        crimes=request.POST.getlist('Crimes')
        # print(crimes,'@@@@@@@@@@@@@')
        crimes_str=', '.join(crimes)
        # print(crimes_str)
        prisoner=Prisoner.objects.create(fname=first,
                                         lname=last,
                                         address=address,
                                         phone = phone,
                                         aadhar=aadhar,
                                         crimes=crimes_str,
                                         prisoner_image=image)
        prisoner.save()
        messages.success(request,'Prisoner Added Successfully')
        return redirect('/jailor-add-prisoner')
    return render(request,'jailor/jailor_add_prisoner.html')
def jailor_view_prisoners(request):
    prisoners=Prisoner.objects.all()
    if request.POST:
        filter_date=request.POST['date']
        # print(filter_date,'filter_date,,,,,,,,,,,,')
        year=filter_date.split('-')[0]
        month=filter_date.split('-')[1]
        # print(year,month,'monthsplitted,,,,,,,,,,,,')
        format=year+"-"+month+'-'
        prisoners=Prisoner.objects.filter(Q(from_date__contains=format))
        return render(request,'jailor/jailor_view_prisoners.html',{'prisoners':prisoners})
    return render(request,'jailor/jailor_view_prisoners.html',{'prisoners':prisoners})

def jailor_view_prisoner_detailed(request):
    id=request.GET['prisoner_id']
    prisoner=Prisoner.objects.get(id=id)
    duties=Duty.objects.filter(prison_id=id)
    remarks=Remarks.objects.filter(prison_id=id)
    if request.POST:
            filterdate = request.POST["filterdate"]
            if filterdate:
                remarks=Remarks.objects.filter(Q(prison__id=id) & Q(created_date = filterdate))
    return render(request,'jailor/jailor_view_prisoner_detailed.html',{"prisoner":prisoner,"duties":duties,"remarks":remarks})
def jailor_edit_prisoner_detailed(request):
    id=request.GET.get('prisoner_id')
    prisoners=Prisoner.objects.filter(id=id)
    if prisoners.exists():
        clist = prisoners[0].crimes
        print(clist,'clist exist')
    crimes_str=''
    new_crimes=[]
    if request.POST:
        prisoner=Prisoner.objects.get(id=id)
        prisoner.fname=request.POST['fname']
        prisoner.lname=request.POST['lname']
        prisoner.address=request.POST['address']
        prisoner.phone=request.POST['phone']
        prisoner.aadhar=request.POST['aadhar']
        if request.POST.getlist('Crimes'):
            crimes=request.POST.getlist('Crimes')
        else:
            crimes=request.POST.getlist('Crimes_prev')
        for crime in crimes:
            # if crime not in prisoners[0].crimes:
            if crime not in clist:
                new_crimes.append(crime)
                
        crimes_str=', '.join(new_crimes)
        crimes_str=crimes_str+", "+clist.lstrip(', ')
        prisoner.crimes=crimes_str
        if 'pimage' in request.FILES:
            # print('yess here#########')
            prisoner.prisoner_image=request.FILES['pimage']
        else:
            prisoner.prisoner_image=prisoners[0].prisoner_image#if get just prisoners.prisoner_image
        prisoner.save()
        messages.success(request,'Prisoner Updated Successfully')
        return redirect('/jailor-view-prisoners')
    return render(request,'jailor/jailor_edit_prisoner_detailed.html',{"prisoners":prisoners})

def jailor_delete_prisoner_detailed(request):
    id=request.GET.get('prisoner_id')
    # print(id,'id,,,,,,,,,,')
    prisoner=Prisoner.objects.filter(id=id).update(status='Released')
    # print(prisoner,'prisoner,,,,,,,,,,,')
    return redirect('/jailor-view-prisoners')
def jailor_add_duty(request):
    jid=request.session['jid']
    id=request.GET.get('pid')
    type=request.GET.get('type')
    print("ON")
    if request.POST:
        dutyname=request.POST['duty']
        dutyenddate = request.POST['dutyenddate']
        dutystartdate = request.POST['dutystartdate']
        print("Jailor=",jid,"Prisoner=",id,"Type=",type,'duty=',dutyname,'!!!!!!!!!!!!!!IF1')
        if type == 'prisoner':
            print("Jailor=",jid,"Prisoner=",id,"Type=",type,'duty=',dutyname,'!!!!!!!!!!!!!!IF2')
            prisoner_obj=Prisoner.objects.get(id=id)
            prison_duty=Duty.objects.create(duty_name=dutyname,
                                            prison_id=id,
                                            jailor_id=jid,
                                            dutyenddate = dutyenddate,
                                            dutystartdate = dutystartdate)
            prison_duty.save()
            return redirect('/jailor-view-prisoners')
        elif type == 'police':
            print("Jailor=",jid,"Prisoner=",id,"Type=",type,'dutyenddate=',dutyenddate,'dutystartdate=',dutystartdate,'duty=',dutyname,'!!!!!!!!!!!!!!IF3')
            police_obj=PoliceReg.objects.get(id=id)
            police_duty=Duty.objects.create(duty_name=dutyname,
                                            police_id=id,
                                            jailor_id=jid,
                                            dutyenddate = dutyenddate,
                                            dutystartdate = dutystartdate)
            police_duty.save()
            return redirect('/jailor-view-polices')
    if type == "police":
        previousdutys = Duty.objects.filter(police__id = id)
    else:
        previousdutys = Duty.objects.filter(prison__id = id)
    return render(request,'jailor/jailor_add_duty.html',{"type":type,"previousdutys":previousdutys})
def jailor_delete_duty(request):
    
    duty_id=request.GET.get('id')
    duty=Duty.objects.filter(id=duty_id).delete()
    if request.GET.get('prisoner_id'):
        p_id=request.GET.get('prisoner_id')
        return redirect('/jailor_view_prisoner_detailed?prisoner_id='+p_id)
    else:
        return redirect('/jailor-view-police-duty')
def jailor_view_polices(request):
    police_list=PoliceReg.objects.filter(policelog__is_active=1)
    return render(request,'jailor/jailor_view_polices.html',{"polices":police_list})
def jailor_view_police_duty(request):
    id=request.GET.get('id')
    duties=Duty.objects.filter(police_id=id)
    return render(request,'jailor/jailor_view_police_duty.html',{"duties":duties})

def jailor_deletesinglepolice(request):
    pid=request.GET.get('pid')
    police=PoliceReg.objects.get(id=pid)
    plog=police.policelog.id
    policereg=PoliceReg.objects.filter(id=pid).delete()
    policelog=Login.objects.filter(id=plog).delete()
    return redirect('/jailor-view-polices')
def jailor_view_parole_list(request):
    paroles=Parole.objects.filter(status='Pending')
    return render(request,'jailor/jailor_view_parole_list.html',{'paroles':paroles})
def jailor_view_visitors(request):
    visitors=Visitor.objects.all()
    return render(request,'jailor/jailor_view_visitors.html',{'visitors':visitors})
def jailor_accept_parole(request):
    paroleid=request.GET.get('id')
    pstatus=Parole.objects.filter(id=paroleid).update(status="Accepted")
    return redirect('/jailor-view-parole_list')
def jailor_reject_parole(request):
    paroleid=request.GET.get('id')
    pstatus=Parole.objects.filter(id=paroleid).update(status="Rejected")
    return redirect('/jailor-view-parole_list')
#police
def calculate_age(born):
    today = date.today()
    born = datetime.strptime(born, '%Y-%m-%d').date()  # Convert birth date string to datetime.date object

    try: 
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year
def police_register(request):
    if request.POST:
        fname=request.POST['name']
        email=request.POST['email']
        pwd=request.POST['password']
        phone=request.POST['phone']
        degree=request.POST['degree']
        rank=request.POST['rank']
        birth=request.POST['dob']
        address=request.POST['address']
        pimage=request.FILES['pimage']
        if Login.objects.filter(username=email,view_password=pwd).exists():
            message='Already exists'
            messages.info(request,message)
            return redirect('/users-login')
        else:
            age=calculate_age(birth)
            # print(age,'###')
            plog=Login.objects.create_user(username=email,view_password=pwd,user_type='police',password=pwd,is_active=0)
            plog.save()
            preg=PoliceReg.objects.create(p_age=age,policelog=plog,name=fname,phone=phone,degree=degree,rank=rank,dob=birth,address=address,police_image=pimage)
            preg.save()
            # print(preg,'@@@@@@@@@@@@@@@@@@@')
            messages.info(request, 'Registration completed; Please wait for approval')
            return render(request, 'jailor/police_register.html', {'messages': messages.get_messages(request)})
    return render(request,'jailor/police_register.html')
def police_dashboard(request):
    message = messages.get_messages(request)
    return render(request,'police/police_dashboard.html',{"message":message})
def police_view_profile(request):
    print("Inside fn")
    policeid=request.session['pid']
    print(policeid,'policeid############')
    police=PoliceReg.objects.get(policelog_id=policeid)
    print(police,'POLICE###############')
    return render(request,'police/police_view_profile.html',{"police":police})
def police_updateprofile(request):
    policeid=request.session['pid']
    print(policeid,'policeid############')
    police=PoliceReg.objects.get(policelog_id=policeid)
    if request.POST:
        pobj=PoliceReg.objects.get(policelog_id=policeid)
        pobj.name=request.POST['name']
        pobj.phone=request.POST['phone']
        if 'pimage' in request.FILES:
            pobj.police_image = request.FILES['pimage']
        else:
            pobj.police_image = police.police_image
        pobj.address=request.POST['address']
        pobj.save()
        return redirect('/police-view-profile')
    return render(request,'police/police_updateprofile.html',{"police":police})
def police_view_prisoners(request):
    prisoners=Prisoner.objects.filter(status='Active')
    print(prisoners)
    return render(request,'police/police_view_prisoners.html',{"prisoners":prisoners})
def police_view_prisoner_detailed(request):
    id=request.GET['prisoner_id']
    prisoner=Prisoner.objects.get(id=id)
    duties=Duty.objects.filter(prison_id=id)
    remarks=Remarks.objects.filter(prison_id=id)
    return render(request,'police/police_view_prisoner_detailed.html',{"prisoner":prisoner,"duties":duties,"remarks":remarks})
def police_add_remarks(request):
    prisoner=request.GET.get('prisoner_id')
    police=request.session['pid']
    pobj=PoliceReg.objects.get(policelog_id=police)
    if request.POST:      
        action=request.POST['action']
        remarks=request.POST['remarks']
        rating=request.POST['rating']
        print(prisoner,pobj,action,remarks,'##################@')
        remark=Remarks.objects.create(prison_id=prisoner,
                                      police=pobj,
                                      action=action,
                                      remarks=remarks,
                                      rating = rating)
        remark.save()
        return redirect('/police-view-prisoners')
    return render(request,'police/police_add_remarks.html')
def police_request_parole(request):
    prisoner=request.GET.get('prisoner_id')
    police=request.session['pid']
    pobj=PoliceReg.objects.get(policelog_id=police)
    if request.POST:
        fdate=request.POST['fdate']
        tdate=request.POST['tdate']
        reason=request.POST['reason']
        parole=Parole.objects.create(prison_id=prisoner,police=pobj,from_date=fdate,to_date=tdate,reason=reason)
        parole.save()
        return redirect('/police-view-prisoners')
    return render(request,'police/police_request_parole.html')
def police_view_parole_status(request):
    paroles=Parole.objects.filter(status__in=['Accepted','Rejected'])
    if request.POST:
            filterdate = request.POST["filterdate"]
            if filterdate:
                paroles=Parole.objects.filter(Q(status__in=['Accepted','Rejected']) & Q(created_date = filterdate)) 
    return render(request,'police/police_view_parole_status.html',{'paroles':paroles})
def police_view_duties(request):
    police=request.session['pid']
    pobj=PoliceReg.objects.get(policelog_id=police)
    duties=Duty.objects.filter(police=pobj)
    return render(request,'police/police_view_duties.html',{"duties":duties})
def police_visitors_list(request):
    prisoners=Prisoner.objects.filter(status='Active')
    police=request.session['pid']
    pobj=PoliceReg.objects.get(policelog_id=police)
    if request.POST:
        prisoner=request.POST['prisoner']
        visitor_name=request.POST['visitor']
        relation = request.POST['relation']
        visitor_phone=request.POST['contact']
        visitor_alloted_time=request.POST['visitor_alloted_time']
        visitorimage = request.FILES['visitorimage']
        visitor=Visitor.objects.create(prison_id=prisoner,
                                       police=pobj,
                                       visitor_name=visitor_name,
                                       visitor_relation = relation,
                                       visitor_phone=visitor_phone,
                                       visitor_image = visitorimage,
                                       visitor_alloted_time = visitor_alloted_time)
        visitor.save()
        return redirect('/police_visitors_list')
    visitors=Visitor.objects.all()
    return render(request,'police/police_visitors_list.html',{"prisoners":prisoners,'visitors':visitors})
