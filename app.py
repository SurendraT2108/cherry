from flask import Flask, request

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Movie Ticket Booking</title>
    <style>
        body {
            font-family: Arial;
            background: #f4f4f4;
            padding: 40px;
        }
        .container {
            background: white;
            padding: 30px;
            max-width: 500px;
            margin: auto;
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: #4f46e5;
        }
        label {
            display: block;
            margin-top: 15px;
        }
        select, input {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
        }
        button {
            margin-top: 20px;
            width: 100%;
            padding: 12px;
            background: #4f46e5;
            color: white;
            border: none;
            font-size: 16px;
            cursor: pointer;
        }
        .result {
            margin-top: 20px;
            background: #e0e7ff;
            padding: 15px;
            border-radius: 6px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Movie Ticket Booking</h1>

    <form method="post">
        <label>Movie Name</label>
        <select name="movie">
            <option>Avengers</option>
            <option>Inception</option>
            <option>Interstellar</option>
            <option>Jawan</option>
        </select>

        <label>Number of Tickets</label>
        <input type="number" name="tickets" min="1" max="10" required>

        <button type="submit">Book Ticket</button>
    </form>

    {result}
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def book():
    result = ""
    if request.method == "POST":
        movie = request.form["movie"]
        tickets = request.form["tickets"]
        result = f"""
        <div class='result'>
            <h3>Booking Confirmed</h3>
            <p>Movie: <b>{movie}</b></p>
            <p>Tickets: <b>{tickets}</b></p>
        </div>
        """

    return HTML_PAGE.format(result=result)

if __name__ == "__main__":
    app.run(debug=True)
