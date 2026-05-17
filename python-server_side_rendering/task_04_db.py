#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/items")
def items():

    try:
        with open("items.json", "r") as file:
            data = json.load(file)
            items = data.get("items", [])

        return render_template("items.html", items=items)

    except FileNotFoundError:
        return "Items file not found", 404

    except json.JSONDecodeError:
        return "Error decoding JSON", 500


def read_json():

    with open("products.json", "r") as file:

        data = json.load(file)

        if isinstance(data, dict):
            return data.get("products", [])

        return data


def read_csv():

    with open("products.csv", newline="") as file:

        reader = csv.DictReader(file)
        return list(reader)


def read_sql():

    conn = sqlite3.connect("products.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")

    rows = cursor.fetchall()

    conn.close()

    products = []

    for row in rows:
        products.append({
            "id": row["id"],
            "name": row["name"],
            "category": row["category"],
            "price": row["price"]
        })

    return products


@app.route("/products")
def products():

    source = request.args.get("source")
    product_id = request.args.get("id")

    try:

        if source == "json":
            data = read_json()

        elif source == "csv":
            data = read_csv()

        elif source == "sql":
            data = read_sql()

        else:
            return render_template(
                "product_display.html",
                error="Wrong source"
            )

    except FileNotFoundError:
        return render_template(
            "product_display.html",
            error="File not found"
        )

    except json.JSONDecodeError:
        return render_template(
            "product_display.html",
            error="Error decoding JSON"
        )

    except sqlite3.Error:
        return render_template(
            "product_display.html",
            error="Database error"
        )

    except Exception:
        return render_template(
            "product_display.html",
            error="Error reading file"
        )

    if product_id:

        filtered_products = []

        for product in data:

            if str(product.get("id")) == str(product_id):
                filtered_products.append(product)

        if not filtered_products:

            return render_template(
                "product_display.html",
                error="Product not found"
            )

        return render_template(
            "product_display.html",
            products=filtered_products
        )

    return render_template(
        "product_display.html",
        products=data
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)