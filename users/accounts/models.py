from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class UserModel(AbstractBaseUser):
    login = models.CharField(_("login"), max_length=50, unique=True)
    name = models.CharField(_("name"), max_length=100)
    user_type = models.CharField(_("user type"), max_length=1)
    main_email = models.EmailField(_("main email"), max_length=50)
    alternative_email = models.EmailField(_("alternative email"),
                                          max_length=254)
    usp_email = models.EmailField(_("email usp"), max_length=254)
    formatted_phone = models.CharField(_("phone"), max_length=50)
    wsuserid = models.CharField(_("wsuserid"), max_length=1024)
    bind = models.TextField(_("bind"))
    is_staff = models.BooleanField(_("is staff"))
    is_active = models.BooleanField(_("is active"))
    date_joined = models.DateTimeField(_("Joined at"), auto_now_add=True)

    USERNAME_FIELD = 'login'
    EMAIL_FIELD = 'main_email'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        short_name = self.name.split()[0]
        return short_name
