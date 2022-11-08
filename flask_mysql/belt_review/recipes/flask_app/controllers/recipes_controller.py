from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe



@app.route('/recipes/new')
def new_recipe():
    return render_template('recipe_new.html')


@app.route('/recipes/create', methods = ['POST'])
def create_recipe():
    if 'user_id' not in session:
        return('/')
    if not Recipe.validator(request.form):
        return redirect('/recipes/new')
    recipe_data = {
        **request.form,
        'user_id' : session['user_id']
    }
    Recipe.create(recipe_data)
    return redirect('/dashboard')


@app.route('/recipes/<int:id>')
def show_one_recipe(id):
    if 'user_id' not in session:
        return('/')
    this_recipe = Recipe.get_by_id({'id' : id})
    logged_user = User.get_by_id({'id' : session['user_id']})
    return render_template('recipe_one.html', this_recipe = this_recipe, logged_user = logged_user)


# @app.route('/my_recipes')
# def show_recipes_for_logged_user():
#     if 'user_id' not in session:
#         return('/')
#     logged_user = User.get_by_id({'id' : session['user_id']})
#     return render_template('/my_recipes.html', logged_user = logged_user)


@app.route('/recipes/<int:id>/edit')
def edit_user_recipe(id):
    if 'user_id' not in session:
        return('/')
    data = {
        'id' : id
    }
    one_recipe = Recipe.get_by_id(data)

    if not one_recipe.user_id == session['user_id']: #                      extra
        flash('You are not original owner of recipe. Cannot edit!')
        return redirect('/dashboard')

    return render_template('recipe_edit.html', one_recipe = one_recipe)


@app.route('/recipes/<int:id>/update', methods = ['POST'])
def update_user(id):
    if 'user_id' not in session:
        return('/')

    if not Recipe.validator(request.form):
        return redirect(f'/recipes/{id}/edit')

    data = {
        'id' : id,
        **request.form
    }
    recipe_to_update = Recipe.get_by_id(data)

    if not recipe_to_update.user_id == session['user_id']: #                extra
        flash('Unauthorized user! Cannot update!')
        return redirect('/dashboard')

    Recipe.update(data)
    return redirect('/dashboard')


@app.route('/recipes/<int:id>/delete')
def del_recipe(id):
    if 'user_id' not in session:
        return('/')
    data = {
        'id' : id,
    }
    this_recipe = Recipe.get_by_id(data)

    if not this_recipe.user_id == session['user_id']: #                     extra
        flash('Unauthorized user! Cannot delete!')
        return redirect('/dashboard')
    
    Recipe.delete(data)
    return redirect('/dashboard')