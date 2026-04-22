from flask import Flask, render_template, request
from crew import legal_assistant_crew 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_query():
    user_question = request.form['legal_query']
    
    result = legal_assistant_crew.kickoff(inputs={'user_input': user_question})
    
    # THIS IS THE CORRECTED LINE:
    formatted_result = result.raw.replace('\n', '<br>')
    
    return render_template('result.html', result=formatted_result)

if __name__ == "__main__":
    app.run(debug=True, port=5001)