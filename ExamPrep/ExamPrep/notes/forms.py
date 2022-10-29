from django import forms

from ExamPrep.notes.models import Note, Profile


class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']


class AddNoteForm(NoteBaseForm):
    pass


class EditNoteForm(NoteBaseForm):
    pass


class DeleteNoteForm(NoteBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_input_fields()

    def _disable_input_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            # field.widget.attr['disabled'] = 'disabled'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
