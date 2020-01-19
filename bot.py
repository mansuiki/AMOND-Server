import random
from datetime import datetime

import requests


class BotData:
    NAME = "pyBot"
    VERSION = "Beta 0.1"
    DEVELOPER = "mansuiki"


def listener(request):
    room = request['Room']
    sender = request['Sender']
    msg = request['Message'].lstrip()
    result = ""

    if msg[0] == '/':
        blank = msg.find(" ")
        if blank == -1:
            func = msg[1:]
            msg = ""
        else:
            func = msg[1:blank]
            msg = msg[blank + 1:]

        if func == 'help':
            result = help(room, sender, msg)
        elif func == 'info':
            result = info(room, sender, msg)
        elif func == '따라하기':
            result = echo(room, sender, msg)
        elif func == '파싱':
            result = parse(room, sender, msg)
        elif func == '날씨':
            result = weather(room, sender, msg)
        elif func == '호출':
            result = call(room, sender, msg)
        elif func == '번역':
            result = translate(room, sender, msg)
        elif func == '시간':
            result = time(room, sender, msg)
        elif func == '날짜':
            result = date(room, sender, msg)
        elif func == '주사위':
            result = dice(room, sender, msg)
        elif func == '미세먼지':
            result = air(room, sender, msg)
        elif func == '검색':
            result = search(room, sender, msg)
        else:
            result = '지원되지 않는 명령어입니다.'

    else:
        result = ""

    return {"Result": result}


def help(room, sender, msg):
    if msg == "":
        result = "숭실봇 많이 사랑해주세요.\n" + \
                 "\n<<명령어 목록>>\n" + \
                 " /help [추가명령어] : 도움말을 출력합니다." + \
                 " /따라하기 [따라할말] : 해당 말을 따라합니다.\n" + \
                 " /파싱 [url] : 해당 웹페이지의 소스를 긁어옵니다.\n" + \
                 " /날씨 : 전국 날씨를 띄웁니다.\n" + \
                 " /호출 : 토스트 메시지를 이용하여 개발자를 부릅니다.\n" + \
                 " /번역 [언어코드1] [언어코드2] [내용] : 해당 내용을 번역합니다.\n" + \
                 " /시간 : 현재 시간을 출력합니다.\n" + \
                 " /날짜 : 현재 날짜를 출력합니다.\n" + \
                 " /주사위 : 랜덤으로 주사위를 던집니다.\n" + \
                 " /미세먼지 : 현재 전국 미세먼지 현황을 띄웁니다.\n" + \
                 " /검색 [내용] : 해당 내용을 검색합니다.\n" + \
                 " /on : 봇을 활성화시킵니다.\n" + \
                 " /off : 봇을 비활성화시킵니다.\n" + \
                 " /info : 봇 정보를 띄웁니다.\n" + \
                 " /help : 도움말을 띄웁니다."
    else:
        if msg == "echo":
            result = "help for echo"
        else:
            result = "지원되지 않는 명령어입니다."

    return result


def info(room, sender, msg):
    result = "숭실봇 많이 사랑해주세요.\n봇 이름 : " + BotData.NAME + "\n버전 : " + BotData.VERSION + \
             "\n제작자 : " + BotData.DEVELOPER + "\n\n라이선스 : GPL 3.0"
    return result


def echo(room, sender, msg):
    result = msg
    return result


def parse(room, sender, msg):
    try:
        result = '파싱 결과입니다.\n' + requests.get(msg, timeout=0.1).text
    except requests.exceptions.Timeout:
        result = '주소에 접속할 수 없습니다.'
    except Exception as e:
        result = '주소를 정확히 입력해주세요.\n' + '예시) https://github.com/mansuiki'
        print(e)

    return result


def weather(room, sender, msg):
    return '구현중'


def call(room, sender, msg):
    return '구현중'


def translate(room, sender, msg):
    return '구현중'


def time(room, sender, msg):
    now = datetime.now()
    result = "지금은 " + str(now.hour) + "시 " + str(now.minute) + "분 " + str(now.second) + "초입니다."
    return result


def date(room, sender, msg):
    now = datetime.now()
    result = "오늘은 " + str(now.month) + "월 " + str(now.day) + "일입니다."
    return result


def dice(room, sender, msg):
    icon = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    return random.choice(icon)


def air(room, sender, msg):
    return '구현중'


def search(room, sender, msg):
    msg = msg.strip.replace(" ", "%20")
    result = "네이버 검색 결과입니다.\nhttps://m.search.naver.com/search.naver?query=" + msg
    return result
