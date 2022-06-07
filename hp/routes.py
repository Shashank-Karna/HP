from flask import render_template, url_for, flash, redirect
from flask_login import login_user, current_user, logout_user, login_required
from hp import app, db
from hp.models import User, Test
from hp.forms import TestForm


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/test", methods=["GET", "POST"])
def test():
    form = TestForm()
    if form.validate_on_submit():
        test = Test(
            age=form.age.data,
            gender=form.gender.data,
            cp=form.cp.data,
            trest_bps=form.trest_bps.data,
            chol=form.chol.data,
            fbs=form.fbs.data,
            rest_ecg=form.rest_ecg.data,
            thalach=form.thalach.data,
            exang=form.exang.data,
            old_peak=form.old_peak.data,
            slope=form.slope.data,
            ca=form.ca.data,
            thal=form.thal.data,
            user=current_user,
        )
        db.session.add(test)
        db.session.commit()
        flash("Your data has been collected for the test.", "success")
        return redirect(url_for("home"))
    return render_template("test.html", title="Test", form=form, legend="Test")
