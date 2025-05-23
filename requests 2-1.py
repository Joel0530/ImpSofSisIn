import requests 
import shutil
import json
class llamadasininternet():
    def primer_request():
        url = 'https://terraria.fandom.com/es/wiki/Wiki_Terraria'
        r = requests.get('https://terraria.fandom.com/es/wiki/Wiki_Terraria')
        print(r)
        print(r.content)
        print(r.status_code)

    def imagen(self,url,file_name):
        
        res = requests.get(url,stream=True)
        if 200==res.status_code:
            with open(file_name,'wb')as f:
                shutil.copyfileobj(res.raw,f)
            print('imagen descargada correctamente')
        else:
            print('no se encontro la imagen')



def clima(self,api_key,city):
    
    base_url = 'https//api.openweathermap.org/daba/2.5/weather?'
    params ={'q':city,'appid:':api_key,'units':'metric'}
    
    try:
        
        r=requests.get(base_url,perams=params)
        r.raise_for_status()
        weathwer_data = r.json()
        if 200==weathwer_data['cod']:
            print(f'El clima en{weathwer_data['name']}:')
            print(f'Descripcion{weathwer_data['weather'][0]['description']}')
            print(f'Temperatura{weathwer_data['main']['temp']}°c')
            print(f'Humedad{weathwer_data['main']['Humidity']}%')
            print(f'Viento{weathwer_data['wind']['speed']}m/s')
        else:
            print(f'Error{weathwer_data['message']}')
    except:
        print('Error')







req = llamadasininternet()
req.imagen(url,'señor.jpg')
api_key = '69ec8ca2037d63a120d31c59efd0f604'
city = 'zapopan'
url = 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/7877295eb0bc45fb6856ee0e2e8a66bb~tplv-tiktokx-cropcenter:1080:1080.jpeg?dr=14579&refresh_token=aff43f42&x-expires=1748206800&x-signature=fZBjxgt%2BJeaYKJMMgYrq2CG8crw%3D&t=4d5b0474&ps=13740610&shp=a5d48078&shcp=81f88b70&idc=maliva'
