import requests

if __name__ == '__main__':
    url = 'https://lh3.googleusercontent.com/CUyx7p3uqhMvdKeDl6mNb0VIdaqJCzObA8LNE0rRUMxmBTxapZWv64ckfsi0vYR44wPtGes2XEfXvrccK9SxqQ6ykMWT7RkcxdyFoCLqV69BgQ0GmZdQOVroDcJiXfsAr3_vbZi9WDr42YtTQyrM4DG8KVP36uMYN9XD-ExV8_WChLpABBvkNk7dYoaKghxSh-6yAnwGxlaOrK5yZ7-6PaYLEqveQzr_MvsRCcrpPJ1V_UnsWSuohxTTyQPU2zIGlJxXDatAwd-jY3hAyhAGJI6VP2ro85aLPr8oMZtsBMv3IDSBtGq9MGnh1PpvZurlbepZL6QzAh3v4Ghg_8xyKhEi20MayWU6jgwqY9HYso8ypMFKzQiCUvEMnlcwHNd0zPud2WeUGd_qabf_bGnLlhnNta0mqZZuvIokNMEBIHDpg_RpoTK_4uVQ5SPmrgpy69c4QJKe5AwxEQElHNn5x9YfIRIKl9LAY9qcxfzwD3zWDmw2fiyhqG-YFaC9UhuiVKrXhKDDRYUbYEVT8im9bxlfGjvuD4Z5hcHa8ei0tD6SCxeEoe6YBq1-xP5pPM8q_AkprJLSXU1lDKv3PPttJmBg8L-KiDmu7fjQd8iHyE5j2dhsZOsHRvzfwN1GFPRMBH5OKQl859uqnTeZRo_kEnm4qX7Zgeeny0EdJqfxahMcIADm4Lr94TVtbWpVlnGmWu-2DD-M9i0drGbijRdhQxxdRw=w501-h668-no?authuser=0'

    response = requests.get(url, stream=True)
    with open('imagen.jpg', 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)

    response.close()

