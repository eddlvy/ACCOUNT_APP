import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from DATABASE.FOLDER.windows_dpi import windows_dpi
import csv


windows_dpi()


# STYLES

MAIN_COLOR = '#bac8ff'
SECONDARY_COLOR = '#dbe4ff'
TERCIARY_COLOR = '#fff3bf'
RED = '#f03e3e'
GREEN = '#51cf66'


root = tk.Tk()
root.title('PRESUPUESTO CASA MENSUAL')
root.geometry('1600x800')
root.columnconfigure(0, weight=1)
root.rowconfigure((1, 2, 3, 4), weight=1)
font.nametofont('TkDefaultFont').configure(size=12)
root.iconbitmap('..\\CONTABILIDAD_APP\\DATABASE\\icons8-economy-96.png')


# VARIABLES
mes_selected = tk.StringVar()
real = tk.IntVar(value=0)
ingresos = tk.IntVar(value=0)
gastos = tk.IntVar(value=0)
resumen_mes = tk.StringVar(value=0)
# var tipo gastos
# comida
comida_entry_text = tk.StringVar()
comida_gasto_real = tk.IntVar(value=0)
comida_real = tk.IntVar()
# gasolina
gasolina_entry_text = tk.StringVar()
gasolina_gasto_real = tk.IntVar(value=0)
gasolina_real = tk.IntVar()
# medicina
medicina_entry_text = tk.StringVar()
medicina_gasto_real = tk.IntVar(value=0)
medicina_real = tk.IntVar()
# banco
banco_entry_text = tk.StringVar()
banco_gasto_real = tk.IntVar(value=0)
banco_real = tk.IntVar()
# otros_gastos
otros_gastos_entry_text = tk.StringVar()
otros_gastos_gasto_real = tk.IntVar(value=0)
otros_gastos_real = tk.IntVar()
# casa fijo mensual

casa = tk.StringVar(value=0)

# FUNCTIONS


def mes_selected_fun(event):
    print(mes_selected.get())


def set_mes_selected():
    with open('..\\CONTABILIDAD_APP\\DATABASE\\ingresos.csv', encoding='utf-8') as mes:
        csv_data = csv.reader(mes)
        csv_data_list = list(csv_data)
        mes = csv_data_list[-1][-1]
        mes_selected.set(mes)
        print(mes_selected.get())
        return mes_selected


def resumen_mes_fun(ingresos, real):
    global resumen_mes
    resumen_mes
    if int(ingresos.get()) >= int(real.get()):
        superavit = int(ingresos.get()) - int(real.get())
        resultado = f'SUPERAVIT:  {superavit}'
        resumen_mes.set(resultado)
        return resumen_mes
    elif int(ingresos.get()) <= int(real.get()):
        deficit = int(ingresos.get()) - int(real.get())
        resultado = f'DEFICIT:  {deficit}'
        resumen_mes.set(resultado)
        return resumen_mes


def ingresos_guardar(mes_selected):
    global ingresos
    ingresos
    value = int(ingresos_input.get('1.0', 'end'))
    ingresos.set(value)
    resumen_mes_fun(ingresos, real)
    if value > 0:
        with open('..\\CONTABILIDAD_APP\\DATABASE\\ingresos.csv',
                  'a', newline='') as output:

            ingreso = value
            mes = mes_selected.get()
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csv_writer.writerow([ingreso, mes])
    color_resultado()
    return ingresos


def csv_reader_ingresos(ingresos_input):
    ingreso_csv = open(
        '..\\CONTABILIDAD_APP\\DATABASE\\ingresos.csv', encoding='utf-8')
    csv_data = csv.reader(ingreso_csv)
    csv_data_list = list(csv_data)
    ing_mes = csv_data_list[-1][0]
    input_ing = ingresos_input.insert('1.0', int(ing_mes))
    return input_ing


def real_csv_reader():
    global real
    real
    real_csv = open('..\\CONTABILIDAD_APP\\DATABASE\\real.csv',
                    encoding='utf-8')
    csv_data = csv.reader(real_csv)
    csv_data_list = list(csv_data)
    real_mes = csv_data_list[-1][-1]
    return real.set(real_mes)


