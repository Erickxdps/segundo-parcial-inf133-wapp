from database import db

class Asistencia(db.Model):
    __tablename__ = "Asistencia"
    id = db.Column(db.Integer, primary_key=True)
    id_duenio = db.Column(db.Integer, db.ForeignKey('Duenio.id'), nullable=False)
    id_reunion = db.Column(db.Integer, db.ForeignKey('Reuniones.id'), nullable=False)
    asistio = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, id_duenio, id_reunion, asistio=False):
        self.id_duenio = id_duenio
        self.id_reunion = id_reunion
        self.asistio = asistio

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Asistencia.query.all()

    @staticmethod
    def get_by_id(id):
        return Asistencia.query.get(id)

    def update(self, id_duenio=None, id_reunion=None, asistio=None):
        if id_duenio is not None:
            self.id_duenio = id_duenio
        if id_reunion is not None:
            self.id_reunion = id_reunion
        if asistio is not None:
            self.asistio = asistio
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()