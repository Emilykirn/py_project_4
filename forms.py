from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class TeamForm(FlaskForm):
    team_name = StringField('team_name',validators=[DataRequired(), Length(min=4, max=250)])
    submit = SubmitField('submit')


class ProjectForm(FlaskForm):
    project_name = StringField('project_name', validators=[DataRequired(),Length(min=5, max=100)])
    description = TextAreaField('description')
    completed = BooleanField("completed?")
    team_selection = SelectField("team")
    submit = SubmitField('submit')

    def update_teams(self, teams):
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams ]

