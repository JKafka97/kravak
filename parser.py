import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_obsazenost_value(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        obsazenost_element = soup.find(string='Obsazenost:')

        if obsazenost_element:
            p_tag = obsazenost_element.find_next('p')

            if p_tag:
                value = obsazenost_element.parent.contents[1].get_text(strip=True)
                return value
            else:
                print('No <p> tag found next to "Obsazenost"')
        else:
            print('"Obsazenost" not found on the page')
    else:
        print(f'Failed to retrieve the page. Status code: {response.status_code}')

    return None

def save_data_to_file(value, output_file):
    if value is not None:
        current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_to_write = f'{current_datetime};{value}\n'

        with open(output_file, 'a') as file:
            file.write(data_to_write)

if __name__ == "__main__":
    url = 'https://www.kravihora-brno.cz/kryta-plavecka-hala'
    output_file = './output.csv'

    obsazenost_value = get_obsazenost_value(url)
    save_data_to_file(obsazenost_value, output_file)
