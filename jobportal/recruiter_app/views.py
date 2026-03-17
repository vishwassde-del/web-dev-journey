from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Recruiter, RecruiterDetail, JobDetail, JobApplied
from django.views.decorators.cache import never_cache


@never_cache
def home(request):
  return render(request,"./recruiter_app/home.html")

@never_cache
def recruiter_signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')

        Recruiter.objects.create(
            username=username,
            name=name,
            email=email,
            phone=phone,
            password=password
        )
        return redirect('recruiter_login')
    else:
            return render(request, 'recruiter_app/signup.html')

@never_cache
def recruiter_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=Recruiter.objects.filter(username=username, password=password).first()
        if user:
            request.session['recruiter_id']=user.id
            request.session['recruiter_name']=user.username
            request.session['recruiter_email']=user.email
            request.session['recruiter_phone']=user.phone
            return redirect('recruiter_dashboard')
        else:
            return HttpResponse("invalid credentials")
    else:
            return render(request, 'recruiter_app/login.html')
    
@never_cache  
def recruiter_dashboard(request):
    if 'recruiter_id' not in request.session:
        return redirect('recruiter_login')
    username = request.session.get('recruiter_name')
    return render(request, 'recruiter_app/dashboard.html', {'username': username})

@never_cache
def recruiter_profile(request):
    if 'recruiter_id' not in request.session:
        return redirect('recruiter_login')
    userid=request.session.get('recruiter_id')
    name=request.session.get('recruiter_name')
    email=request.session.get('recruiter_email')
    user=RecruiterDetail.objects.filter(user_id=userid).first()

    if user:
        bio=user.bio
        address=user.address
        profile_pic=user.profile_pic
    else:
        bio=""
        address=""
        profile_pic=""
    context={'name': name, 'email': email, 'bio': bio, 'address': address, 'profile_pic': profile_pic}
    return render(request, 'recruiter_app/profile.html', context)

@never_cache
def recruiter_profile_update(request):
    if 'recruiter_id' not in request.session:
        return redirect('recruiter_login')
    if request.method == 'POST':
        bio=request.POST.get('bio')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        image=request.FILES.get('image')

        id=request.session.get('recruiter_id')
        recruiter_id=Recruiter.objects.filter(id=id).first()
        RecruiterDetail.objects.update_or_create(
            user=recruiter_id,
            defaults={
                'bio': bio,
                'address': address,
                'city': city,
                'state': state,
                'profile_pic': image
            }
        )
        return redirect('recruiter_profile')
    else:
            return render(request, 'recruiter_app/profile_update.html')

@never_cache
def job_details(request):
    if 'recruiter_id' not in request.session:
        return redirect('recruiter_login')
    id=request.session.get('recruiter_id')
    recruiter=Recruiter.objects.filter(id=id).first()
    if request.method == 'POST':
        company_name=request.POST.get('company_name')#
        company_address=request.POST.get('company_address')#
        company_image=request.FILES.get('company_image')#
        job_role=request.POST.get('job_role')#
        job_description=request.POST.get('job_description')#
        skills=request.POST.get('skills_required')#
        salary=request.POST.get('salary_range')#
        experinece_required=request.POST.get('experinece_required')#
        qualification=request.POST.get('qualification')#
        vacancy=request.POST.get('vacancy')#
        employment_type=request.POST.get('employment_type')#
        job_location=request.POST.get('job_location')#
        industry=request.POST.get('industry_type')#
        job_posted=request.POST.get('job_posted')#
        last_date=request.POST.get('last_date')#
        hiring_process=request.POST.get('hiring_process')#

        JobDetail.objects.create(
            recruiter=recruiter,
            company_name=company_name,
            company_address=company_address,
            company_image=company_image,
            job_role=job_role,
            job_description=job_description,
            skills_required=skills,
            salary_range=salary,
            experinece_required=experinece_required,
            qualification=qualification,
            vacancy=vacancy,
            job_location=job_location,
            employment_type=employment_type,
            industry_type=industry,
            job_posted_on=job_posted,
            last_date_to_apply=last_date,
            hiring_process=hiring_process
        )
        return redirect('recruiter_dashboard')
    else:
            return render(request, 'recruiter_app/job_detail.html')


    # id=request.session.get('recruiter_id')
    # recruiter=Recruiter.objects.filter(id=id).first()
# @never_cache
# def applied_job(request):
#     if 'recruiter_id' not in request.session:
#         return redirect('recruiter_login')
#     id = request.session.get('recruiter_id')
#     jobs = JobApplied.objects.filter(id=id)
#     return render(request, 'recruiter_app/applied_job.html', {'jobs': jobs})
@never_cache
def applied_job(request):
    if "recruiter_id" not in request.session:
        return redirect("recruiter_login")

    recruiter_id = request.session["recruiter_id"]

    jobs = JobApplied.objects.filter(
        job_detail__recruiter_id=recruiter_id,
        scheduled=False
    )

    return render(
        request,
        "recruiter_app/applied_job.html",
        {"jobs": jobs}
    )


# @never_cache
# def approve(request, id):
#     if 'recruiter_id' not in request.session:
#         return redirect('recruiter_login')
#     job=get_object_or_404(JobApplied,id=id)
#     job.scheduled=True
#     job.save()
#     return redirect("recruiter_dashboard")

@never_cache
def approve(request, id):
    if 'recruiter_id' not in request.session:
        return redirect('recruiter_login')

    job = get_object_or_404(JobApplied, id=id)
    job.scheduled = True
    job.save()

    return redirect('applied_job')

@never_cache
def recruiter_logout(request):
    request.session.flush()
    return redirect('recruiter_login')

