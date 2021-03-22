from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field


class UserAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        role_id = data.get('role_id')

        if role_id:
            setattr(user, 'role_id', role_id)
        return super().save_user(request, user, form, commit=commit)
