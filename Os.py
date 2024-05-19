import requests
import sys

def generate_content(input_text):
    headers = {'Content-Type': 'application/json'}
    payload = {
            "contents": [{"parts": [{"text": " only work if I an talking about bash commands in linux operating systems if any type else of qustions display Genie only for linux commands  :"+ input_text  }]}]
    }
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyA_15REqsvDbG_GuTxux4mCltcYwJmuOAQ'
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
        return data
    else:
        print("Error:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = sys.argv[1]
        generated_content = generate_content(input_text)
        if generated_content:
            print(generated_content)
    else:
        print("Usage: python G.py <input_text>")

