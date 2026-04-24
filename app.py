import os
import requests
from flask import Flask, request

app = Flask(__name__)

# YOUR API KEY
API_KEY = "AIzaSyAgfs8vN9iIQe600aTOE-YzRLxrOWxeqfE"
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        user_input = request.form.get('content').lower()
        
        # This is "Mock AI" logic so you have a working prototype NOW
        if "chest" in user_input or "breath" in user_input:
            result = "URGENCY: RED (CRITICAL)<br>Reasoning: Potential cardiac or respiratory distress.<br>Action: Call 999 immediately or go to the nearest ER."
        elif "fever" in user_input or "cough" in user_input:
            result = "URGENCY: YELLOW (MODERATE)<br>Reasoning: Symptoms indicate infection. Monitoring required.<br>Action: Visit a GP within 24 hours."
        else:
            result = "URGENCY: GREEN (LOW)<br>Reasoning: Symptoms appear non-life-threatening.<br>Action: Rest and monitor at home. Visit a clinic if symptoms persist."
    
    return f'''
    <html>
        <head>
            <title>V-Triage | AI Emergency Dept</title>
            <style>
                body {{ font-family: sans-serif; background: #050a10; color: #e0e0e0; padding: 40px; }}
                .console {{ border: 2px solid #00d4ff; border-radius: 15px; padding: 30px; background: #0a1420; }}
                textarea {{ width: 100%; height: 120px; background: #121c2a; color: white; border: 1px solid #00d4ff; padding: 15px; }}
                button {{ background: #00d4ff; color: #050a10; border: none; padding: 15px 30px; cursor: pointer; font-weight: bold; }}
                .report {{ background: #121c2a; border-left: 5px solid #00d4ff; padding: 20px; margin-top: 30px; }}
            </style>
        </head>
        <body>
            <div class="console">
                <h1>HOSPITAL SYSTEM: V-TRIAGE AI</h1>
                <form method="post">
                    <p>DESCRIBE PATIENT SYMPTOMS:</p>
                    <textarea name="content"></textarea><br>
                    <button type="submit">GENERATE TRIAGE REPORT</button>
                </form>
                {f'<div class="report">{result}</div>' if result else ''}
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))