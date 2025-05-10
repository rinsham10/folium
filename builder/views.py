from django.shortcuts import render, redirect, get_object_or_404
from .models import Portfolio, Project, Experience, Education

def home(request):
    return render(request, 'index.html')

def template_selection(request):
    return render(request, 'template_selection.html')

def build_portfolio(request):
    if request.method == "POST":
        selected_template = request.POST.get('template')
        request.session['selected_template'] = selected_template
        return render(request, 'form_page.html', {'template': selected_template})
    return redirect('select_template')

def submit_portfolio(request):
    if request.method == "POST":
        name = request.POST.get('name')
        title = request.POST.get('title', None)
        bio = request.POST.get('bio')
        skills = request.POST.get('skills', '')
        github = request.POST.get('github')
        linkedin = request.POST.get('linkedin')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

         # Get selected template from session
        selected_template = request.session.get('selected_template', 'template1')

        # Create Portfolio
        portfolio = Portfolio.objects.create(
            name=name,
            title=title,
            bio=bio,
            skills=skills,
            github=github,
            linkedin=linkedin,
            email=email,
            phone=phone
        )

        # Projects
        titles = request.POST.getlist('project_title[]')
        project_durations = request.POST.getlist('project_duration[]')
        descs = request.POST.getlist('project_desc[]')
        stacks = request.POST.getlist('project_stack[]')
        links = request.POST.getlist('project_link[]')
        gits = request.POST.getlist('project_github[]')

        for i in range(len(titles)):
            if titles[i]:
                Project.objects.create(
                    portfolio=portfolio,
                    title=titles[i],
                    project_duration=project_durations[i],
                    description=descs[i] if i < len(descs) else '',
                    stack=stacks[i] if i < len(stacks) else '',
                    link=links[i] if i < len(links) else '',
                    github=gits[i] if i < len(gits) else ''
                )

        # Experience
        job_titles = request.POST.getlist('job_title[]')
        companies = request.POST.getlist('company_name[]')
        job_descs = request.POST.getlist('job_desc[]')
        durations = request.POST.getlist('duration[]')
        locations = request.POST.getlist('location[]')

        for i in range(len(job_titles)):
            if job_titles[i] and companies[i]:
                Experience.objects.create(
                    portfolio=portfolio,
                    job_title=job_titles[i],
                    company_name=companies[i],
                    job_desc=job_descs[i],
                    duration=durations[i],
                    location=locations[i]
                )

        # Education
        degrees = request.POST.getlist('degree[]')
        schools = request.POST.getlist('school[]')
        edu_descs = request.POST.getlist('edu_desc[]')
        edu_locs = request.POST.getlist('edu_location[]')
        edu_durations = request.POST.getlist('edu_duration[]')

        for i in range(len(degrees)):
            if degrees[i] and schools[i]:
                Education.objects.create(
                    portfolio=portfolio,
                    degree=degrees[i],
                    school=schools[i],
                    edu_desc=edu_descs[i],
                    edu_location=edu_locs[i],
                    edu_duration=edu_durations[i]
                )

        # Redirect to the correct template view based on selection
        if selected_template == 'template2':
            return redirect('view_template2', slug=portfolio.slug)
        else:
            return redirect('view_portfolio', slug=portfolio.slug)

    return redirect('home')

def view_portfolio(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)

    # Check if project links are absolute URLs
    project_data = []
    for project in portfolio.projects.all():
        project_data.append({
            'title': project.title,
            'description': project.description,
            'duration': project.project_duration,
            'stack': project.stack,
            'link': project.link if project.link.startswith('http') else 'https://rinsham10.github.io/AgriSens/',
            'github': project.github if project.github.startswith('http') else ''
        })

    return render(request, 'template1.html', {
        'name': portfolio.name,
        'title': portfolio.title,
        'bio': portfolio.bio,
        'skills': [s.strip() for s in portfolio.skills.split(',')],
        'github': portfolio.github,
        'linkedin': portfolio.linkedin,
        'email': portfolio.email,
        'phone': portfolio.phone,
        'project_data': project_data,  # Adjusted to ensure full URL
        'experience': portfolio.experiences.all(),
        'education': portfolio.educations.all(),
    })

def view_template2(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)

    project_data = []
    for project in portfolio.projects.all():
        project_data.append({
            'title': project.title,
            'description': project.description,
            'duration': project.project_duration,
            'stack': project.stack,
            'link': project.link if project.link.startswith('http') else '',
            'github': project.github if project.github.startswith('http') else ''
        })

    return render(request, 'template2.html', {
        'name': portfolio.name,
        'title': portfolio.title,
        'bio': portfolio.bio,
        'skills': [s.strip() for s in portfolio.skills.split(',')],
        'github': portfolio.github,
        'linkedin': portfolio.linkedin,
        'email': portfolio.email,
        'phone': portfolio.phone,
        'project_data': project_data,
        'experience': portfolio.experiences.all(),
        'education': portfolio.educations.all(),
    })


