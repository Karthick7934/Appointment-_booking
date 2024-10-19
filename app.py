import mysql.connector
from mysql.connector import Error
import openai
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


# Configure OpenAI API
openai.api_key = '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'

# Database connection function
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='Raja@397',  # Replace with your MySQL password
            database='AppointmentBooking'  # Make sure your database name is correct
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to insert appointment data
def insert_appointment(connection, appointment):
    cursor = connection.cursor()
    query = "INSERT INTO appointments (name, email, phone_number, age, appointment_time) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, appointment)
    connection.commit()
    return cursor.lastrowid

# Function to get available appointment slots
def get_available_slots():
    now = datetime.datetime.now()
    return [now + datetime.timedelta(days=i) for i in range(1, 6)]

# Function to validate user details
def validate_user_details(name, email, phone, age):
    if not all([name, email, phone, age]):
        return False
    if age > 0:
        return True
    else:
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    available_slots = get_available_slots()
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        age = int(request.form['age'])


        if not validate_user_details(name, email, phone, age):
            flash("Please provide valid details.")
            return redirect(url_for('index'))

        
        selected_time = request.form.get('selected_time')

        if selected_time:
            appointment = (name, email, phone, age, selected_time)
            connection = create_connection()
            insert_appointment(connection, appointment)
            connection.close()
            return redirect(url_for('confirmation'))

        return render_template('index.html', available_slots=available_slots)

    return render_template('index.html', available_slots=available_slots)
def chat_with_gpt(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model to use
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

@app.route('/confirmation',methods=['GET', 'POST'])
def confirmation():
    if request.method == 'POST':
        userinput = request.form['name']
        data  = chat_with_gpt(userinput)
        return render_template('confirmation.html',data)
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
