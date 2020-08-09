from django.core.exceptions import ValidationError, MultipleObjectsReturned
from django.forms import ModelForm

from student.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAddForm(StudentBaseForm):
    pass


class StudentEditForm(StudentBaseForm):

    def clean(self):
        fname1 = self.instance.first_name
        lname1 = self.instance.last_name
        fname = self.cleaned_data['first_name']
        lname = self.cleaned_data['last_name']
        s = Student.objects.filter(first_name=fname, last_name=lname).exists()

        if fname == fname1 and lname == lname1:
            return self.cleaned_data
        elif s is True:
            raise ValidationError("Student with such name already exists")
        else:
            return self.cleaned_data

    def clean_email(self):
        email1 = self.instance.email
        email = self.cleaned_data['email']
        b = Student.objects.filter(email=email).exists()

        if email == email1:
            return email
        elif b is True:
            raise ValidationError('Email already exists')
        else:
            return email


class StudentDeleteForm(StudentBaseForm):
    pass
