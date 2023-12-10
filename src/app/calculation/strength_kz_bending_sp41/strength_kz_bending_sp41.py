import json
import os
import matplotlib.pyplot as plt
import base64
import io
import matplotlib

matplotlib.use('Agg')  # Или 'TkAgg'

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../../reference_data/concrete_data.json')), "r", encoding="utf-8") as data_c:
    concrete_data = json.load(data_c)

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../../reference_data/reinforcement_data.json')), "r", encoding="utf-8") as data_r:
    reinforcement_data = json.load(data_r)

# os.path.abspath(__file__)


def plot_fig(x, y):
    plt.plot(x, y)
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    fig = base64.b64encode(buffer.getvalue()).decode('utf8')
    return fig



def compressed_zone(ys, yb, r_s, a_s, r_sc, a_sc, r_b, b):
    x = (ys * (r_s * 1000) * a_s / 10000 - ys * (r_sc * 1000) * a_sc / 10000) / (yb * (r_b * 1000) * b)
    return x


def limit_compressed_zone(h0):
    eps_b2 = 0.0035
    eps_s_el = 0.0023
    zeta_r = 0.8 * (1 + eps_s_el / eps_b2)
    zeta_x = zeta_r * h0
    return zeta_x


def strength_test_1(yn, ylc, yc, ys, r_s, a_s, h0, pl_sc, m):
    left_side = yn * ylc * m
    right_side = yc * ys * (r_s * 1000) * (a_s / 10000) * (h0 - pl_sc)
    output = {'strength_condition': right_side > left_side,
              'left_side': left_side,
              'right_side': right_side,
              }
    return output


def strength_test_2(yn, ylc, yc, yb, ys, r_b, r_sc, b, a_sc, pl_s, h0, x, m):
    left_side = yn * ylc * m
    right_side = yc * (yb * (r_b * 1000) * b * x * (h0 - 0.5 * x) + ys * (r_sc * 1000) * (a_sc / 10000) * (h0 - pl_s))
    output = {'strength_condition': right_side > left_side,
              'left_side': left_side,
              'right_side': right_side,
              }
    return output


data = {'yn': '1',
        'yc': '1',
        'ylc': '1',
        'yb': '1',
        'ys': '1',
        'h': '0.6',
        'b': '1',
        'a': '0.04',
        'a_s_d': '20',
        'a_s_n': '5',
        'a_sc_d': '12',
        'a_sc_n': '5',
        'class_concrete': 'B20',
        'class_reinforcement': 'A400',
        'm': '1000'
        }


def strength_kz_bending_sp41(input_data):
    # variables_list = ['gamma_n', 'gamma_c', 'gamma_lc', 'gamma_b', 'gamma_s', 'section_height', 'section_width',
    #                   's_protective_layer', 'sc_protective_layer', 's_reinforcement_area', 'sc_reinforcement_area',
    #                   'class_concrete', 'class_reinforcement', 'bending_moment']

    yn = float(input_data.get('gamma_n')) if 'gamma_n' in input_data else 1
    yc = float(input_data.get('gamma_c')) if 'gamma_c' in input_data else 1
    ylc = float(input_data.get('gamma_lc')) if 'gamma_lc' in input_data else 1
    yb = float(input_data.get('gamma_b')) if 'gamma_b' in input_data else 1
    ys = float(input_data.get('gamma_s')) if 'gamma_s' in input_data else 1

    h = float(input_data.get('section_height')) if 'section_height' in input_data else None
    b = float(input_data.get('section_width')) if 'section_width' in input_data else None
    pl_s = float(input_data.get('s_protective_layer')) if 's_protective_layer' in input_data else None
    pl_sc = float(input_data.get('sc_protective_layer')) if 'sc_protective_layer' in input_data else None

    a_d_s = float(input_data.get('s_reinforcement_diameter')) if 's_reinforcement_diameter' in input_data else None
    a_d_sc = float(input_data.get('sc_reinforcement_diameter')) if 'sc_reinforcement_diameter' in input_data else None

    a_s = float(input_data.get('s_reinforcement_area')) if 's_reinforcement_area' in input_data else None
    a_sc = float(input_data.get('sc_reinforcement_area')) if 'sc_reinforcement_area' in input_data else None

    class_concrete = str(input_data.get('class_concrete')) if 'class_concrete' in input_data else None
    class_reinforcement = str(input_data.get('class_reinforcement')) if 'class_reinforcement' in input_data else None

    m = float(input_data.get('bending_moment')) if 'bending_moment' in input_data else None

    pl_s = (pl_s + a_d_s / 2) / 1000
    pl_sc = (pl_sc + a_d_sc / 2) / 1000

    r_b = float(concrete_data.get(class_concrete)[0]) if class_concrete in concrete_data else None
    r_s = int(reinforcement_data.get(class_reinforcement)[0]) if class_reinforcement in reinforcement_data else None
    r_sc = int(reinforcement_data.get(class_reinforcement)[1]) if class_reinforcement in reinforcement_data else None

    h0 = h - pl_s
    x = compressed_zone(ys, yb, r_s, a_s, r_sc, a_sc, r_b, b)
    zeta_x = limit_compressed_zone(h0)

    if x <= 0:
        output = strength_test_1(yn, ylc, yc, ys, r_s, a_s, h0, pl_sc, m)
        output['solution_option'] =1
    elif x < zeta_x:
        output = strength_test_2(yn, ylc, yc, yb, ys, r_b, r_sc, b, a_sc, pl_s, h0, x, m)
        output['solution_option'] = 2
    else:
        output = strength_test_2(yn, ylc, yc, yb, ys, r_b, r_sc, b, a_sc, pl_s, h0, zeta_x, m)
        output['solution_option'] = 3
    

    fig_url = plot_fig([0, 1,3, 5,8], [4, 8, 10, 0, 6])

    output['r_b'] = r_b
    output['r_s'] = r_s
    output['r_sc'] = r_sc
    output['x'] = x
    output['zeta_x'] = zeta_x
    output['h0'] = h0
    output['pl_s'] = pl_s
    output['pl_sc'] = pl_sc
    output['fig_url'] = fig_url



    return output

# print(bending_strength_kz(data))
