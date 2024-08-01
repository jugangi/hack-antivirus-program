from flask import Flask, render_template

app = Flask(__name__)

# 해킹 기법과 백신 프로그램에 대한 정보
hacking_methods = {
    "웹 해킹": {
        "description": "웹 사이트나 웹 애플리케이션의 취약점을 이용하여 침입하고, 사용자 정보를 탈취하거나 시스템을 제어하는 공격",
        "example": "2017년에 발생한 Equifax 데이터 침해 사고는 SQL 인젝션 공격으로 유명한 사례입니다. 해커는 Equifax의 웹 응용 프로그램에서 취약점을 이용하여 약 1억 4700만 명의 개인 정보를 탈취했습니다."
    },
    "시스템 해킹": {
        "description": "운영체제 또는 네트워크 시스템에 대한 침입을 목표로 하는 해킹",
        "example": "2017년 발생한 WannaCry 공격은 시스템 해킹과 랜섬웨어 공격을 결합한 사례입니다. 악성코드가 전 세계적으로 퍼져 수백만 대의 컴퓨터 시스템을 감염시키고, 파일을 암호화한 후 비트코인으로 금전 보상을 요구했습니다."
    },
    "소셜 엔지니어링": {
        "description": "사람들의 신뢰를 이용하여 정보를 얻거나 시스템에 침입하는 공격",
        "example": "2016년에 발생한 DNC 해킹 사건은 소셜 엔지니어링 기술을 활용한 사례로 알려져 있습니다. 해커는 위장 이메일을 사용하여 미국 민주당의 고위 관계자들을 속여 개인 정보와 이메일을 탈취했습니다."
    },
    "애플리케이션 해킹": {
        "description": "특정 소프트웨어나 애플리케이션의 취약점을 이용하여 공격",
        "example": "2015년, 이탈리아에서 유명한 해킹 팀인 Hacking Team의 데이터가 유출되었습니다. 해당 데이터에는 Adobe Flash Player의 취약점을 악용한 해킹 기술과 관련된 정보가 포함되어 있었고, 해커들은 이 취약점을 이용하여 악성 코드를 실행하고 원격으로 시스템을 제어할 수 있었습니다."
    },
    "네트워크 해킹": {
        "description": "네트워크 인프라에 대한 공격",
        "example": "2010년에 발견된 Stuxnet 웜은 산업 시설을 대상으로 한 네트워크 해킹의 대표적인 사례입니다. 이 웜은 이란의 핵 프로그램을 공격하기 위해 개발되었으며, SCADA 시스템을 통해 제어되는 중요한 산업 시설을 감염시킴으로써 시스템을 파괴하거나 조작했습니다."
    }
}

antivirus_programs = {
    "AhnLab V3 Internet Security": {
        "description": "한국 대표 백신 프로그램. 악성코드 탐지 및 제거 성능이 우수. 경량화된 엔진으로 시스템 자원 사용량이 적음.",
        "image": "images/ahnlab_v3.jpg"
    },
    "Kaspersky Anti-Virus": {
        "description": "높은 악성코드 탐지율. 실시간 보호 기능 강력. 시스템 부하가 상대적으로 큼.",
        "image": "images/kaspersky_antivirus.jpg"
    },
    "Norton AntiVirus": {
        "description": "오랜 역사를 가진 글로벌 제품. 강력한 바이러스 및 멀웨어 차단 기능. 자동 업데이트와 사용자 친화적 인터페이스.",
        "image": "images/norton_antivirus_global.jpg"
    },
    "McAfee AntiVirus": {
        "description": "널리 사용되는 글로벌 브랜드. 다양한 보안 기능 통합. 다소 무거운 시스템 리소스 사용.",
        "image": "images/mcafee.jpg"
    },
    "Bitdefender Antivirus": {
        "description": "뛰어난 악성코드 탐지 및 제거 능력. 가벼운 시스템 부하. 사용자 친화적인 인터페이스.",
        "image": "images/bitdefender.jpg"
    },
    "Avast Free Antivirus": {
        "description": "무료 버전으로 인기가 많음. 높은 탐지율과 실시간 보호 기능. 광고와 팝업이 많음.",
        "image": "images/avast.jpg"
    },
    "AVG AntiVirus": {
        "description": "무료 및 유료 버전 제공. 견고한 바이러스 및 멀웨어 탐지 기능. 시스템 부하가 적음.",
        "image": "images/avg.jpg"
    },
    "Trend Micro Antivirus": {
        "description": "클라우드 기반 보호 기능. 높은 악성코드 탐지율. 때때로 시스템 성능 저하 발생.",
        "image": "images/trend_micro.jpg"
    },
    "ESET NOD32 Antivirus": {
        "description": "가벼운 시스템 부하. 빠르고 정확한 악성코드 탐지. 간편한 설치 및 관리.",
        "image": "images/eset_nod32.jpg"
    },
    "Sophos Home": {
        "description": "강력한 웹 보호 기능. 다양한 디바이스 관리 가능. 무료로 사용 가능하지만 고급 기능은 유료.",
        "image": "images/sophos_home.jpg"
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hacking_methods')
def show_hacking_methods():
    return render_template('hacking_methods.html', methods=hacking_methods)

@app.route('/hacking_method/<method_name>')
def show_hacking_method(method_name):
    method_info = hacking_methods.get(method_name, {})
    return render_template('hacking_method_detail.html', method_name=method_name, method_info=method_info)

@app.route('/antivirus_programs')
def show_antivirus_programs():
    return render_template('antivirus_programs.html', programs=antivirus_programs)

@app.route('/antivirus_program/<program_name>')
def show_antivirus_program(program_name):
    program_info = antivirus_programs.get(program_name, {})
    return render_template('antivirus_program_detail.html', program_name=program_name, program_info=program_info)

if __name__ == "__main__":
    app.run(debug=True)
