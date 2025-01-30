from database import db

class Beneficiario(db.Model):
    # aca se crea la tabla para los paciente 
    __tablename__ = "beneficiarios"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(), nullable=False)
    ci = db.Column(db.String(100), nullable=False)
    # nroManzano = db.Column(db.Integer, nullable=False)
    # nroLote = db.Column(db.Integer, nullable=False)
    asistencia = db.Column(db.Boolean, nullable=False)
    # constructor o algo asi Dx
    def __init__(self, name, lastname, ci , nroManzano, nroLote, asistencia):
        self.name = name
        self.lastname = lastname
        self.ci = ci 
        self.nroManzano = nroManzano
        self.nroLote = nroLote
        self.asistencia = bool(asistencia)
    # save = guardar xd
    def save(self):
        db.session.add(self)
        db.session.commit()
    # get todoooo
    @staticmethod
    def get_all():
        return Beneficiario.query.all()
    # get pero por id
    @staticmethod
    def get_by_id(id):
        return Beneficiario.query.get(id)
    #actualizar
    def update(self, name = None, lastname = None, ci = None , NroManzano = None, NroLote = None, asistencia = None):
        if name is not None:
            self.name = name
        if lastname is not None:
            self.lastname = lastname
        if ci is not None:
            self.ci = ci
        if NroManzano is not None:
            self.NroManzano = NroManzano
        if NroLote is not None:
            self.NroLote = NroLote
        if asistencia is not None:
            self.asistencia = asistencia
        db.session.commit()
    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()
