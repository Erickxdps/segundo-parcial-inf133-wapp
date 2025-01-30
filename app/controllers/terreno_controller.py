from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.terreno_model import Terreno
from views import terreno_view
from utils.decorators import role_required

terreno_bp = Blueprint("terreno", __name__)

# Ruta para obtener la lista de terrenos
@terreno_bp.route("/terrenos")
@login_required
def list_terrenos():
    terrenos = Terreno.get_all()
    return terreno_view.list_terrenos(terrenos)

# Ruta para crear terrenos
@terreno_bp.route("/terrenos/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_terreno():
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = float(request.form["peso"])
            sabor = request.form["sabor"]
            origen = request.form["origen"]
            terreno = Terreno(marca = marca, peso = peso, sabor = sabor, origen = origen)
            terreno.save()
            flash("Terreno creado exitosamente", "success")
            return redirect(url_for("terreno.list_terrenos"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return terreno_view.create_terreno()

# Ruta para actualizar terrenos por ID
@terreno_bp.route("/terrenos/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_terreno(id):
    terreno = Terreno.get_by_id(id)
    if not terreno:
        return "Terreno no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = float(request.form["peso"])
            sabor = request.form["sabor"]
            origen = request.form["origen"]
            terreno.update(marca = marca, peso = peso, sabor = sabor, origen = origen)
            flash("Terreno actualizado exitosamente", "success")
            return redirect(url_for("terreno.list_terrenos"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return terreno_view.update_terreno(terreno)

# Ruta para eliminar terrenos por ID
@terreno_bp.route("/terrenos/<int:id>/delete")
@login_required
@role_required("admin")
def delete_terreno(id):
    terreno = Terreno.get_by_id(id)
    if not terreno:
        return "Terreno no encontrado", 404
    if current_user.has_role("admin"):
        terreno.delete()
        flash("Terreno eliminado exitosamente", "success")
        return redirect(url_for("terreno.list_terrenos"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
