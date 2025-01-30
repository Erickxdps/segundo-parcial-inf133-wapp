from flask import Blueprint, request, redirect, url_for, flash, jsonify #type:ignore
from flask_login import login_required, current_user #type:ignore
from models.beneficiario_model import Beneficiario
from views import beneficiario_view
from utils.decorators import role_required


beneficiario_bp = Blueprint("beneficiario", __name__)
# ruta beneficiarios
@beneficiario_bp.route("/beneficiarios")
@login_required
def list_beneficiarios():
    beneficiarios = Beneficiario.get_all()
    return beneficiario_view.list_beneficiarios(beneficiarios)
# Crea beneficiarios 
@beneficiario_bp.route("/beneficiarios/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_beneficiario():
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            lastname = request.form["lastname"]
            ci = request.form["ci"]
            nroManzano = request.form["nroManzano"]
            nroLote = request.form["nroLote"]
            
            beneficiario = Beneficiario(name = name, lastname=lastname, ci = ci , nroManzano=nroManzano, nroLote=nroLote, asistencia=False)
            beneficiario.save()
            flash("Beneficiario creado exitosamente", "success")
            return redirect(url_for("beneficiario.list_beneficiarios"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return beneficiario_view.create_beneficiario()
# Actualiza beneficiarios por ID
@beneficiario_bp.route("/beneficiarios/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_beneficiario(id):
    beneficiario = Beneficiario.get_by_id(id)
    if not beneficiario:
        return "Beneficiario no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            name = request.form["name"]
            lastname = request.form["lastname"]
            ci = request.form["ci"]
            nroManzano = request.form["nroManzano"]
            nroLote = request.form["nroLote"]
            beneficiario.update(name = name, lastname=lastname, ci = ci , nroManzano=nroManzano, nroLote=nroLote, asistencia=False)
            flash("Beneficiario actualizado exitosamente", "success")
            return redirect(url_for("beneficiario.list_beneficiarios"))
        else:
            return jsonify({"message": "Unauthorized"}), 403
    return beneficiario_view.update_beneficiario(beneficiario)
# Elimina beneficiarios por ID
@beneficiario_bp.route("/beneficiarios/<int:id>/delete")
@login_required
@role_required("admin")
def delete_beneficiario(id):
    beneficiario = Beneficiario.get_by_id(id)
    if not beneficiario:
        return "Beneficiario no encontrado", 404
    if current_user.has_role("admin"):
        beneficiario.delete()
        flash("Beneficiario eliminado", "success")
        return redirect(url_for("beneficiario.list_beneficiarios"))
    else:
        return jsonify({"message": "Unauthorized"}), 403
#actualizar asistencia
@beneficiario_bp.route("/beneficiarios/update_asistencia", methods=["POST"])
@login_required
@role_required("admin")
def update_asistencia():
    beneficiario_id = request.form.get("beneficiario_id")
    asistencia = request.form.get("asistencia")  # Asume que asistencia es un valor booleano o entero
    beneficiario = Beneficiario.query.get(beneficiario_id)
    if beneficiario:
        beneficiario.asistencia = asistencia  # Asegúrate de que este campo exista en tu modelo
        beneficiario.save()  # O usa db.session.commit() dependiendo de cómo manejes las transacciones en tu ORM
        flash("Asistencia actualizada con éxito.", "success")
    else:
        flash("Beneficiario no encontrado.", "error")
    return redirect(url_for("beneficiario.list_beneficiarios"))

@beneficiario_bp.route('/update_assist/<int:id>', methods=['POST'])
@login_required
@role_required("admin")
def actualizar_asistencia(id):
    beneficiario = Beneficiario.query.get_or_404(id)
    beneficiario.asistencia = 'asistencia' in request.form
    beneficiario_bp.session.commit()
    return redirect(url_for('ruta_donde_se_muestra_beneficiario'))