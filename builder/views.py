from django.shortcuts import render, redirect

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
        # Collect basic details
        name = request.POST.get('name', None)
        title = request.POST.get('title', None)
        bio = request.POST.get('bio', None)
        skills = request.POST.get('skills', None)
        github = request.POST.get('github', None)
        linkedin = request.POST.get('linkedin', None)
        email = request.POST.get('email', None)  # <-- added
        phone = request.POST.get('phone', None)  # <-- added

        # Collect multiple project data
        project_titles = request.POST.getlist('project_title[]')
        project_descs = request.POST.getlist('project_desc[]')
        project_stacks = request.POST.getlist('project_stack[]')
        project_links = request.POST.getlist('project_link[]')
        project_githubs = request.POST.getlist('project_github[]')

        # Collect multiple experience data
        experience = []
        job_titles = request.POST.getlist('job_title[]')
        company_names = request.POST.getlist('company_name[]')
        job_descs = request.POST.getlist('job_desc[]')
        durations = request.POST.getlist('duration[]')
        locations = request.POST.getlist('location[]')

        for i in range(len(job_titles)):
            if job_titles[i] and company_names[i]:
                experience.append({
                    'job_title': job_titles[i],
                    'company_name': company_names[i],
                    'job_desc': job_descs[i],
                    'duration': durations[i],
                    'location': locations[i]
                })

        # Collect multiple education data
        education = []
        degrees = request.POST.getlist('degree[]')
        schools = request.POST.getlist('school[]')
        edu_descs = request.POST.getlist('edu_desc[]')
        edu_location = request.POST.getlist('edu_location[]')
        edu_duration = request.POST.getlist('edu_duration[]')
        for i in range(len(degrees)):
            if degrees[i] and schools[i]:
                education.append({
                    'degree': degrees[i],
                    'school': schools[i],
                    'edu_desc': edu_descs[i],
                    'edu_location': edu_location[i],
                    'edu_duration': edu_duration[i]
                })

        # Handle skills list
        skills_list = skills.split(',') if skills else []

        # Handle project data
        project_data = []
        for i in range(len(project_titles)):
            if project_titles[i] and project_descs[i]:
                project_data.append({
                    'title': project_titles[i],
                    'description': project_descs[i],
                    'stack': project_stacks[i],
                    'link': project_links[i],
                    'github': project_githubs[i] if i < len(project_githubs) else ''
                })

        # Get selected template
        selected_template = request.session.get('selected_template', 'template1')

        if selected_template == 'template1':
            return render(request, 'template1.html', {
                'name': name,
                'title': title,
                'bio': bio,
                'skills': skills_list,
                'project_data': project_data,
                'experience': experience,
                'education': education,
                'github': github,
                'linkedin': linkedin,
                'email': email,         # <-- pass email to template
                'phone': phone          # <-- pass phone to template
            })
    return redirect('home')

def template1_view(request):
    context = {
        'name': 'John Doe',
        'bio': 'I am a passionate developer',
        'skills': ['Python', 'Django', 'JavaScript'],
        'project_data': [{'title': 'Project 1', 'description': 'Description of Project 1', 'link': 'https://example.com'}],
        'github': 'https://github.com/johndoe',
        'linkedin': 'https://linkedin.com/in/johndoe',
        'email': 'johndoe@example.com',     # example data for email
        'phone': '+1234567890'               # example data for phone
    }
    return render(request, 'template1.html', context)
