from flask import render_template
from flask_login import current_user

def list_pacientes(pacientes):
    return render_template(
        "pacientes.html",
        pacientes = pacientes,
        title="Lista de pacientes",
        current_user=current_user,
    )
def create_paciente():
    return render_template(
        "create_pacientes.html", title="Crear Paciente", current_user=current_user
    )
def update_paciente(paciente):
    return render_template(
        "update_paciente.html",
        title="Editar Paciente",
        paciente=paciente,
        current_user=current_user,
    )
