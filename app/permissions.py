from rest_framework import permissions


class GlobalPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        app_action_model_permission_codename = (
            self.__get_app_action_model_permission_codename(
                method=request.method,
                view=view,
            )
        )

        if not app_action_model_permission_codename:
            return False

        return request.user.has_perm(app_action_model_permission_codename)

    def __get_app_action_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_action_sufix(self, method):
        method_actions = {
            'POST': 'add',
            'DELETE': 'delete',
            'PUT': 'change',
            'PATCH': 'change',
            'GET': 'view',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')
