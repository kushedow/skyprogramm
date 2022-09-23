from flask import Blueprint, render_template

page_error = Blueprint('page_error', __name__, template_folder="templates")


@page_error.errorhandler(404)
def pageNotFound(error):
    """ Обработчик запросов к несуществующим страницам"""
    return render_template('page404.html', title="Страница не найдена", error=error)


@page_error.errorhandler(500)
def pageNotFound(error):
    """ Обработчик ошибок, возникших на стороне сервера"""
    return render_template('page500.html', title="Сервер не отвечает", error=error)
