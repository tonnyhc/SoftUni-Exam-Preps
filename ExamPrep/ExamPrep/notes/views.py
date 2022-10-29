from django.shortcuts import render, redirect

from ExamPrep.notes.forms import AddNoteForm, EditNoteForm, DeleteNoteForm, ProfileCreateForm
from ExamPrep.notes.models import Profile, Note


def get_profile():
    return Profile.objects.first()


def get_notes():
    return Note.objects.all()


def index(request):
    profile = get_profile()
    notes = get_notes()
    if not profile:
        return add_profile(request)
    context = {
        'notes': notes,
    }
    return render(request, 'common/home-with-profile.html', context)


def add_note(request):
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = AddNoteForm()
    context = {
        'form': form
    }
    return render(request, 'note/note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = EditNoteForm(instance=note)
    context = {
        'form': form,
    }
    return render(request, 'note/note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = DeleteNoteForm(instance=note)
    context = {
        'form': form
    }
    return render(request, 'note/note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note,
    }
    return render(request, 'note/note-details.html', context)


def add_profile(request):
    if request.method == "POST":
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    form = ProfileCreateForm()
    context = {
        'form': form
    }
    return render(request, 'common/home-no-profile.html', context)


def profile(request):
    profile = Profile.objects.first()
    notes = get_notes()
    context = {
        'profile': profile,
        'notes_count': len(notes)
    }
    return render(request, 'profile/profile.html', context)


def delete_profile(request):
    Profile.objects.first().delete()
    Note.objects.all().delete()
    return redirect('home page')
