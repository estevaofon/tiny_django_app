from django.shortcuts import render
from django.http import HttpResponse
from coffee.models import Post
from coffee.forms import PostForm


def index(request):
    posts = Post.objects.all()
    context_dict = {'posts': posts}

    return render(request, 'coffee/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "Site made by Estevao using Django"}
    return render(request, 'coffee/about.html', context=context_dict)

def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            post = form.save(commit=True)
            print(post, post.body)
            # Now that the category is saved
            # We could give a confirmation message
            # But instead since the most recent catergory added is on the index page
            # Then we can direct the user back to the index page.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print(form.errors)
    # Will handle the bad form (or form details), new form or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'coffee/add_post.html', {'form': form})

