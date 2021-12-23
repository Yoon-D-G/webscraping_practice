import wx
import Webscraper as ws

FRAME_SIZE_X = 400
FRAME_SIZE_Y = 400

SCRAPER = ws.Scraper()

def get_model_names(make: str) -> list:
    return [model["Model_Name"] for model in SCRAPER.get_models(make)]


def onChoice(event):
    textbox.SetValue("")
    choice = choicebox.GetStringSelection()
    if choice:
        for model in get_model_names(choice):
            textbox.AppendText(model + "\n")


if __name__ == '__main__':
    car_makes = [make["Make_Name"] for make in SCRAPER.get_makes()]

    window = wx.App()
    frame = wx.Frame(None, title="Car Models", size=(FRAME_SIZE_X, FRAME_SIZE_Y))

    car_makes.insert(0, "--Car Makes--")
    choicebox = wx.Choice(frame, choices=car_makes, style=0, size=(FRAME_SIZE_X, wx.EXPAND))
    choicebox.SetSelection(0)
    choicebox.Bind(wx.EVT_CHOICE, onChoice)

    textbox = wx.TextCtrl(frame, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(FRAME_SIZE_X, FRAME_SIZE_Y-20), pos=(0, 20))

    frame.Show()
    window.MainLoop()