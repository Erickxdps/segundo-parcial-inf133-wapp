from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.asistencia_model import Asistencia
from views import asistencia_view

# Importamos el decorador de roles
from utils.decorators import role_required

asistencia_bp = Blueprint("asistencia", __name__)

# Ruta para obtener la lista de asistencias
@asistencia_bp.route("/asistencias")
@login_required
def list_asistencias():
    asistencias = Asistencia.get_all()
    return asistencia_view.list_asistencias(asistencias)

# Ruta para crear asistencias
@asistencia_bp.route("/asistencias/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_asistencia():
    if request.method == "POST":
        if current_user.has_role("admin"):
            id_duenio = request.form["id_duenio"]
            id_reunion = request.form["id_reunion"]
            asistio = request.form["asistio"]
            asistencia = Asistencia(id_duenio = id_duenio, id_reunion = id_reunion, asistio = asistio)  
            asistencia.save()
            flash("Asistencia creado exitosamente", "success")
            return redirect(url_for("asistencia.list_asistencias"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return asistencia_view.create_asistencia()

# Ruta para actualizar asistencias por ID
@asistencia_bp.route("/asistencias/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_asistencia(id):
    asistencia = Asistencia.get_by_id(id)
    if not asistencia:
        return "Asistencia no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            id_duenio = request.form["id_duenio"]
            id_reunion = request.form["id_reunion"]
            asistio = request.form["asistio"]
            asistencia.update(id_duenio = id_duenio, id_reunion = id_reunion, asistio = asistio)
            flash("Asistencia actualizado exitosamente", "success")
            return redirect(url_for("asistencia.list_asistencias"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return asistencia_view.update_asistencia(asistencia)

# Ruta para eliminar asistencias por ID
@asistencia_bp.route("/asistencias/<int:id>/delete")
@login_required
@role_required("admin")
def delete_asistencia(id):
    asistencia = Asistencia.get_by_id(id)
    if not asistencia:
        return "Asistencia no encontrado", 404
    if current_user.has_role("admin"):
        asistencia.delete()
        flash("Asistencia eliminado exitosamente", "success")
        return redirect(url_for("asistencia.list_asistencias"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
