from datetime import datetime as dt
import xml.etree.ElementTree as ET
import requests
import pandas as pd


class ApiBaseClass:
    def _load_data(self, url: str) -> [{str: str}]:
        response = requests.get(url)
        xml_string = response.content.decode('utf-8')
        root = ET.fromstring(xml_string)
        return [elm.attrib for elm in root]

    def _load_kv_style_data(self, url: str) -> {str: str}:
        response = requests.get(url)
        xml_string = response.content.decode('utf-8')
        root = ET.fromstring(xml_string)
        return {elm.tag: elm.text for elm in list(root)}

    def _load_nested_data(self, url: str) -> {str: {str: str}}:
        response = requests.get(url)
        xml_string = response.content.decode('utf-8')
        root = ET.fromstring(xml_string)
        return {
            elm.tag: {
                child.attrib['id']: child.text
                for child in list(elm)
            } for elm in list(root)
        }

    def _load_data_as_df(self, url: str) -> pd.DataFrame:
        data = self._load_data(url)
        return pd.DataFrame(data)


def nowstr():
    return dt.now().strftime('%Y%m%d_%H%M%S_%f')
