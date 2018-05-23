from krvjezivot.users.models import User
from krvjezivot.common.models import Notification


def add_users_list_to_context(request):
    if request.user.is_authenticated:
        users_list = User.objects.filter(
            is_superuser=False).order_by('full_name')
    else:
        users_list = []
    return {'users_list': users_list}


def add_notifications_list_to_context(request):
    if request.user.is_authenticated:
        notifications_list = Notification.objects.filter(
            assigned_to=request.user.id)
        notifications_new_cnt = len(
            [n for n in notifications_list if n.seen is False])
    else:
        notifications_list = []
        notifications_new_cnt = 0
    return {
        'notifications_list': notifications_list,
        'notifications_new_cnt': notifications_new_cnt
    }
