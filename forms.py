from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, SelectField, FormField, Field, Form
from wtforms.validators import DataRequired, InputRequired, NumberRange, Length, ValidationError

FROM_CLASS = 'form__input'
CHECK_CLASS = 'form__check'


class LoadWaveStanding(Form):
    h = FloatField("h:", validators=[InputRequired(), NumberRange(min=1)])
    lam = FloatField("lambda:", validators=[InputRequired(), NumberRange(min=1)])
    h_sur = FloatField("h_sur:", validators=[InputRequired(), NumberRange(min=1)])
    lam_sur = FloatField("lambda_sur:", validators=[InputRequired(), NumberRange(min=0)])
    d_cr = FloatField("d_cr:", validators=[InputRequired(), NumberRange(min=0)])
    d_f = FloatField("d_f:", validators=[InputRequired(), NumberRange(min=0)])
    d_br = FloatField("d_br:", validators=[InputRequired(), NumberRange(min=0)])
    d_b = FloatField("d_b:", validators=[InputRequired(), NumberRange(min=0)])


class Form_2(Form):
    x = IntegerField("x:", validators=[DataRequired()])
    y = IntegerField("y:", validators=[DataRequired()])


class CoefficientSP58(Form):
    gamma_n = FloatField("Коэффициент надежности",
                         validators=[
                             InputRequired(
                                 message='Это поле обязательно к заполнению'
                             ),
                             NumberRange(
                                 min=1.0,
                                 max=1.25,
                                 message="Введите число в интервале от 1 до 1.25"
                             )
                         ],
                         render_kw={
                             'symbol': "&gamma; <sub>n</sub>",
                             'prefix': '',
                             'unit': '',
                             'field_size': 'small',
                             'placeholder': '1',
                             'title': "Согласно п. 8.17 СП 58.13330",
                         }
                         )
    gamma_lc = FloatField("Коэффициент сочетания нагрузок",
                          validators=[
                              InputRequired(
                                  message='Это поле обязательно к заполнению'
                              ),
                              NumberRange(
                                  min=0.5,
                                  max=2,
                                  message="Введите число в интервале от 0.5 до 2"
                              )
                          ],
                          render_kw={
                              'symbol': "&gamma; <sub>lc</sub>",
                              'prefix': '',
                              'unit': '',
                              'field_size': 'small',
                              'placeholder': '1',
                              'title': "Согласно п. 8.17 СП 58.13330",
                          }
                          )
    gamma_c = FloatField("Коэффициент условий работы сооружения",
                         validators=[
                             InputRequired(
                                 message='Это поле обязательно к заполнению'
                             ),
                             NumberRange(
                                 min=0.1,
                                 max=2,
                                 message="Введите число в интервале от 0.1 до 2"
                             )
                         ],
                         render_kw={
                             'symbol': "&gamma;<sub>c</sub>",
                             'prefix': '',
                             'unit': '',
                             'field_size': 'small',
                             'placeholder': '1',
                             'title': "Принимается по строительным нормам и правилам на отдельные виды сооружений",

                         }
                         )


class CoefficientSP41(Form):
    gamma_b = FloatField("Коэффициент условий работы бетона",
                         validators=[
                             InputRequired(
                                 message='Это поле обязательно к заполнению'
                             ),
                             NumberRange(
                                 min=0.45,
                                 max=2,
                                 message="Введите число в интервале от 0.45 до 2"
                             )
                         ],
                         render_kw={
                             'symbol': "&gamma; <sub>b</sub>",
                             'prefix': '',
                             'unit': '',
                             'field_size': 'small',
                             'placeholder': '1',
                             'title': "Принимается по таблице 5 СП 41.13330",
                         }
                         )
    gamma_s = FloatField("Коэффициент условий работы арматуры",
                         validators=[
                             InputRequired(
                                 message='Это поле обязательно к заполнению'
                             ),
                             NumberRange(
                                 min=0.45,
                                 max=1.1,
                                 message="Введите число в интервале от 0.45 до 1.1"
                             )
                         ],
                         render_kw={
                             'symbol': "&gamma; <sub>s</sub>",
                             'prefix': '',
                             'unit': '',
                             'field_size': 'small',
                             'placeholder': '1',
                             'title': "Принимается по таблице 13 СП 41.13330",
                         }
                         )


class SectionGeometric(Form):
    section_height = FloatField("Высота сечения",
                                validators=[
                                    InputRequired(
                                        message='Это поле обязательно к заполнению'
                                    ),
                                    NumberRange(
                                        min=0.001,
                                        message="Введите число больше 0"
                                    )
                                ],
                                render_kw={
                                    'symbol': "h",
                                    'prefix': '',
                                    'unit': 'м',
                                    'field_size': 'small',
                                    'placeholder': '1',
                                    'title': "Высота сечения в м",
                                }
                                )
    section_width = FloatField("Ширина сечения",
                               validators=[
                                   InputRequired(
                                       message='Это поле обязательно к заполнению'
                                   ),
                                   NumberRange(
                                       min=0.001,
                                       message="Введите число больше 0"
                                   )
                               ],
                               render_kw={
                                   'symbol': "b",
                                   'prefix': '',
                                   'unit': 'м',
                                   'field_size': 'small',
                                   'placeholder': '1',
                                   'title': "Ширина сечения в м",
                               }
                               )


