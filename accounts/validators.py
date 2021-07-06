from django.core.exceptions import (
    FieldDoesNotExist, ValidationError,
)
import re
from difflib import SequenceMatcher
from django.utils.translation import gettext as _, ngettext
from django.contrib.auth.password_validation import (
    MinimumLengthValidator,UserAttributeSimilarityValidator,CommonPasswordValidator
)



class MinimumLength(MinimumLengthValidator):

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "داشته باشد %(min_length)d  پسورد باید حداقل.",
                    "داشته باشد %(min_length)d  پسورد باید حداقل",
                    self.min_length
                ),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return ngettext(
            "داشته باشد %(min_length)d  پسورد باید حداقل",
            "داشته باشد %(min_length)d  پسورد باید حداقل",
            self.min_length
        ) % {'min_length': self.min_length}


class UserAttributeSimilarity(UserAttributeSimilarityValidator):

    def validate(self, password, user=None):
        if not user:
            return

        for attribute_name in self.user_attributes:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, str):
                continue
            value_parts = re.split(r'\W+', value) + [value]
            for value_part in value_parts:
                if SequenceMatcher(a=password.lower(), b=value_part.lower()).quick_ratio() >= self.max_similarity:
                    try:
                        verbose_name = str(user._meta.get_field(attribute_name).verbose_name)
                    except FieldDoesNotExist:
                        verbose_name = attribute_name
                    raise ValidationError(
                        _("شبیه هست %(verbose_name)s پسوردتان به "),
                        code='password_too_similar',
                        params={'verbose_name': verbose_name},
                    )

    def get_help_text(self):
        return _('پسوردتان نباید به اطلاعات شخصی تان شبیه باشد')


class CommonPassword(CommonPasswordValidator):

    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                _("پسوردتان خیلی ضعیف هست"),
                code='password_too_common',
            )

    def get_help_text(self):
        return _('پسوردتان نباید ضعیف باشد')


class NumericPassword():
    def validate(self, password, user=None):
        if not re.search("[0-9]", password):
            raise ValidationError(
                _("پسوردتان باید شامل اعداد باشد"),
                code='password_numeric',
            )

    def get_help_text(self):
        return _('پسوردتان باید شامل اعداد و حروف باشد')


class LowerCase():
    def validate(self,password,user=None):
        if not re.search("[a-z]", password):
            raise ValidationError(
                _("پسورد باید شامل حروف کوچک هم باشد"),
                code="lower_case",
            )
    def get_help_text(self):
        return _('پسوردتان باید شامل حروف کوچک باشد')


class UpperCase():
    def validate(self,password,user=None):
        if not re.search("[A-Z]", password):
            raise ValidationError(
                _("پسورد باید شامل حروف بزرگ هم باشد"),
                code="lower_case",
            )
    def get_help_text(self):
        return _('پسوردتان باید شامل حروف بزرگ باشد')