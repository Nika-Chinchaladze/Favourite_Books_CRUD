from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myBooks.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE SQL myBooks DATABASE WITH Book TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.route("/")
def home_page():
    book_data = db.session.query(Book).all()
    return render_template("index.html", book_list=book_data)


@app.route("/add", methods=["GET", "POST"])
def add_page():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        db.session.close()
        return redirect(url_for("home_page"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit_page():
    # come back from edit into home page with changes:
    if request.method == "POST":
        update_id = request.form["id"]
        update_record = Book.query.get(update_id)
        update_record.title = request.form["title"]
        update_record.author = request.form["author"]
        update_record.rating = request.form["rating"]
        db.session.commit()
        db.session.close()
        return redirect(url_for("home_page"))
    # enter into edit page with chosen book:
    chosen_id = request.args.get("id")
    current_book = Book.query.get(chosen_id)
    return render_template("edit.html", book=current_book)


@app.route("/delete")
def delete_page():
    delete_id = request.args.get("id")
    delete_record = Book.query.get(delete_id)
    db.session.delete(delete_record)
    db.session.commit()
    db.session.close()
    return redirect(url_for("home_page"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
