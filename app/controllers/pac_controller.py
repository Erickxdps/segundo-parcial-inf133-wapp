from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.pac_model import Paciente
from views import pac_view
from utils.decorators import role_required


paciente_bp = Blueprint("paciente", __name__)
# ruta pacientes
@paciente_bp.route("/pacientes")
@login_required
def list_pacientes():
    pacientes = Paciente.get_all()
    return pac_view.list_pacientes(pacientes)
# Crea pacientes 
@paciente_bp.route("/pacientes/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_paciente():
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            lastname = request.form["lastname"]
            ci = request.form["ci"]
            birth_date = request.form["birth_date"]
            paciente = Paciente(name = name, lastname=lastname, ci = ci , birth_date=birth_date)
            paciente.save()
            flash("Paciente creado exitosamente", "success")
            return redirect(url_for("paciente.list_pacientes"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return pac_view.create_paciente()
# Actualiza pacientes por ID
@paciente_bp.route("/pacientes/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_paciente(id):
    paciente = Paciente.get_by_id(id)
    if not paciente:
        return "Paciente no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            lastname = request.form["last_name"]
            ci = request.form["ci"]
            birth_date = request.form["birth_date"]
            paciente.update(name = name, lastname=lastname, ci = ci , birth_date=birth_date)
            flash("Paciente actualizado exitosamente", "success")
            return redirect(url_for("paciente.list_pacientes"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return pac_view.update_paciente(paciente)
# Elimina pacientes por ID
@paciente_bp.route("/pacientes/<int:id>/delete")
@login_required
@role_required("admin")
def delete_paciente(id):
    paciente = Paciente.get_by_id(id)
    if not paciente:
        return "Paciente no encontrado", 404
    if current_user.has_role("admin"):
        paciente.delete()
        flash("Paciente eliminao", "success")
        return redirect(url_for("paciente.list_pacientes"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
