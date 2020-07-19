
from tkinter import *

class GeneticAlGUI:

    def __init__(self):

        myBgColor = '#d5e8e8'
        myInitColor = '#e6f5f5'
        myBtnColor = '#1797ff'
        myTitleColor = '#164452'

        # задаем параметны интерфейса
        self.root = Tk()
        self.root.title("Генетический алгоритм")
        self.root.iconbitmap(bitmap=None)
        self.root.geometry('1020x500+400+200')
        self.root.config(bg=myBgColor)
        self.root.resizable(True, False)  # размер окна может быть изменён только по горизонтали

        # задаем три Frame, в которые будем размещаться виджеты по ветрикали

        # инициализируем функции элементов интерфейса
        self.population_number = IntVar()
        self.generations_number = IntVar()
        self.chance_cross_percent = IntVar()
        self.chance_mutation_percent = IntVar()
        self.strategy_choice = IntVar()
        self.selection_type = IntVar()
        self.cross_operator = IntVar()
        self.mutation_operator = IntVar()
        self.short_result = StringVar()
        self.total_console_result = StringVar()

        # добавляем элементы spinbox в первую колонку
        self.root.population_number_label = Label(
            text="Размер начальной популяции:", font='Helvetica 15',
            bg=myBgColor, padx=5, pady=8, fg=myTitleColor
        ).grid(column=0, row=0)
        self.root.population_number_spinbox = Spinbox(
            from_=10, to=100, increment=10, width=30, bg=myInitColor
        ).grid(column=0, row=1)
        self.root.generations_number_label = Label(
            text="Количество генераций:", font='Helvetica 15',
            bg=myBgColor, padx=5, pady=8, fg=myTitleColor
        ).grid(column=0, row=2)
        self.root.generations_number_spinbox = Spinbox(
            from_=50, to=200, increment=10, width=30, bg=myInitColor
        ).grid(column=0, row=3)

        # добавляем элементы scale в первую колонку
        self.root.chance_cross_percent_label = Label(
            text="Вероятность кроссинговера", font='Helvetica 15',
            bg=myBgColor, bd=4, padx=5, pady=8, width=30, fg=myTitleColor
        ).grid(column=0, row=4)
        self.root.chance_cross_scale = Scale(
            orient=HORIZONTAL, length=300, bg=myInitColor, relief=GROOVE,
            activebackground=myBtnColor,
            from_=0, to=100, resolution=10, tickinterval=10,
        ).grid(column=0, row=5)
        self.root.chance_mutation_percent_label = Label(
            text="Вероятность мутации", font='Helvetica 15',
            bg=myBgColor, bd=4, padx=5, pady=8, width=30, fg=myTitleColor
        ).grid(column=0, row=6)
        self.root.chance_mutation_scale = Scale(
            orient=HORIZONTAL, length=300, bg=myInitColor, relief=GROOVE,
            activebackground=myBtnColor,
            from_=0, to=100, resolution=10, tickinterval=10,
        ).grid(column=0, row=7)

        # добавляем элементы условия и ответа в frame
        self.root.leftFrame = Frame(width=30, bd=5, padx=5, pady=15, bg=myInitColor, relief=GROOVE)
        self.root.leftFrame.grid(column=0, row=8, rowspan=3)
        self.root.leftFrame.math_func_label = Label(
            text="max f(x) = х^2+ 20х − 34", font='Helvetica 15', bg=myInitColor, padx=5, pady=10, width=32)
        self.root.leftFrame.math_func_label.grid(column=0, row=9)
        self.root.leftFrame.interval_func_label = Label(
            text="на интервале [8−12]", font='Helvetica 15', bg=myInitColor, padx=5, width=32)
        self.root.leftFrame.interval_func_label.grid(column=0, row=10)
        self.root.leftFrame.short_result_label = Label(
            text="Ответ: ", font='Helvetica 15', bg=myInitColor, padx=5, width=32)  # добавить сюда ответ
        self.root.leftFrame.short_result_label.grid(column=0, row=11, sticky='w')

        # добавляем элементы RadioButton во вторую колонку
        self.root.strategy_choice_label = Label(
            text="Стратегия создания начальной популяции:",
            font='Helvetica 15', bg=myBgColor, padx=5, pady=5, width=32, fg=myTitleColor
        ).grid(column=1, row=0, columnspan=2)
        self.root.strategy_choice_1 = Radiobutton(
            text='Стратегия \"одеяла\"',  font='Helvetica 15', bg=myBgColor,
            justify='left', variable=self.strategy_choice, value=1
        ).grid(column=1, row=1, padx=10, sticky='nw')
        self.root.strategy_choice_2 = Radiobutton(
            text='Стратегия фокусировки', font='Helvetica 15', bg=myBgColor,
            justify='left', variable=self.strategy_choice, value=2
        ).grid(column=1, row=2, padx=10, sticky='nw')

        self.root.selection_type_label = Label(
            text="Вид селекции:", font='Helvetica 15',
            bg=myBgColor, padx=5, pady=5, width=32, fg=myTitleColor
        ).grid(column=1, row=3, columnspan=2)
        self.root.selection_type_1 = Radiobutton(
            text='Случайная', font='Helvetica 15', bg=myBgColor,
            justify='left', variable=self.selection_type, value=1
        ).grid(column=1, row=4, padx=10, sticky='nw', rowspan=2)
        self.root.selection_type_2 = Radiobutton(
            text='Инбридинг', font='Helvetica 15', bg=myBgColor,
            justify='left', variable=self.selection_type, value=2
        ).grid(column=1, row=5, padx=10, sticky='nw', rowspan=3)

        self.root.сross_operator_label = Label(
            text="Оператор кроссинговера:", font='Helvetica 15',
            bg=myBgColor, padx=5, pady=5, width=32, fg=myTitleColor
        ).grid(column=1, row=6, columnspan=2)
        self.root.сross_operator_1 = Radiobutton(
            text='Стандартный одноточечный', font='Helvetica 15', bg=myBgColor,
            justify='left', variable=self.cross_operator, value=1
        ).grid(column=1, row=7, padx=10, sticky='nw')
        self.root.сross_operator_2 = Radiobutton(
            text='Частично соответствующий одноточечный', font='Helvetica 15', bg=myBgColor,
            justify='left', variable=self.cross_operator, value=2
        ).grid(column=1, row=8, padx=10, sticky='nw')
        self.root.сross_operator_3 = Radiobutton(
            text='На основе \"Золотого сечения»\"', font='Helvetica 15', bg=myBgColor,
            justify='left', variable=self.cross_operator, value=3
        ).grid(column=1, row=9, padx=10, sticky='nw')

        self.root.mutation_operator_label = Label(
            text="Оператор мутации и инверсии:", font='Helvetica 15',
            bg=myBgColor, padx=5, pady=5, width=32, fg=myTitleColor
        ).grid(column=1, row=10, columnspan=2)
        self.root.mutation_operator_1 = Radiobutton(
            text='Стандартный одноточечный', font='Helvetica 15', bg=myBgColor,
            justify='left', variable=self.mutation_operator, value=1
        ).grid(column=1, row=11, padx=10, sticky='nw')
        self.root.mutation_operator_2 = Radiobutton(
            text='Частично соответствующий одноточечный', font='Helvetica 15', bg=myBgColor,
            justify='left', variable=self.mutation_operator, value=2
        ).grid(column=1, row=12, padx=10, sticky='nw')

        # добавляем элементы Button и Text в третью колонку
        self.root.startButton = Button(
            text='Выполнить', font='Helvetica 15', bg=myBtnColor,
            width=15, height=5, padx=1, pady=10
        ).grid(column=2, row=0)
        self.root.total_console_result_text = Text(
            height=40, width=40, wrap=WORD
        ).pack(side='right')
        self.root.vscrollbar = Scrollbar(
            orient='vert', command=self.root.total_console_result_text.yview
        ).pack(side='right')
        self.root.total_console_result_text['yscrollcommand'] = self.root.vscrollbar.set

        self.root.mainloop()
