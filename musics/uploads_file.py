import mimetypes
from os.path import splitext

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat


class FileValidator(object):
    min_size_message = _('The current file %(size)s, which is too small. The minumum file size is %(allowed_size)s.')
    max_size_message = _('The current file %(size)s, which is too large. The maximum file size is %(allowed_size)s.')

    def __init__(self, *args, **kwargs):

        self.min_size = kwargs.pop('min_size', 0)
        self.max_size = kwargs.pop('max_size', None)

    def __call__(self, value):
        # Check the file size
        filesize = len(value)
        if self.max_size and filesize > self.max_size:
            message = self.max_size_message % {
                'size': filesizeformat(filesize),
                'allowed_size': filesizeformat(self.max_size)
            }

            raise ValidationError(message)

        elif filesize < self.min_size:
            message = self.min_size_message % {
                'size': filesizeformat(filesize),
                'allowed_size': filesizeformat(self.min_size)
            }

            raise ValidationError(message)