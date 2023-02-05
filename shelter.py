import database
import math
from flask import (Blueprint, request, url_for, redirect, render_template, flash, g, abort, current_app)

lat = 45.50418693241608
long = -73.61360121950645

def closer_shelter():
    shelters = database.get_shelters()
    distances = [2]
    for i in range(0, len(shelters)-1):
        distances[i] = math.sqrt((float(shelters[i][3]) - lat)**2 + (float(shelters[i][4]) - long)**2)

    closest = shelters[distances.index(min(distances))]

    return render_template('board.html', name=closest[0], image=closest[7], latitude=closest[3], longitude=closest[4])

    # return shelters[distances.index(distances.min())]

