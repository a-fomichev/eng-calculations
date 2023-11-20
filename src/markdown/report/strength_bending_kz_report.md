### Met

Расчет прочности прямоугольных сечений железобетонных элементов на действие изгибающего момента производится согласно п.8.14 СП&nbsp;41.13330 из условия:
$$
\gamma_n\cdot\gamma_{lc}\cdot\ M\le\gamma_c\cdot \left(\gamma_b\cdot\ R_b\cdot\ b\cdot\
                x\cdot\left(h_0-0.5\cdot\ x\right)+\gamma_s\cdot\ R_{sc}\cdot\
                {A^\prime}_s\cdot\left(h_0-a\right)\right)
               \tag{1}\label{eq1}
$$

При этом положение нейтральной оси определяется по формуле:
$$
\gamma_b \cdot R_b \cdot b \cdot x+\gamma_s \cdot R_{sc} \cdot A^\prime_s+\gamma_s \cdot R_s \cdot A_s
                \tag{2}\label{eq2}
$$

### Исходные данные

Расчетное сечение имеет размеры: ${{input_data.section_width}}х{{input_data.section_height}} s$ .

Площадь арматуры растянутой и сжатой зоны равна:
$$
A_s={{input_data.s_reinforcement_number}}\cdot \emptyset{{input_data.s_reinforcement_diameter}}={{input_data.s_reinforcement_area}}\,cm^2
\tag{3}\label{eq3}
$$
$$
A_{sc}={{input_data.sc_reinforcement_number}}\cdot \emptyset{{input_data.sc_reinforcement_diameter}}={{input_data.sc_reinforcement_area}}\,cm^2
\tag{4}\label{eq4}
$$

Защитный слой у растянутой грани равен $a={{input_data.s_protective_layer}} мм$, у сжатой грани $a'={{input_data.sc_protective_layer}} mm$.

Расчетное сопротивление бетона {{input_data.class_concrete}} осевому сжатию равно $R_b=22 mmm$

Расчетное сопротивление арматуры {{input_data.class_reinforcement}} растяжению сжатию равно $R_s={{result_data.r_s}}\,mmm$, $R_{sc}={{result_data.r_sc}}\,mmm$ соответственно.

### Расчет прочности

Определим положение нейтральной оси из условия ($\ref{eq1}$):
$$
x=\frac{\gamma_s \cdot R_s\cdot A_s-\gamma_s \cdot R_{sc}\cdot A_{sc} }{\gamma_b \cdot R_b\cdot b}=\\
=\frac{ {{input_data.gamma_s}} \cdot R_s\cdot {{input_data.s_reinforcement_area}} \cdot 10^{-4}-{{input_data.gamma_s}} \cdot R_{sc}\cdot {{input_data.sc_reinforcement_area}} \cdot 10^{-4} }{ {{input_data.gamma_b}} \cdot R_b\cdot {{input_data.section_width}}}={{ '%.2f'|format(result_data.x) }}
\tag{5}\label{eq5}
$$
{% if result_data.solution_option=="1" %}

### Первое

{% elif result_data.solution_option=="2" %}

### Второе

{% else %}

### Третье

{% endif%}



