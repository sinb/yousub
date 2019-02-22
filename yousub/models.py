import os
import urllib.request
import xml.etree.ElementTree as ET

from .tools import seconds_to_srt_time


class YouSub:
    LANG_URL = 'https://video.google.com/timedtext?type=list&v=%s'
    SUBTITLE_URL = "https://video.google.com/timedtext?hl=%s&lang=%s&name=&v=%s"

    @classmethod
    def get_lang_codes_list(cls, vid):
        url = cls.LANG_URL % vid
        root = cls.parse_xml_from_url(url)
        codes = []
        for child in root:
            codes.append(child.attrib['lang_code'])
        return codes

    @classmethod
    def get_subtitle_by_lang_code(cls, code, vid, type='srt', directory=None):
        url = cls.SUBTITLE_URL % (code, code, vid)
        directory = directory or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if type == 'srt':
            root = cls.parse_xml_from_url(url)
            str_data = cls.xml_to_srt(root)
            cls.write_file(directory, vid + '.srt', str_data)

    @staticmethod
    def parse_xml_from_url(url):
        with urllib.request.urlopen(url) as response:
            xml = response.read()
            root = ET.fromstring(xml)
        return root

    @staticmethod
    def xml_to_json():
        pass

    @staticmethod
    def xml_to_srt(root):
        subtitle_data = []
        line = 1
        for child in root:
            subtitle_data.append({
                "line": line,
                "text": child.text,
                "start": child.attrib['start'],
                "dur": child.attrib['dur']
            })
            line += 1

        srt_line = []
        for item in subtitle_data:
            srt_line.append(
                "{}\n{} --> {}\n{}\n\n".format(item['line'],
                                               seconds_to_srt_time(item['start']),
                                               seconds_to_srt_time("%.3f" % (float(item['start']) + float(item['dur']))),
                                               item['text']))
        return "".join(srt_line)

    @staticmethod
    def save_xml(url, directory):
        pass

    @staticmethod
    def write_file(directory, filename, str_data):
        with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
            f.write(str_data)
