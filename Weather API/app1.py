from flask import Flask, url_for, render_template
import requests, os


app = Flask(__name__)
# app.secret_key = "sk1"
#api_key = "97146f0f088483ce0496138e69c7da58"


@app.route('/', methods = ['GET'])
def home():
    construct_url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=" + "97146f0f088483ce0496138e69c7da58"
    response = requests.get(construct_url)
    list_of_data = response.json()

    html_data = f"""
    <table border="1">
    <tr>
        <td>country_code</td>
        <td>coordinate</td>
        <td>temp</td>
        <td>pressure</td>
        <td>humidity</td>
    </tr>
    <tr>
        <td>{str(list_of_data['sys']['country'])}</td>
        <td>{str(list_of_data['coord']['lon']) + ' ' 
                    + str(list_of_data['coord']['lat'])}</td>
        <td>{str(list_of_data['main']['temp']) + 'k'}</td>
        <td>{str(list_of_data['main']['pressure'])}</td>
        <td>{str(list_of_data['main']['humidity'])}</td>
    </tr>

    </table>
    """
    return html_data

if __name__ == '__main__':
    app.run(debug=True)