import requests
from evaluacion_ambiental.lib.constans import URL_EVALUACION_AMBIENTAL
from typing import Any, Dict, List, Optional, Tuple
from bs4 import BeautifulSoup
import json
import re
from evaluacion_ambiental.models import Proyectos


def get_data_by_url(url: str):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tbody_tr_items = soup.find_all('tbody')[0].find_all('tr')
    data_list = []
    for item in tbody_tr_items:
        data = {}
        item_td = item.find_all('td')
        data['id_table'] = item_td[0].text
        data['nombre'] = item_td[1].text
        data['tipo'] = item_td[2].text
        data['region'] = item_td[3].text
        data['tipologia'] = item_td[4].text
        data['titular'] = item_td[5].text
        data['inversion'] = item_td[6].text
        data['fecha_presentacion'] = item_td[7].text
        data['estado'] = item_td[8].text
        eva_amb_proyect = create_proyect(data)
        if not eva_amb_proyect:
            break
        data_list.append(data)
    return data_list, eva_amb_proyect


def numbers_page():
    page = requests.get(URL_EVALUACION_AMBIENTAL)
    soup = BeautifulSoup(page.text, 'html.parser')
    RealValue = soup.find("div", {"id":"info_resultado"})
    number_pages = int(''.join( x for x in RealValue.text if x not in ",.\n").split(": ")[-1])
    return number_pages


def creating_json_file_with_data(homepage: int, final_page: int):
    data_file = []
    for page in range(homepage , final_page+1):
        try:
            url = URL_EVALUACION_AMBIENTAL + f"?_paginador_fila_actual={page}"
            #if page == 505:
            #    url = 'xxx'
            print(url)
            data, eva_amb_proyect = get_data_by_url(url)
            if not eva_amb_proyect:
                break
            data_file = data_file + data
        except:
            break
    
    with open("datos.json", "r") as j:
        data = json.load(j)

    last_page = int(data[-1]['id_table'])/10 if data else 0
    if eva_amb_proyect:
        archivo_json = open("datos.json", "w")
        archivo_json.write(json.dumps(data + data_file))
        
    return data_file, page , last_page


def create_proyect(data: Dict[str, Any]) -> Proyectos:
    proyecto = Proyectos.objects.filter(id_table=data.get('id_table')).first()
    if not proyecto:
        eva_amb_proyect = Proyectos(
            id_table=data.get('id_table'),
            nombre=data.get('nombre',''),
            tipo=data.get('tipo',''),
            region=data.get('region'),
            tipologia=data.get('tipologia',''),
            titular=data.get('titular',''),
            inversion=data.get('inversion',''),
            fecha_presentacion=data.get('fecha_presentacion',''),
            estado=data.get('estado','')
        )
        eva_amb_proyect.save()
        return eva_amb_proyect
    return None
