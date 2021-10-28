from wtforms import Form
from wtforms import StringField, TexField
from wtforms.fields.html5 import EmailField



class CommentForm(Form):
    username = StringField('username')
    emain = EmailField('Correo electronico')
    comment = TexField('Comentario')
