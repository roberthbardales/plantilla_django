from django  import forms

from .models import Project

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        #fields =(__all_)
        fields =(
        'title',
        'description',
        'image',
        'tags',
        'category',

        )
        widgets={

            'category':forms.Select(
                attrs={
                'class':'form-control form-control',
                }
            ),

            'title':forms.TextInput(
                attrs={
                    'class':'form-control form-control',
                }
            ),
            'tags':forms.SelectMultiple(
                attrs={

                    'class':'form-control form-control',
                }
            ),
            'description':forms.Textarea(
                attrs={
                    'class':'form-control form-control',
                    'rows':'2',
                }
            ),

        }

            # 'public':forms.CheckboxInput(
            #     attrs={
            #         'checked':'',
            #     }
            # ),
            # 'user':forms.Select(
            #     attrs={
            #     'class':'form-control form-control-sm',

            #     }
            # ),