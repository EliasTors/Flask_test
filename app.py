# flask run --host=0.0.0.0 -p 80

from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import random
import os

def get_dropdown_values():
    df = pd.read_csv('data.csv')
    return df.iloc[:, 1].tolist()  # Get all values from the second column


app = Flask(__name__, template_folder='.')
df = pd.read_csv('data.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    
    dropdown_values = get_dropdown_values()
    selected_data = ''  # Initialize selected_data
    selected_value = request.form.get('my_dropdown')
    if request.method == 'POST':
        
        print(selected_value)
        
        print(selected_value)
        selected_data = df.loc[df['Country'] == selected_value, 'Erect length'].values[0]
    
        
    return render_template('site.html', dropdown_values=dropdown_values, selected_value=selected_value, selected_data=selected_data)


@app.route('/button/<int:button_id>')
def button(button_id):
    global mode
    mode = button_id
    
    return str(mode)  # Return the new value of the variable


def list_files(directory):
    return os.listdir(directory)

mode = 0

@app.route('/amalia')
def random_image():
    image_dir_bal = 'static/Balder'  # Replace with your directory path
    image_dir_cat = 'static/cats'  # Replace with your directory path
    balder = [f for f in os.listdir(image_dir_bal) if os.path.isfile(os.path.join(image_dir_bal, f))]
    cats = [f for f in os.listdir(image_dir_cat) if os.path.isfile(os.path.join(image_dir_cat, f))]
    match mode:
        case 0:
            image_file = random.choice(balder)
            path='Balder/'
            
        case 1:
            image_file = random.choice(cats)
            path='cats/'
        case 2:
            choice = random.choice(['cats', 'balder', 'bal'])
            if choice == 'cats':
                image_file = random.choice(cats)
                path='cats/'
            elif choice == 'balder' or choice == 'bal':
                image_file = random.choice(balder)
                path='Balder/'
            
            
    #image_file = random.choice(images)
    return render_template('amalia.html', image_file=image_file, path=path)