def csv_reader_real_especifico():
    with open('..\\CONTABILIDAD_APP\\DATABASE\\comida_real.csv', encoding='utf-8') as real:
        csv_data = csv.reader(real)
        csv_data_list = list(csv_data)
        comida = csv_data_list[-1][-1]
        comida_real.set(comida)

    with open('..\\CONTABILIDAD_APP\\DATABASE\\gasolina_real.csv', encoding='utf-8') as real:
        csv_data = csv.reader(real)
        csv_data_list = list(csv_data)
        gasolina = csv_data_list[-1][-1]
        gasolina_real.set(gasolina)

    with open('..\\CONTABILIDAD_APP\\DATABASE\\medicina_real.csv', encoding='utf-8') as real:
        csv_data = csv.reader(real)
        csv_data_list = list(csv_data)
        medicina = csv_data_list[-1][-1]
        medicina_real.set(medicina)
    with open('..\\CONTABILIDAD_APP\\DATABASE\\banco_real.csv', encoding='utf-8') as real:
        csv_data = csv.reader(real)
        csv_data_list = list(csv_data)
        banco = csv_data_list[-1][-1]
        banco_real.set(banco)
    with open('..\\CONTABILIDAD_APP\\DATABASE\\otros_gastos_real.csv', encoding='utf-8') as real:
        csv_data = csv.reader(real)
        csv_data_list = list(csv_data)
        otros_gastos = csv_data_list[-1][-1]
        otros_gastos_real.set(otros_gastos)


def csv_writer_real_especifico(gasto_real):
    if gasto_real is comida_gasto_real:
        comida_r = comida_real.get()
        with open('..\\CONTABILIDAD_APP\\DATABASE\\comida_real.csv', 'a', newline='') as output:
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csv_writer.writerow([int(gasto_real.get())+comida_r])

    elif gasto_real is gasolina_gasto_real:
        gasolina_r = gasolina_real.get()
        with open('..\\CONTABILIDAD_APP\\DATABASE\\gasolina_real.csv', 'a', newline='') as output:
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csv_writer.writerow(
                [int(gasto_real.get())+gasolina_r])
    elif gasto_real is medicina_gasto_real:
        medicina_r = medicina_real.get()
        with open('..\\CONTABILIDAD_APP\\DATABASE\\medicina_real.csv', 'a', newline='') as output:
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([gasto_real.get()+medicina_r])
    elif gasto_real is banco_gasto_real:
        banco_r = banco_real.get()
        with open('..\\CONTABILIDAD_APP\\DATABASE\\banco_real.csv', 'a', newline='') as output:
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([gasto_real.get()+banco_r])
    elif gasto_real is otros_gastos_gasto_real:
        otros_gastos_r = otros_gastos_real.get()
        with open('..\\CONTABILIDAD_APP\\DATABASE\\otros_gastos_real.csv', 'a', newline='') as output:
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([gasto_real.get()+otros_gastos_r])


