from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewAuthorForm, NewEntryform, AddRelatedContentForm
from django.contrib.auth.models import User
from .models import NewEntry, AddRelatedContent
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

# List all current wiki entries and/or signup as a new Wiki Author
def home(request):
    form = NewAuthorForm(request.POST or None)
    allEntries = NewEntry.objects.all()
    if form.is_valid():
        print("user")
        User.objects.create_user(request.POST["username"], "", request.POST["password"])
        # form.save()
        return redirect('home')
    return render(request, 'big2App/index.html', {'form': form, 'allEntries': allEntries})

def search(request):
    results = NewEntry.objects.filter(Q(title__contains=request.POST['searchBar']) | Q(text__contains=request.POST['searchBar']))
    return render(request, 'big2/searchResults.html', {'all_entries': results})


# creates new wikki pots
def createEntry(request):
    userLogedIn = User.objects.get(username=request.user)
    form = NewEntryform(request.POST or None)
    # save form to database
    if form.is_valid():
        NewEntry.objects.create(title=request.POST['title'], text=request.POST['text'], dateCreated=request.POST['dateCreated'],
        lastUpdate=request.POST['lastUpdate'], authour=userLogedIn)
        return redirect('profile')
    return render(request, 'big2App/createEntry.html', {'form': form})
# allows you to add related content to the post
@login_required
def createRelated(request, id):
    originPost = get_object_or_404(NewEntry,pk=id)
    form = AddRelatedContentForm(request.POST or None)
    if form.is_valid():
        AddRelatedContent.objects.create(title=request.POST['title'], text=request.POST['text'], dateCreated=request.POST['dateCreated'],
                                lastUpdate=request.POST['lastUpdate'], parentPost=originPost)
        return redirect('profile')
    return render(request, 'big2App/createRelated.html', {'form': form, 'post': originPost})
# allows you to edit selected post
@login_required
def editPost(request, id):
    selectedEntry = NewEntry.objects.get(pk=id)
    form = NewEntryform(request.POST or None, instance= selectedEntry)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'big2App/editPost.html', {'form': form})

# allows you to edit the related content attached to the post
def editRealted(request, id):
    selectedEntry = NewEntry.objects.get(pk=id)
    form = AddRelatedContentForm(request.POST or None, request.FILES or None, instance=selectedEntry)
    if request.method == 'POST':
        form.save()
        return redirect('profile')

    return render(request, 'big2App/editRelated.html',{'form': form})

# allows you to delet post
def deletePost(request, id):
    selectedEntry = get_object_or_404(NewEntry, pk=id)

    if request.method == 'POST':
        selectedEntry.delete()
        return redirect('profile')
    return render(request, 'big2App/deletePost.html',{'selectedEntry': selectedEntry})

# allows you to delet the deleted content
def deleteRelated(request, id):
    selectedEntry = get_object_or_404(AddRelatedContent, pk=id)
    if request.method == 'POST':
        selectedEntry.delete()
        return redirect('profile')
    return render(request, 'big2App/deleteRelated.html', {'selectedEntry': selectedEntry})


# Get entries for the logged in User
@login_required
def get_logged_in_user_posts(request):
    print(request.user)
    urEntries = NewEntry.objects.filter(authour=request.user)
    print(urEntries)

    return render(request, 'big2App/profile.html', {'urEntries': urEntries})
# shows full text of the post along with related items attached to post
def entryDetails(request, id):
    selectedEntry = NewEntry.objects.get(pk= id)
    relatedContent = AddRelatedContent.objects.filter(parentPost=selectedEntry)
    return render(request, 'big2App/entryDetails.html', {'selectedEntry': selectedEntry,'relatedContent': relatedContent})

# loggin authentication
def login(request):
    return render(request, 'registration/login.html')
