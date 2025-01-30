from flask import render_template #type:ignore
from flask_login import current_user #type:ignore

def list_beneficiarios(beneficiarios):
    return render_template(
        "beneficiario.html",
        beneficiarios = beneficiarios,
        title="Lista de beneficiarios",
        current_user=current_user,
    )
def create_beneficiario():
    return render_template(
        "create_beneficiario.html", title="Crear Beneficiario", current_user=current_user
    )
def update_beneficiario(beneficiario):
    return render_template(
        "update_beneficiario.html",
        title="Editar Beneficiario",
        beneficiario = beneficiario,
        current_user=current_user,
    )
