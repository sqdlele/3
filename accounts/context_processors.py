from .models import Profile


def navigation_context(request):
    is_admin_nav = False
    if request.user.is_authenticated:
        is_admin_nav = request.user.is_superuser or Profile.objects.filter(
            user=request.user,
            role='admin',
        ).exists()
    return {'is_admin_nav': is_admin_nav}
