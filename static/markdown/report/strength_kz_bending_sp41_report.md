### Met

Расчет прочности прямоугольных сечений железобетонных элементов на действие изгибающего момента производится согласно п.8.14 СП&nbsp;41.13330 из условия: в апавп ва пвап вап вап ва пва вапва пва пвавп впв пвып выпыпаы ывапвапваып выапваы п вапвы пы пывапвы пваы пывапыв пыва выап впа вапвапв ап вапвп
$$
\gamma_n\cdot\gamma_{lc}\cdot\ M\le\gamma_c\cdot \left(\gamma_b\cdot\ R_b\cdot\ b\cdot\
                x\cdot\left(h_0-0.5\cdot\ x\right)+\gamma_s\cdot\ R_{sc}\cdot\
                {A^\prime}_s\cdot\left(h_0-a\right)\right)
\label{eq:f1}
\tag{1}
$$

При этом положение нейтральной оси определяется по формуле:
$$
\gamma_b \cdot R_b \cdot b \cdot x+\gamma_s \cdot R_{sc} \cdot A^\prime_s+\gamma_s \cdot R_s \cdot A_s
\label{eq:f2}
\tag{2}
$$

где

$\gamma_n$ — коэффициент надежности, принимаемый равным {{report_data.gamma_n}};

$\gamma_c$ — коэффициент условий работы, принимаемый равным {{report_data.gamma_c}};

$\gamma_{lc}$ — коэффициент сочетания нагрузок, принимаемый равным {{report_data.gamma_lc}};

$\gamma_{b}$ — коэффициент условий работы бетона, принимаемый равным {{report_data.gamma_b}};

$\gamma_{s}$ — коэффициент условий работы арматуры, принимаемый равным {{report_data.gamma_s}};

$R_{b}$ — расчетное сопротивление бетона сжатию, равное {{report_data.r_b}} МПа;

$R_{s}$ — расчетное сопротивление арматуры растяжению, равное {{report_data.r_s}}​ МПа;



### Расчет прочности

Определим положение нейтральной оси:

$$
\displaylines{x=\frac{\gamma_s \cdot R_s\cdot A_s-\gamma_s \cdot R_{sc}\cdot A_{sc} }{\gamma_b \cdot R_b\cdot b}
= \\\ \frac{ {{report_data.gamma_s}}\cdot{{report_data.r_s}}\cdot10^{-3}\cdot{{report_data.s_reinforcement_area}}\cdot10^{-4}-{{report_data.gamma_s}}\cdot{{report_data.r_sc}}\cdot10^{-3}\cdot{{report_data.sc_reinforcement_area}}\cdot10^{-4} }{ {{report_data.gamma_b}}\cdot{{report_data.r_b}}\cdot10^{-3}\cdot{{report_data.b}} }=
{{report_data.x }}}
\label{eq:f3}
\tag{3}
$$

{% if report_data.solution_option==1 %}
### Первое
В случае если высота сжатой зоны меньше или равна 0 расчет прочности ведётся из условия:  
$$
\gamma_n\cdot\gamma_{lc}\cdot\ M\le\gamma_c\cdot +\gamma_s\cdot\ R_{sc}\cdot\ A^\prime_s\cdot\left(h_0-a\right)
$$



$$
a=1
\label{eq:f5}
\tag{5}
$$

$$
b+c=14
\label{eq:f6}
\tag{6}
$$

{% elif report_data.solution_option==2 %}

### Второе
{% else %}
### Третье
{% endif%}



### Картинка
 <img src="data:image/png;base64,{{report_data.fig_url}}" alt="Standing Wave C">





