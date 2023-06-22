from django.core.exceptions import ValidationError


# User model
def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit * 1024 * 1024:
        raise ValidationError("Maksimal hajmi %sMB bo'lishi lozim!" % str(megabyte_limit))


# User model
def custom_validator(value):
    valid_formats = ['png', 'jpeg', 'jpg', 'jfif']
    if not any([True if value.name.lower().endswith(i) else False for i in valid_formats]):
        raise ValidationError('Mos format emas. Iltimos, png, jpeg yoki jpg formatda yuklang')


# Post model
def post_validator(value):
    valid_formats = ['png', 'jpeg', 'jpg', 'dwg', 'max', 'crd', 'doc', 'docx', 'pdf', 'xlsx']
    if not any([True if value.name.lower().endswith(i) else False for i in valid_formats]):
        raise ValidationError('Mos format emas. Iltimos boshqa formatda yuklab ko`ring!')


# Post model
def validate_file(fieldfile_obj):
    filesize = fieldfile_obj.size
    megabyte_limit = 30.0
    if filesize > megabyte_limit * 2048 * 2048:
        raise ValidationError("Maksimal hajmi %sMB bo'lishi lozim!" % str(megabyte_limit))
