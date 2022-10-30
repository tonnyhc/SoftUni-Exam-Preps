from django.shortcuts import render, redirect

from car_collection_exam.car_collection_app.form import ProfileCreateForm, CarCreateForm, CarDeleteForm, CarEditForm, \
    ProfileEditForm, ProfileDeleteForm
from car_collection_exam.car_collection_app.models import Profile, Car


def index(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'common/index.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()
    context = {
        'cars':cars,
        'profile': profile,
        'full_name': get_profile_full_name(profile),
        'cars_price': get_all_cars_price(cars)
    }
    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = ProfileEditForm(instance=profile)
    context = {
        'form':form,
        'profile': profile
    }
    return render(request, 'profile/profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    if request.method == "POST":
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = ProfileDeleteForm(instance=profile)
    context = {
        'profile':profile,
        'form':form
    }
    return render(request, 'profile/profile-delete.html', context)


def create_profile(request):
    if request.method == "POST":
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileCreateForm()
    context = {
        'form': form
    }
    return render(request, 'profile/profile-create.html', context)


def catalogue(request):
    cars = Car.objects.all()
    profile = Profile.objects.first()
    context = {
        'cars': cars,
        'profile': profile,
        'cars_count': len(cars)
    }
    return render(request, 'common/catalogue.html', context)


def create_car(request):
    if request.method == "POST":
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarCreateForm()
    context = {
        'form': form,
        'profile': Profile.objects.first()
    }
    return render(request, 'car/car-create.html', context)


def details_car(request, pk):
    profile = Profile.objects.first()
    car = Car.objects.get(pk=pk)
    context = {
        'profile': profile,
        'car': car,
    }
    return render(request, 'car/car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    profile = Profile.objects.first()
    if request.method == "POST":
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarEditForm(instance=car)
    context = {
        'car': car,
        'form': form,
        'profile': profile,
    }
    return render(request, 'car/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    profile = Profile.objects.first()
    if request.method == "POST":
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarDeleteForm(instance=car)
    context = {
        'car': car,
        'form': form,
        'profile': profile,
    }

    return render(request, 'car/car-delete.html', context)


def get_profile_full_name(profile):
    result = ''
    if profile.first_name:
        result += profile.first_name + " "
    if profile.last_name:
        result += profile.last_name + ' '
    return result


def get_all_cars_price(cars):
    result = 0
    for car in cars:
        result += car.price
    return result
