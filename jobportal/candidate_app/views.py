from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Candidate, CandidateDetail
from recruiter_app.models import Recruiter, JobDetail, JobApplied
from django.views.decorators.cache import never_cache

@never_cache
def candidate_signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')

        Candidate.objects.create(
            username=username,
            name=name,
            email=email,
            phone=phone,
            password=password
        )
        return redirect('candidate_login')
    else:
        return render(request, './candidate_app/signup.html')

@never_cache
def candidate_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=Candidate.objects.filter(username=username, password=password).first()
        if user:
            request.session['candidate_id']=user.id
            request.session['candidate_name']=user.username
            request.session['candidate_email']=user.email
            request.session['candidate_phone']=user.phone
            return redirect('candidate_dashboard')
        else:
            return HttpResponse("Invalid credentials")
    else:
        return render(request, './candidate_app/login.html')

@never_cache
def candidate_dashboard(request):
    if 'candidate_id' not in request.session:
        return redirect('candidate_login')
    username = request.session.get('candidate_name')
    jobs = JobDetail.objects.all()
    return render(request, './candidate_app/dashboard.html', {'username': username, 'jobs': jobs})

@never_cache
def candidate_profile(request):
    if 'candidate_id' not in request.session:
        return redirect('candidate_login')
    userid=request.session.get('candidate_id')
    name=request.session.get('candidate_name')
    email=request.session.get('candidate_email')
    user=CandidateDetail.objects.filter(user_id=userid).first()

    if user:
        bio=user.bio
        address=user.address
        profile_pic=user.profile_pic
    else:
        bio=""
        address=""
        profile_pic=""
    context={'name': name, 'email': email, 'bio': bio, 'address': address, 'profile_pic': profile_pic}
    return render(request, './candidate_app/profile.html', context)

@never_cache
def candidate_profile_update(request):
    if 'candidate_id' not in request.session:
        return redirect('candidate_login')
    if request.method == 'POST':
        bio=request.POST.get('bio')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        image=request.FILES.get('image')

        id=request.session.get('candidate_id')
        candidate_id=Candidate.objects.filter(id=id).first()
        CandidateDetail.objects.update_or_create(
            user=candidate_id,
            defaults={
                'bio': bio,
                'address': address,
                'city': city,
                'state': state,
                'profile_pic': image
            }
        )
        return redirect('candidate_profile')
    else:
        return render(request, './candidate_app/profile_update.html')
    
@never_cache
def view_detail(request, id):
    if 'candidate_id' not in request.session:
        return redirect('candidate_login')
    job = JobDetail.objects.filter(id=id).first()
    return render(request, './candidate_app/view_detail.html', {'job': job})

@never_cache
def apply_job(request, id):
    if 'candidate_id' not in request.session:
        return redirect('candidate_login')
    candidate_id=request.session.get('candidate_id')
    candidate=Candidate.objects.filter(id=candidate_id).first()
    job=JobDetail.objects.filter(id=id).first()
    recruiter_id=job.recruiter.id
    recruiter=Recruiter.objects.filter(id=recruiter_id).first()

    JobApplied.objects.create(
        job_detail=job,
        recruiter=recruiter,
        candidate=candidate,
        scheduled=False
    )
    return redirect('candidate_dashboard')

@never_cache
def scheduled(request):
    if 'candidate_id' not in request.session:
        return redirect('candidate_login')
    user_id=request.session.get('candidate_id')
    user=JobApplied.objects.filter(candidate=user_id)
    return render(request, './candidate_app/result.html', {'user': user})

@never_cache
def candidate_logout(request):
    request.session.flush()
    return redirect('candidate_login')