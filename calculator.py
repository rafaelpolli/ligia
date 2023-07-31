from flask import Flask, render_template, request
import ligia

Flask_App = Flask(__name__) # Creating our Flask Instance

@Flask_App.route('/', methods=['GET'])
def index():
    """ Displays the index page accessible at '/' """

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """Route where we send calculator form input"""

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= " 
    first_input = request.form['Input1']  
    operation = request.form['operation']

    try:
        input1 = str(first_input)

        result = ligia.consulta(assunto = operation, question = first_input)

        return render_template(
            'index.html',
            input1=input1,
            operation=operation,
            table=result,
            calculation_success=True
        )
    
        
    except:
        pass


if __name__ == '__main__':
    Flask_App.debug = True
    Flask_App.run()
