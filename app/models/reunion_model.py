from database import db
from datetime import date

class Reunion(db.Model):
    __tablename__ = "Reuniones"
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    dueño_id = db.Column(db.Integer, db.ForeignKey('Duenio.id'), nullable=False)

    def __init__(self, fecha, hora, dueño_id):
        self.fecha = fecha
        self.hora = hora
        self.dueño_id = dueño_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Reunion.query.all()

    @staticmethod
    def get_by_id(id):
        return Reunion.query.get(id)

    def update(self, fecha=None, hora=None, dueño_id=None):
        if fecha is not None:
            self.fecha = fecha
        if hora is not None:
            self.hora = hora
        if dueño_id is not None:
            self.dueño_id = dueño_id
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()