class Reinforcement(Form):
    reinforcement_diameter = SelectField("Диаметр арматуры",
                                         choices=[(4, "4"),
                                                  (5, "5"),
                                                  (6, "6"),
                                                  (8, "8"),
                                                  (10, "10"),
                                                  (12, "12"),
                                                  (14, "14"),
                                                  (16, "16"),
                                                  (18, "18"),
                                                  (20, "20"),
                                                  (22, "22"),
                                                  (25, "25"),
                                                  (28, "28"),
                                                  (32, "32"),
                                                  (36, "36"),
                                                  (40, "40")],
                                         render_kw={
                                             'symbol': '',
                                             'prefix': '',
                                             'unit': 'мм',
                                             'field_size': 'small',
                                             'title': "Диаметр стержней"
                                         }
                                         )
    reinforcement_number = IntegerField("Число стержней растянутой арматуры",
                                        validators=[
                                            InputRequired(
                                                message='Это поле обязательно к заполнению'
                                            ),
                                            NumberRange(
                                                min=1,
                                                message="Кол-во стержней должно быть больше 0"
                                            )
                                        ],
                                        render_kw={
                                            'symbol': '',
                                            'prefix': '',
                                            'unit': '',
                                            'field_size': 'small',
                                            'placeholder': '5',
                                            'title': "Количество стержней"
                                        }
                                        )
    reinforcement_area = FloatField("Площадь арматуры",
                                    validators=[
                                        InputRequired(
                                            message='Это поле обязательно к заполнению'
                                        ),
                                        NumberRange(
                                            min=0.001,
                                            message="Значение площади должно быть больше 0"
                                        )
                                    ],
                                    render_kw={
                                        'symbol': 'A',
                                        'prefix': '',
                                        'unit': 'см2',
                                        'field_size': 'medium',
                                        'title': "Общая площадь арматуры в см2",
                                    }
                                    )
    protective_layer = FloatField("Защитный слой",
                                  validators=[
                                      InputRequired(
                                          message='Это поле обязательно к заполнению'
                                      ),
                                      NumberRange(
                                          min=0,
                                          message="Введите число больше 0"
                                      )
                                  ],
                                  render_kw={
                                      'symbol': 'a',
                                      'prefix': '',
                                      'unit': 'мм',
                                      'field_size': 'small',
                                      'placeholder': '40',
                                      'title': "Толщина защитного слоя в м",
                                  }
                                  )


class ReinforcementClass(Form):
    class_reinforcement = SelectField("Класс арматуры",
                                      choices=[
                                          ("A240", "A240"),
                                          ("A300", "A300"),
                                          ("A400", "A400"),
                                          ("A500", "A500"),
                                          ("A600", "A600")
                                      ],
                                      render_kw={
                                          'symbol': '',
                                          'prefix': '',
                                          'unit': '',
                                          'field_size': 'medium',
                                      }
                                      )


class ConcreteClass(Form):
    class_concrete = SelectField("Класс бетона",
                                 choices=[
                                     ("B10", "B10"),
                                     ("B12.5", "B12.5"),
                                     ("B15", "B15"),
                                     ("B20", "B20"),
                                     ("B25", "B25"),
                                     ("B30", "B30"),
                                     ("B35", "B35"),
                                     ("B40", "B40"),
                                     ("B45", "B45"),
                                     ("B50", "B50"),
                                 ],
                                 render_kw={
                                     'symbol': '',
                                     'prefix': '',
                                     'unit': '',
                                     'field_size': 'medium',
                                 }
                                 )


class Loads(Form):
    bending_moment = FloatField("Изгибающий момент",
                                validators=[
                                    InputRequired(
                                        message='Это поле обязательно к заполнению'
                                    ),
                                    NumberRange(
                                        min=0,
                                        message="Введите число больше 0"
                                    )
                                ],
                                render_kw={
                                    'symbol': "M",
                                    'prefix': '',
                                    'unit': 'кНм',
                                    'field_size': 'medium',
                                    'placeholder': '100',
                                    'title': "Абсолютное значение изгибающего момента",
                                }
                                )


class StrengthBendingKZ(FlaskForm, ReinforcementClass, ConcreteClass, SectionGeometric, CoefficientSP58,
                        CoefficientSP41, Loads):
    s = FormField(Reinforcement,
                  separator="_",
                  label="Растянутая арматура"
                  )
    sc = FormField(Reinforcement,
                   separator="_",
                   label="Сжатая арматура"
                   )
