from . import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    project_type = db.Column(db.String(50))
    duration = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'project_type': self.project_type,
            'duration': self.duration
        }
