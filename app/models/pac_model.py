from database import db

class Paciente(db.Model):
    # aca se crea la tabla para los paciente 
    __tablename__ = "pacientes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(), nullable=False)
    ci = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.String(100), nullable=False)
    # constructor o algo asi Dx
    def __init__(self, name, lastname, ci , birth_date):
        self.name = name
        self.lastname = lastname
        self.ci = ci 
        self.birth_date = birth_date
    # save = guardar xd
    def save(self):
        db.session.add(self)
        db.session.commit()
    # get todoooo
    @staticmethod
    def get_all():
        return Paciente.query.all()
    # get pero por id
    @staticmethod
    def get_by_id(id):
        return Paciente.query.get(id)
    #actualizar
    def update(self, name = None, lastname = None, ci = None , birth_date = None):
        if name is not None:
            self.name = name
        if lastname is not None:
            self.lastname = lastname
        if ci is not None:
            self.ci = ci
        if birth_date is not None:
            self.birth_date = birth_date
        db.session.commit()
    #eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()
