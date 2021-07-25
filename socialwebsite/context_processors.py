from account.models import Profile


def global_processor(request):
    profile = Profile.objects.all()

    context = {
        'profile': profile,
    }

    return context