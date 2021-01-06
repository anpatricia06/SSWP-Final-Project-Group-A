from django.forms import ModelForm
from django.core.exceptions import ValidationError
from school.models.student import Student
from school.models.teacher import Teacher
from school.models.student_id import StudentId
from school.models.teacher_id import TeacherId
from school.models.subject import Subject
from school.models.position import TeacherPosition
from school.models.oxford import Dictionary
from school.models.extracurricular import Extracurricular
from django.conf import settings
import requests

class StudentForm(ModelForm):
    class Meta:
        model= Student
        fields= ['student_id', 's_name', 's_dob', 's_address', 's_phonenum', 's_email', 'teacher_id', 'extracurricular']

class TeacherForm(ModelForm):
    class Meta:
        model= Teacher
        fields=['teacher_id', 't_name', 'subject', 't_dob', 't_address', 't_phonenum', 't_email', 'position']

class DictionaryForm(ModelForm):
    class Meta:
        model= Dictionary
        fields=['word']

    def search(self):
        result = {}
        word = self.cleaned_data['word']
        endpoint = 'https://od-api.oxforddictionaries.com/api/v2/entries/{source_lang}/{word_id}'
        url = endpoint.format(source_lang='en', word_id=word)
        headers = {'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'No entry found for "%s"' % word
            else:
                result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
        return result
