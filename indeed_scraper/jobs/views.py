# indeed_scraper/jobs/views.py
from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    print(f"Number of jobs fetched: {jobs.count()}")
    for job in jobs:
        print(job.title, job.company, job.location, job.salary, job.description, job.url)
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

# Create your views here.
