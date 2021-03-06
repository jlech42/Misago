from django.utils.translation import ugettext_lazy as _

from . import basefields


class BioField(basefields.TextareaProfileField):
    fieldname = 'bio'
    label = _("Bio")


class FullNameField(basefields.TextProfileField):
    fieldname = 'fullname'
    label = _("Full name")


class LocationField(basefields.TextProfileField):
    fieldname = 'location'
    label = _("Location")


class GenderField(basefields.ChoiceProfileField):
    fieldname = 'gender'
    label = _("Gender")

    choices = (
        ('', _('Not specified')),
        ('secret', _('Not telling')),
        ('f', _('Female')),
        ('f', _('Male')),
    )


class WebsiteField(basefields.UrlProfileField):
    fieldname = 'website'
    label = _("Website")


class SkypeHandleField(basefields.TextProfileField):
    fieldname = 'skype'
    label = _("Skype ID")


class TwitterHandleField(basefields.SlugProfileField):
    fieldname = 'twitter'
    label = _("Twitter handle")
    help_text = _('Without leading "@" sign.')
