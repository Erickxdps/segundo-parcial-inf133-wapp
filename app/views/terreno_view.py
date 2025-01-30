from flask import render_template
from flask_login import current_user


# La función `list_terrenos` recibe una lista de
# terrenoes y renderiza el template `terrenoes.html`
def list_terrenos(terrenos):
    return render_template(
        "terrenos.html",
        terrenos = terrenos,
        title="Lista de terrenos",
        current_user=current_user,
    )


# La función `create_terreno` renderiza el
# template `create_terreno.html` o devuelve un JSON
# según la solicitud
def create_terreno():
    return render_template(
        "create_terreno.html", title="Crear Libro", current_user=current_user
    )


# La función `update_terreno` recibe un terreno
# y renderiza el template `update_terreno.html`
def update_terreno(terreno):
    return render_template(
        "update_terreno.html",
        title="Editar Libro",
        terreno=terreno,
        current_user=current_user,
    )
