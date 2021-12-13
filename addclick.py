n=0
mul=1
def addclick(label,btn):
    global n,mul
    mul = n // 10+1
    n += 1 * mul
    label['text'] = str(n) + '$'
    btn.configure(text=f"Клик+{mul}")