def calculo_func(x_entry_text, mes_selected, x_gasto_real):
    global real
    real
    real_value = real.get()
    lugar = x_entry_text.get()
    gasto = x_gasto_real.get()
    mes = mes_selected.get()
    if x_entry_text is comida_entry_text:
        with open('..\\CONTABILIDAD_APP\\DATABASE\\comida_gastos.csv', 'a', newline='') as output:
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csv_writer.writerow([lugar, mes, gasto])
    elif x_entry_text is gasolina_entry_text:
        with open('..\\CONTABILIDAD_APP\\DATABASE\\gasolina.csv', 'a', newline='') as output:
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)

            csv_writer.writerow([lugar, mes, gasto])
    elif x_entry_text is medicina_entry_text:
        with open('..\\CONTABILIDAD_APP\\DATABASE\\medicina.csv', 'a', newline='') as output:
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([lugar, mes, gasto])
    elif x_entry_text is banco_entry_text:
        with open('..\\CONTABILIDAD_APP\\DATABASE\\banco.csv', 'a', newline='') as output:
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([lugar, mes, gasto])
    elif x_entry_text is otros_gastos_entry_text:
        with open('..\\CONTABILIDAD_APP\\DATABASE\\otros_gastos.csv', 'a', newline='') as output:
            csv_writer = csv.writer(output, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([lugar, mes, gasto])
    csv_writer_real_especifico(x_gasto_real)
    csv_reader_real_especifico()
    real_new = real_value + gasto
    real.set(real_new)
    with open('..\\CONTABILIDAD_APP\\DATABASE\\real.csv', 'a', newline='') as value:
        csv_writer = csv.writer(value, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([real_new])
    real_csv_reader()
    ingresos_guardar(mes_selected)
    color_resultado()


def ingresos_setter():
    global ingresos
    ingresos
    with open('..\\CONTABILIDAD_APP\\DATABASE\\ingresos.csv', encoding='utf-8')as ing:
        csv_data = csv.reader(ing)
        csv_data_list = list(csv_data)
        ingreso = csv_data_list[-1][0]
        return ingresos.set(ingreso)


def color_resultado():
    if 'SUPERAVIT:' in str(resumen_mes.get()):
        resultados_label['background'] = GREEN
    else:
        resultados_label['background'] = RED


def casa_fun():
    casa_gasto = int(casa.get())
    real_new = real.get() + casa_gasto
    real.set(real_new)
    with open('..\\CONTABILIDAD_APP\\DATABASE\\real.csv', 'a', newline='') as value:
        csv_writer = csv.writer(value, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([real_new])
    with open('..\\CONTABILIDAD_APP\\DATABASE\\casa.csv', 'a', newline='') as value:
        csv_writer = csv.writer(value, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([real_new])
    real_csv_reader()
    ingresos_guardar(mes_selected)
    color_resultado()


def casa_reader():
    with open('..\\CONTABILIDAD_APP\\DATABASE\\casa.csv', encoding='utf-8') as file:
        csv_data = csv.reader(file)
        csv_data_list = list(csv_data)
        casa_gasto = csv_data_list[-1][0]
        return casa.set(casa_gasto)


def reset_fun():

    real.set(0)
    ingresos_input.delete('1.0', 'end')
    ingresos_input.insert('1.0', '0')
    gastos.set(0)
    resumen_mes.set('SUPERAVIT:  0')

    comida_entry_text.set('')
    comida_gasto_real.set(0)
    comida_real.set(0)

    gasolina_entry_text.set('')
    gasolina_gasto_real.set(0)
    gasolina_real.set(0)

    medicina_entry_text.set('')
    medicina_gasto_real.set(0)
    medicina_real.set(0)

    banco_entry_text.set('')
    banco_gasto_real.set(0)
    banco_real.set(0)

    otros_gastos_entry_text.set('')
    otros_gastos_gasto_real.set(0)
    otros_gastos_real.set(0)

    casa.set(0)
    with open('..\\CONTABILIDAD_APP\\DATABASE\\comida_real.csv', 'a', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([0])

    with open('..\\CONTABILIDAD_APP\\DATABASE\\gasolina_real.csv', 'a', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow(
            [0])

    with open('..\\CONTABILIDAD_APP\\DATABASE\\medicina_real.csv', 'a', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([0])

    with open('..\\CONTABILIDAD_APP\\DATABASE\\banco_real.csv', 'a', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([0])

    with open('..\\CONTABILIDAD_APP\\DATABASE\\otros_gastos_real.csv', 'a', newline='') as output:
        csv_writer = csv.writer(output, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([0])
    with open('..\\CONTABILIDAD_APP\\DATABASE\\real.csv', 'a', newline='') as value:
        csv_writer = csv.writer(value, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([0])
    with open('..\\CONTABILIDAD_APP\\DATABASE\\ingresos.csv',
              'a', newline='') as output:

        csv_writer = csv.writer(output, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([0, 'DEFINE MES'])
    with open('..\\CONTABILIDAD_APP\\DATABASE\\casa.csv', 'a', newline='') as value:
        csv_writer = csv.writer(value, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([0])
    color_resultado()


set_mes_selected()
ingresos_setter()
real_csv_reader()
csv_reader_real_especifico()
resumen_mes_fun(ingresos, real)
casa_reader()

# PRINCIPAL FRAME1
frame1 = ttk.Frame(root, relief='solid', border=1)
frame1.grid(row=0, column=0, sticky='ew')
frame1.columnconfigure((1, 2, 3, 4), weight=1)

# ROW 0
presupuesto_label = ttk.Label(
    frame1, text='PRESUPUESTO DEL MES', anchor='center', background=MAIN_COLOR, padding=15, font=('Cursive', 15))
presupuesto_label.grid(row=0, column=1, columnspan=4, sticky='ew')

# ROW 1
# column1
gastos_label = ttk.Label(
    frame1, text='PLANIFICACION \nDE GASTOS', anchor='center', font=('Helvetica', 15), background=TERCIARY_COLOR)
gastos_label.grid(row=1, column=1, sticky='ew', pady=20, padx=(15, 0))

# column2

escoje_mes_label = ttk.Label(
    frame1, text='DEFINE EL MES', anchor='center', font=('Cursive', 14), padding=(20, 10, 20, 0))
escoje_mes_label.grid(row=1, column=2, sticky='n')
mes_combobox = ttk.Combobox(frame1, textvariable=mes_selected, justify='center', values=(
    'ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE'),  width=15, font=(
    'Cursive', 12))
mes_combobox.grid(row=1, column=2, pady=10)

# frame1 column 3


empezar_mes_button = ttk.Button(
    frame1, text='CLICK AQUI PARA EMPEZAR MES', cursor='hand2', padding=4, command=lambda: reset_fun())
empezar_mes_button.grid(row=1, column=3, sticky='n', pady=30)


# frame1
# column4


real_label_label = ttk.Label(frame1, text='REAL GASTOS', font=(
    'Cursive', 14), padding=(20, 10, 20, 0))
real_label_label.grid(row=1, column=4, sticky='n')

real_label = ttk.Label(frame1, textvariable=real, font=(
    'Cursive', 14), padding=(20, 0, 20, 0), anchor='center', background=TERCIARY_COLOR)
real_label.grid(row=1, column=4, pady=5)

# FRAME2

frame2 = ttk.Frame(root)
frame2.grid(row=1, column=0, sticky='ew')
frame2.columnconfigure((1, 2), weight=1)

# frame2
# column1

resumen_mes_label = ttk.Label(
    frame2, text='RESUMEN FIN DE MES', anchor='center', font=('Helvetica', 14))
resumen_mes_label.grid(row=1, column=0, sticky='ew', padx=80)

separator = ttk.Separator(frame2, orient='vertical')
separator.grid(row=1, column=1, sticky='ns')


# INGRESOS FRAME
# frame_ingresos row 1
frame_ingresos = ttk.Frame(frame2)
frame_ingresos.grid(row=1, column=2, sticky='ew')
frame_ingresos.columnconfigure((1, 2), weight=1)

ingresos_label = ttk.Label(frame_ingresos, text='INGRESOS PLANIFICADOS MES', justify='left', font=(
    'Cursive', 14), background=TERCIARY_COLOR)
ingresos_label.grid(row=1, column=1, sticky='w', padx=22)

# frame_ingresos_input
frame_ingresos_input = ttk.Frame(frame_ingresos)
frame_ingresos_input.grid(row=1, column=2)


frame_ingresos_input.columnconfigure((1, 2), weight=1)
ingresos_input = tk.Text(frame_ingresos_input, height=1.2, font=(
    'Cursive', 14,), width=14)
csv_reader_ingresos(ingresos_input)
ingresos_input.grid(row=1, column=1)
ingresos_button = ttk.Button(
    frame_ingresos_input, text='Guardar', command=lambda: ingresos_guardar(mes_selected), cursor='hand2', padding=2)
ingresos_button.grid(row=1, column=2, padx=3)

# frame_ingresos row2
# subframe
menos_label = menos_real_label = ttk.Label(frame_ingresos, text='- REAL    ', font=(
    'Cursive', 14))
menos_real_label.grid(row=2, column=1, pady=5, sticky='w')
menos_real_label = ttk.Label(frame_ingresos, textvariable=real, font=(
    'Cursive', 14))
menos_real_label.grid(row=2, column=1, pady=5, sticky='e')
sep3 = ttk.Separator(frame_ingresos, orient='horizontal')
sep3.grid(row=3, columnspan=2, sticky='ew')

# frame ingresos row 3

resultados_label = ttk.Label(frame_ingresos, textvariable=resumen_mes, font=(
    'Cursive', 14), justify='left')
color_resultado()
resultados_label.grid(row=4, column=1)

sep_frame1_frame2 = ttk.Separator(root, orient='horizontal')
sep_frame1_frame2.grid(row=2, column=0, sticky='ew')

# PRINCIPAL FRAME 3

frame3 = ttk.Frame(root, relief='solid', border=1)
frame3.grid(row=2, column=0, sticky='nsew', pady=20)
frame3.rowconfigure((0, 1, 2, 3, 4, 6, 7), weight=1, pad=15)
frame3.columnconfigure((1, 2, 3, 4, 5), weight=1)

# LABEL GASTOS
tipo_gastos_label = ttk.Label(frame3, text='TIPO GASTO', font=(
    'Cursive', 14), justify='center')
tipo_gastos_label.grid(row=0, column=1)
lugar_label = ttk.Label(frame3, text='LUGAR Y FECHA', font=(
    'Cursive', 14), justify='left')
lugar_label.grid(row=0, column=2)
real_label_tipo_gasto = ttk.Label(frame3, text='IMPORTE', font=(
    'Cursive', 14), justify='center')
real_label_tipo_gasto.grid(row=0, column=3)
plan_label_tipo_gasto = ttk.Label(frame3, text='TOTAL MES', font=(
    'Cursive', 12), justify='center')
plan_label_tipo_gasto.grid(row=0, column=4)


# comida gastos

comida_label = ttk.Label(frame3, text='GASTOS COMIDA', font=(
    'Cursive', 14), justify='center')
comida_label.grid(row=1, column=1)
comida_entry = ttk.Entry(
    frame3, textvariable=comida_entry_text, width=27, font=(
        'Cursive', 14), justify='left')
comida_entry.grid(row=1, column=2, sticky='ew')
real_comida_entry = ttk.Entry(
    frame3, textvariable=comida_gasto_real, width=15, font=(
        'Cursive', 14), justify='left')
real_comida_entry.grid(row=1, column=3)

plan_tipo_gasto_comida = ttk.Label(frame3, textvariable=comida_real, font=(
    'Cursive', 14), justify='center', background=TERCIARY_COLOR)
plan_tipo_gasto_comida.grid(row=1, column=4)
comida_guardar = ttk.Button(
    frame3, text='CLICK GUARDAR', cursor='hand2', padding=1, command=lambda: calculo_func(comida_entry_text, mes_selected, comida_gasto_real))
comida_guardar.grid(row=1, column=5)

# gasolina gastos

gasolina_label = ttk.Label(frame3, text='GASOLINA', font=(
    'Cursive', 14), justify='center')
gasolina_label.grid(row=2, column=1)
comida_entry = ttk.Entry(
    frame3, textvariable=gasolina_entry_text, width=27, font=(
        'Cursive', 14), justify='left')
comida_entry.grid(row=2, column=2, sticky='ew')
real_gasolina_entry = ttk.Entry(
    frame3, textvariable=gasolina_gasto_real, width=15, font=(
        'Cursive', 14), justify='left')
real_gasolina_entry.grid(row=2, column=3)
plan_tipo_gasto_gasolina = ttk.Label(frame3, textvariable=gasolina_real, font=(
    'Cursive', 14), justify='center', background=TERCIARY_COLOR)
plan_tipo_gasto_gasolina.grid(row=2, column=4)
gasolina_guardar = ttk.Button(
    frame3, text='CLICK GUARDAR', cursor='hand2', padding=1, command=lambda: calculo_func(gasolina_entry_text, mes_selected, gasolina_gasto_real))
gasolina_guardar.grid(row=2, column=5)

# medicinas gastos

medicina_label = ttk.Label(frame3, text='MEDICINAS', font=(
    'Cursive', 14), justify='center')
medicina_label.grid(row=3, column=1)
medicina_entry = ttk.Entry(
    frame3, textvariable=medicina_entry_text, width=27, font=(
        'Cursive', 14), justify='left')
medicina_entry.grid(row=3, column=2, sticky='ew')
real_medicina_entry = ttk.Entry(
    frame3, textvariable=medicina_gasto_real, width=15, font=(
        'Cursive', 14), justify='left')
real_medicina_entry.grid(row=3, column=3)
plan_tipo_gasto_medicina = ttk.Label(frame3, textvariable=medicina_real, font=(
    'Cursive', 14), justify='center', background=TERCIARY_COLOR)
plan_tipo_gasto_medicina.grid(row=3, column=4)
medicina_guardar = ttk.Button(
    frame3, text='CLICK GUARDAR', cursor='hand2', padding=1, command=lambda: calculo_func(medicina_entry_text, mes_selected, medicina_gasto_real))
medicina_guardar.grid(row=3, column=5)

# deudas banco,tarjetas,prestamos

banco_label = ttk.Label(frame3, text='PRESTAMO BANCO,TARJETAS,DEUDAS', font=(
    'Cursive', 10), justify='center')
banco_label.grid(row=4, column=1)
banco_entry = ttk.Entry(
    frame3, textvariable=banco_entry_text, width=27, font=(
        'Cursive', 14), justify='left')
banco_entry.grid(row=4, column=2, sticky='ew')
real_banco_entry = ttk.Entry(
    frame3, textvariable=banco_gasto_real, width=15, font=(
        'Cursive', 14), justify='left')
real_banco_entry.grid(row=4, column=3)
plan_tipo_gasto_banco = ttk.Label(frame3, textvariable=banco_real, font=(
    'Cursive', 14), justify='center', background=TERCIARY_COLOR)
plan_tipo_gasto_banco.grid(row=4, column=4)
banco_guardar = ttk.Button(
    frame3, text='CLICK GUARDAR', cursor='hand2', padding=1, command=lambda: calculo_func(banco_entry_text, mes_selected, banco_gasto_real))
banco_guardar.grid(row=4, column=5)

# otros gastos

otros_gastos_label = ttk.Label(frame3, text='OTROS GASTOS', font=(
    'Cursive', 14), justify='center')
otros_gastos_label.grid(row=5, column=1)
otros_gastos_entry = ttk.Entry(
    frame3, textvariable=otros_gastos_entry_text, width=27, font=(
        'Cursive', 14), justify='left')
otros_gastos_entry.grid(row=5, column=2, sticky='ew')
real_otros_gastos_entry = ttk.Entry(
    frame3, textvariable=otros_gastos_gasto_real, width=15, font=(
        'Cursive', 14), justify='left')
real_otros_gastos_entry.grid(row=5, column=3)
plan_tipo_gasto_otros_gastos = ttk.Label(frame3, textvariable=otros_gastos_real, font=(
    'Cursive', 14), justify='center', background=TERCIARY_COLOR)
plan_tipo_gasto_otros_gastos.grid(row=5, column=4)
otros_gastos_guardar = ttk.Button(
    frame3, text='CLICK GUARDAR', cursor='hand2', padding=1, command=lambda: calculo_func(otros_gastos_entry_text, mes_selected, otros_gastos_gasto_real))
otros_gastos_guardar.grid(row=5, column=5)

# casa

casa_label = ttk.Label(frame3, text='CASA FIJO MENSUAL', font=(
    'Cursive', 14), justify='center')
casa_label.grid(row=6, column=1)

casa_entry = ttk.Entry(
    frame3, textvariable=casa, width=15, font=(
        'Cursive', 14), justify='left')
casa_entry.grid(row=6, column=3)
casa_guardar = ttk.Button(
    frame3, text='CLICK GUARDAR', cursor='hand2', padding=1, command=lambda: casa_fun())
casa_guardar.grid(row=6, column=5)

# prod label

edu_label = ttk.Label(root, text='made by EduLPLab', font=(
    'Cursive', 10), justify='center', anchor='center')
edu_label.grid(row=4, column=0, sticky='n')


# BINGDINGS
mes_combobox.bind('<<ComboboxSelected>>', mes_selected_fun)


root.mainloop()
