from django import forms

class ScoreForm(forms.Form):
    q1 = forms.IntegerField(label='Pregunta 1')
    q2 = forms.IntegerField(label='Pregunta 2')
    q3 = forms.IntegerField(label='Pregunta 3')
    q4 = forms.IntegerField(label='Pregunta 4')
    q5 = forms.IntegerField(label='Pregunta 5')
