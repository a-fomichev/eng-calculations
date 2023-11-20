import os
from flask import Flask, Response, render_template, request
from jinja2 import Template
import markdown
from weasyprint.text.fonts import FontConfiguration
from weasyprint import HTML, CSS

import src.app.calculation as calc
import forms 

# calc.ndm_kz()
# calc.strength_bending_kz()


app = Flask(__name__)


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

CALCULATION_TEMPLATES_DIR = "calculation_templates"
CALC_CONTENT_DESCRIPTION_DIR = "src/markdown/description"
CALC_CONTENT_REPORT_DIR = "src/markdown/report"


strength_calc_list = {'strength_calc_1': ['strength_bending_kz', 'Проверка прочности '],
                      'strength_calc_2': ['strength_bending_kz', 'Проверка прочности-2 '],
                              }

form_list = {'load_wave_standing': 'LoadWaveStanding',
             'strength_bending_kz': 'StrengthBendingKZ'}


def convert_md_to_html(md_file_path, input_data={}, result_data={}):
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        markdown_template = Template(md_file.read())
    # Рендерим Jinja2-шаблон в Markdown
    markdown_content = markdown_template.render(input_data=input_data, result_data=result_data)
    # Создаем экземпляр Markdown-процессора с расширением mdx-math
    md = markdown.Markdown(
        # extensions=[MathExtension(enable_dollar_delimiter=True)]
    )
    # Преобразование Markdown в HTML
    html_content = md.convert(markdown_content)
    return html_content



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc_list')
def calc_list():
    return render_template('calc_list.html',
                           strength_calc_list=strength_calc_list
                           )

@app.route('/strength_calc/<calc_type>', methods=['GET', 'POST'])
def strength_calc(calc_type):
    form = getattr(forms, form_list.get(calc_type))()
    form_description = convert_md_to_html(f"{CALC_CONTENT_DESCRIPTION_DIR}/{calc_type}_description.md")

    if form.validate_on_submit():
        input_data = request.form  # чтение результатов ввода
        calculations_func = getattr(calc, calc_type)
        result_data = calculations_func(input_data)
        report_flag = True
        # print(input_data)
        # print(result_data)
        form_report = convert_md_to_html(f"{CALC_CONTENT_REPORT_DIR}/{calc_type}_report.md", input_data=input_data,
                                         result_data=result_data)
        return render_template(f"{CALCULATION_TEMPLATES_DIR}/{calc_type}.html",
                               form=form,
                               report_flag=report_flag,
                               form_description=form_description,
                               form_report=form_report
                               )
    report_flag = False
    input_data = {}

    return render_template(f"{CALCULATION_TEMPLATES_DIR}/{calc_type}.html",
                           form=form,
                           report_flag=report_flag,
                           input_data=input_data,
                           form_description=form_description
                           )


@app.route('/save_rendered_html', methods=['POST'])
def save_rendered_html():
    data = request.get_json()
    html_content = data.get('html', '')

    rendered_html = render_template('report.html', html_content=html_content)

    font_config = FontConfiguration()

    html = HTML(string=rendered_html)
    css = CSS(filename='static/css/style_report.css', font_config=font_config)

    pdf = html.write_pdf(stylesheets=[css], font_config=font_config)

    response = Response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'

    return response



if __name__ == '__main__':
    # settings=setings()
    app.run(debug=True)