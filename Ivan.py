import addclick
def clearclicks(label,btn):
    addclick.n = 0
    label['text'] = str(addclick.n) + '$'
    btn["text"] = "клиик+1"