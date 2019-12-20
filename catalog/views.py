from django.shortcuts import render
from django.conf import settings
import json

# Create your views here.


def index(request):

    basedir = settings.BASE_DIR
    filename = basedir + "/scrap/checkurl.json"
    try:
        with open(filename, "r") as f:
            dict_checkurl = json.load(f)
    except Exception as e:
        dict_checkurl = {"error", str(e)}

    dict_context = {
        "jumbotron_title": "Bienvenue sur notre page Babel",
        "jumbotron_p": "Vous aurez toutes les informations plus tard....",
        "check_url": dict_checkurl,
    }
    """ The home page for Learning Log."""
    return render(request, "index.html", context=dict_context)
