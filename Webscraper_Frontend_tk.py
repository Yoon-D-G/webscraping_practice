import tkinter as tk
import Webscraper as ws

WINDOW = tk.Tk()
TEXT_WIDGET = tk.Text()
SCRAPER = ws.Scraper()


def update_text_widget(values: list):
    if values:
        TEXT_WIDGET.delete(1.0, tk.END)
        for value in values:
            TEXT_WIDGET.insert(tk.END, value + '\n')
        TEXT_WIDGET.pack()


def construct_options(values: list, label, trace) -> tk.OptionMenu:
    if values:
        var = tk.StringVar()
        var.set(label)
        return tk.OptionMenu(WINDOW, trace, var, *values)


def update(*args):
    models = SCRAPER.get_models(option_select.get())
    model_names = []
    for model in models:
        model_names.append(model['Model_Name'])
    update_text_widget(model_names)
    print("Value changed!" + option_select.get())


if __name__ == '__main__':
    data = SCRAPER.get_makes()
    make_names = []
    for make in data:
        if make:
            make_names.append(make["Make_Name"])

    option_select = tk.StringVar(WINDOW)
    option_select.trace("w", update)

    option_menu = construct_options(values=make_names, label="Car Make", trace=option_select)

    option_menu.pack()

    WINDOW.mainloop()
