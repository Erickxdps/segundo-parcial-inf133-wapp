from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.reunion_model import Reunion
from views import reunion_view
from utils.decorators import role_required

reunion_bp = Blueprint("reunion", __name__)

# Ruta para obtener la lista de reuniones
@reunion_bp.route("/reuniones")
@login_required
def list_reuniones():
    reuniones = Reunion.get_all()
    return reunion_view.list_reuniones(reuniones)


@reunion_bp.route("/reuniones/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_reunion():
    if request.method == "POST":
        if current_user.has_role("admin"):
            fecha = request.form["fecha"]
            hora = request.form["hora"]
            dueño_id = request.form["dueño_id"]
            reunion = Reunion(fecha = fecha, hora = hora, dueño_id = dueño_id)
            reunion.save()
            flash("Reunion creado exitosamente", "success")
            return redirect(url_for("reunion.list_reuniones"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return reunion_view.create_reunion()


@reunion_bp.route("/reuniones/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_reunion(id):
    reunion = Reunion.get_by_id(id)
    if not reunion:
        return "Reunion no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            fecha = request.form["fecha"]
            hora = request.form["hora"]
            dueño_id = request.form["dueño_id"]
            reunion.update(fecha = fecha, hora = hora, dueño_id = dueño_id)
            flash("Reunion actualizado exitosamente", "success")
            return redirect(url_for("reunion.list_reuniones"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return reunion_view.update_reunion(reunion)


@reunion_bp.route("/reuniones/<int:id>/delete")
@login_required
@role_required("admin")
def delete_reunion(id):
    reunion = Reunion.get_by_id(id)
    if not reunion:
        return "Reunion no encontrado", 404
    if current_user.has_role("admin"):
        reunion.delete()
        flash("Reunion eliminado exitosamente", "success")
        return redirect(url_for("reunion.list_reuniones"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
