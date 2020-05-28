from django import forms


class LazyQuestionForm(forms.Form):
    question = forms.CharField(required=True, label="email")


class CustomForm(forms.Form):
    def __init__(self, context, spreadsheet=None, *args, **kwargs):
        super(CustomForm, self).__init__(*args, **kwargs)

        if context.method == "GET":
            for field in spreadsheet.spreadsheetfield_set.iterator():
                key = field.field_name.lower().replace(" ", "_")
                if field.field_type == "INTEGER":
                    self.fields[key] = forms.IntegerField(
                        required=True, label=field.field_name
                    )
                elif field.field_type == "STRING":
                    self.fields[key] = forms.CharField(
                        required=True, label=field.field_name
                    )
                elif field.field_type == "BOOL":
                    self.fields[key] = forms.BooleanField(
                        required=True, label=field.field_name
                    )
