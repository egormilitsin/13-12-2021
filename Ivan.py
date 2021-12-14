import addclick
def clearclicks(label,btn):
    addclick.n = 0
    label['text'] = str(addclick.n) + '$'
    btn["text"] = "клик+1"