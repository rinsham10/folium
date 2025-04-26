from django.shortcuts import render, redirect
def home(request):
    return render(request, 'index.html')
def template_selection(request):
    return render(request, 'template_selection.html')
from django.shortcuts import render, redirect

def build_portfolio(request):
    if request.method == "POST":
        selected_template = request.POST.get('template')
        request.session['selected_template'] = selected_template
        return render(request, 'form_page.html', {'template': selected_template})
    return redirect('select_template')
from django.shortcuts import render

def submit_portfolio(request):
    if request.method == "POST":
        # Collect basic details (name is required, others are optional)
        name = request.POST.get('name', None)
        title = request.POST.get('title', None)
        bio = request.POST.get('bio', None)
        skills = request.POST.get('skills', None)
        github = request.POST.get('github', None)
        linkedin = request.POST.get('linkedin', None)

        # Collect multiple project data (optional)
        project_titles = request.POST.getlist('project_title[]')
        project_descs = request.POST.getlist('project_desc[]')
        project_stacks = request.POST.getlist('project_stack[]')
        project_links = request.POST.getlist('project_link[]')

        # Collect multiple experience data (optional)
        experience = []
        job_titles = request.POST.getlist('job_title[]')
        company_names = request.POST.getlist('company_name[]')
        job_descs = request.POST.getlist('job_desc[]')
        durations = request.POST.getlist('duration[]')

        # Collect valid experience data (add to list if valid)
        for i in range(len(job_titles)):
            if job_titles[i] and company_names[i]:  # Only add if both job title and company name exist
                experience.append({
                    'job_title': job_titles[i],
                    'company_name': company_names[i],
                    'job_desc': job_descs[i],
                    'duration': durations[i]
                })

        # Collect multiple education data (optional)
        education = []
        degrees = request.POST.getlist('degree[]')
        schools = request.POST.getlist('school[]')
        edu_descs = request.POST.getlist('edu_desc[]')

        # Collect valid education data (add to list if valid)
        for i in range(len(degrees)):
            if degrees[i] and schools[i]:  # Only add if both degree and school name exist
                education.append({
                    'degree': degrees[i],
                    'school': schools[i],
                    'edu_desc': edu_descs[i]
                })

        # Split skills into a list (optional)
        skills_list = skills.split(',') if skills else []

        # Handle multiple project data (optional)
        project_data = []
        for i in range(len(project_titles)):
            if project_titles[i] and project_descs[i]:  # Only add valid project data
                project_data.append({
                    'title': project_titles[i],
                    'description': project_descs[i],
                    'stack': project_stacks[i],
                    'link': project_links[i]
                })

         # Get the selected template from session
        selected_template = request.session.get('selected_template', 'template1')  # Default to template1 if not selected

        # Pass the collected data and the selected template to the respective template
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
                'linkedin': linkedin
            })
        # Add more templates as required (template2, template3, etc.)
        # elif selected_template == 'template2':
        #     return render(request, 'template2.html', {...})


        
def template1_view(request):
    # Add any context data you want to pass to the template
    context = {
        'name': 'John Doe',  # Example data
        'bio': 'I am a passionate developer',  # Example bio
        'skills': ['Python', 'Django', 'JavaScript'],  # Example skills
        'project_data': [{'title': 'Project 1', 'description': 'Description of Project 1', 'link': 'https://example.com'}],  # Example project
        'github': 'https://github.com/johndoe',  # Example GitHub link
        'linkedin': 'https://linkedin.com/in/johndoe'  # Example LinkedIn link
    }
    return render(request, 'template1.html', context)
    return redirect('select_template')