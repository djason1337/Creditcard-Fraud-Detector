from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def grab_ip():
    response = requests.get("https://api.ipify.org/")
    if response.status_code == 200:
        public_ip = response.text.strip()
    else:
        public_ip = "Error retrieving IP"
    return public_ip

def get_location(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    


ip_address = grab_ip()
location_data = get_location(ip_address)

@app.route('/')
def index():
    response = requests.get("https://api.ipify.org/")
    if response.status_code == 200:
        public_ip = response.text.strip()
    else:
        public_ip = "Error retrieving IP"
    return render_template('index.html', ip_address=public_ip, country=location_data['country'], region=location_data['region'], city=location_data['city'])

@app.route('/', methods=['POST'])
def post_fraudscore():
    threshold = 30
    score = 0
    if request.method == 'POST':
        city = request.form.get('city')
        billing_street = request.form.get('street')
        shipping_street = request.form.get('shipStreet')
        billing_zip = request.form.get('zip')
        shipping_zip = request.form.get('shipZip')
        print(shipping_street)
        print(billing_street)
        
        if location_data and 'city' in location_data:
            user_city = city.upper()
            ip_city = location_data['city'].upper()
            if user_city == ip_city:
                score += 0
            else:
                score += 30
        print(score)
        if billing_street == shipping_street:
            score += 0
        else:
            score += 30
        print(score)

        if billing_zip == shipping_zip:
            score += 0
        else:
            score += 30

    if score >= threshold:
        return render_template('failed.html')
    else:
        return render_template('success.html')



if __name__ == '__main__':
    app.run(debug=True)