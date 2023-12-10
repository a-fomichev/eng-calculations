import os
from tempfile import NamedTemporaryFile

import os
from flask import Flask, Response, render_template, request, send_file
from jinja2 import Template
import pdfkit
import markdown
from weasyprint.text.fonts import FontConfiguration
from weasyprint import HTML, CSS

import src.app.calculation as calc
import forms 

app = Flask(__name__)


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

CALCULATION_TEMPLATES_DIR = "calculation_templates"
CALC_CONTENT_DESCRIPTION_DIR = "static/markdown/description"
CALC_CONTENT_REPORT_DIR = "static/markdown/report"


strength_checks_kz_list = {'calc_1': ['strength_kz_bending_sp41', 'Проверка прочности изгибаемого железобетонного элемента','КЖ-1','СП 41.13330.2012'],
                      'calc_2': ['strength_kz_bending_sp41', 'Проверка прочности изгибаемого железобетонного элемента','КЖ-2','СП 41.13330.2012'],
                      'calc_3': ['strength_kz_bending_sp41', 'Проверка прочности изгибаемого железобетонного элемента','КЖ-3','СП 41.13330.2012'],
                              }

form_list = {'load_wave_standing': 'LoadWaveStanding',
             'strength_kz_bending_sp41': 'StrengthBendingKZ'}


def convert_md_to_html(md_file_path,report_data={}):
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        markdown_template = Template(md_file.read())
    # Рендерим Jinja2-шаблон в Markdown
    markdown_content = markdown_template.render(report_data=report_data)
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
                           strength_checks_kz_list=strength_checks_kz_list
                           )

@app.route('/<calc_type>', methods=['GET', 'POST'])
def calculation(calc_type):
    form = getattr(forms, form_list.get(calc_type))()
    form_description = convert_md_to_html(f"{CALC_CONTENT_DESCRIPTION_DIR}/{calc_type}_description.md")

    if form.validate_on_submit():
        input_data = request.form  # чтение результатов ввода
        calculations_func = getattr(calc, calc_type)
        result_data = calculations_func(input_data)
        report_data=input_data|result_data
        report_flag = True

        form_report = convert_md_to_html(f"{CALC_CONTENT_REPORT_DIR}/{calc_type}_report.md", report_data=report_data)
        return render_template(f"{CALCULATION_TEMPLATES_DIR}/{calc_type}.html",
                               form=form,
                               report_flag=report_flag,
                               form_description=form_description,
                               form_report=form_report,
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
    style = data.get('style', '')
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    rendered_html = render_template('report.html', html_content=html_content, style=style)

    # with open('rendered_template.html', 'w', encoding='utf-8') as file:
    #     file.write(rendered_html)


    temp_file = NamedTemporaryFile(suffix='.pdf')
    pdfkit.from_string(rendered_html, temp_file.name, configuration=config, verbose=True)
    return send_file(temp_file.name, as_attachment=False, mimetype='application/pdf')
    # pdf=pdfkit.from_url('https://stackoverflow.com/questions/33705368/unable-to-find-wkhtmltopdf-on-this-system-the-report-will-be-shown-in-html', configuration = config)
    # return Response(pdf, mimetype='application/pdf')




if __name__ == '__main__':
    # settings=setings()
    app.run(debug=True)





# @app.route('/save_rendered_html', methods=['POST'])
# def save_rendered_html():
#     data = request.get_json()

#     html_content = data.get('html', '')
#     style=data.get('style','')

#     rendered_html = render_template('report.html', html_content=html_content, style=style)
#     # Сохранение rendered_html в файл
#     # with open('rendered_template.html', 'w', encoding='utf-8') as file:
#     #     file.write(rendered_html)
#     font_config = FontConfiguration()
#     html = HTML(string=rendered_html)

#     # css = CSS(
#     #     # string='@page { size: A4; margin: 1cm }',
#     #     # string=style,
#     #     filename='static/css/style2.css',
#     #     font_config=font_config
#     # )

#     pdf = html.write_pdf(
#         # stylesheets=[css],
#         font_config=font_config
#         )
    
#     response = Response(pdf)
#     response.headers['Content-Type'] = 'application/pdf'
#     response.headers['Content-Disposition'] = 'attachment; filename=output.pdf'
    
#     return response



# @app.route('/get_pdf/<calc_type>', methods=['POST'])
# def get_pdf(calc_type):
#     form = getattr(forms, form_list.get(calc_type))()

#     if form.validate_on_submit():
#         input_data = request.form  # чтение результатов ввода
#         calculations_func = getattr(strength_calculations, calc_type)
#         result_data = calculations_func(input_data)
#         form_report = convert_md_to_html(f"{CALC_CONTENT_REPORT_DIR}/{calc_type}_report.md",
#                                          input_data=input_data,
#                                          result_data=result_data)

#         path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
#         config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
#         options = {
#             'page-size': 'A4',
#             'javascript-delay': '5000',
#             'margin-top': '3.0cm',
#             'encoding': 'utf-8'
#         }
#         rendered = render_template('report.html', form_report=form_report)       
#         css = ['static/css/style.css']
#         pdf = pdfkit.from_string(rendered,
#                                  configuration=config,
#                                  options=options,
#                                  verbose=True,
#                                  css=css
#                                  )
#         return Response(pdf, mimetype='application/pdf')