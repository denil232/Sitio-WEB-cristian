from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Aquí ocurre la magia: le decimos que busque si lo que escribiste
            # coincide con el 'username' O con el 'email'
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            # Si no existe ni como usuario ni como email
            return None
        except UserModel.MultipleObjectsReturned:
            # Si por error hubiera duplicados, tomamos el primero
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()

        # Si encontró al usuario y la contraseña es correcta
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None