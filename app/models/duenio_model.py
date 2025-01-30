from database import db

class Duenio(db.Model):
    __tablename__ = "Duenio"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    paterno = db.Column(db.String(20), nullable=False)
    materno = db.Column(db.String(20), nullable=False)
    ci = db.Column(db.String(20), nullable=False, unique=True)

    def __init__(self, nombre, paterno, materno, ci):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.ci = ci

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Duenio.query.all()

    @staticmethod
    def get_by_id(id):
        return Duenio.query.get(id)

    def update(self, nombre=None, paterno=None,materno=None, ci=None):
        if nombre is not None:
            self.nombre = nombre
        if paterno is not None:
            self.paterno = paterno
        if materno is not None:
            self.materno = materno
        if ci is not None:
            self.ci = ci
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()