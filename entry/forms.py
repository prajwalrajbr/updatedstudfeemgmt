from django import forms
from . import models

class DateInput(forms.DateInput):
    input_type='date'

class TextInput(forms.TextInput):
    input_type="text"

class Select(forms.Select):
    input_type="option"

class TextArea(forms.Textarea):
    input_type="textarea"

class create_stud_pd(forms.ModelForm):
    class Meta:
        model = models.Stud_PD
        fields = ['Sname','USN','Gender','DOB','POB','S_Pno','S_Add','Batch']
        widgets = {
            'Sname':TextInput(attrs={'class':'form-control'}),
            'USN':TextInput(attrs={'class':'form-control'}),
            'Gender':Select(attrs={'class':'form-control'}),
            'DOB':DateInput(attrs={'class':'form-control'}),
            'POB':TextInput(attrs={'class':'form-control'}),
            'S_Pno':TextInput(attrs={'class':'form-control'}),
            'S_Add':TextArea(attrs={'class':'form-control'}),
            'Batch':Select(attrs={'class':'form-control'}),
            }
        labels = {
            "Sname": "Student Name ",
            "USN":"Student USN ",
            "DOB":"Date Of Birth ",
            "POB":"Place Of Birth ",
            "S_Pno":"Student Phone Number ",
            "S_Add":"Student Permanent Address "
        }

class create_stud_admn(forms.ModelForm):
    class Meta:
        model = models.Stud_Admn
        fields = ['Adm_No','Course','Adm_Year','Sem','Branch','Adm_Type','Quota']
        widgets = {
            'Adm_No':TextInput(attrs={'class':'form-control'}),
            'Course':Select(attrs={'class':'form-control'}),
            'Adm_Year':Select(attrs={'class':'form-control'}),
            'Sem':Select(attrs={'class':'form-control'}),
            'Branch':Select(attrs={'class':'form-control'}),
            'Adm_Type':Select(attrs={'class':'form-control'}),
            'Quota':Select(attrs={'class':'form-control'}),
        }
        labels = {
            "Adm_No":"Admission Number ",
            "Adm_Year":"Admission Year ",
            "Sem":"Semester ",
            "Adm_Type":"Admission Type "
        }