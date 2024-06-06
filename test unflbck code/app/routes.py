from flask import render_template, request
from app import app
from Date_Format_Remover import remove_date_formats
from Difference_Between_lists import print_difference_between_lists

# Route for rendering the form
@app.route('/')
def index():
    return render_template('index.html')

# Route for processing form submission
@app.route('/submit', methods=['POST'])
def submit():
    followers = request.form['followers']
    following = request.form['following']

    # Remove date formats and split input into lists
    list1 = [remove_date_formats(name.strip()) for name in followers.split('\n')]
    list2 = [remove_date_formats(name.strip()) for name in following.split('\n')]

    # Get differences between lists
    only_in_list1, only_in_list2 = print_difference_between_lists(list1, list2)

    return render_template('result.html', only_in_list1=only_in_list1, only_in_list2=only_in_list2)
