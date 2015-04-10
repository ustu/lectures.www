from jinja2 import Template
from wtforms import BooleanField, Form, StringField, validators


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    rules = BooleanField('I accept the site rules',
                         [validators.InputRequired()])

if __name__ == '__main__':
    form = RegistrationForm(username="root")
    template = Template("""
<form method="POST" action="">
    {% for field in form.data %}
        {{ form[field].label }} |
        {{ form[field] }}
        <br />
    {% endfor %}
    <input type="submit" value="Ok">
</form>
    """)
    print(template.render(form=form))
