import tkinter as tk

class Window(object):

  def __init__(self):
    self.root = tk.Tk()

    self.canvas = tk.Canvas(self.root)

    self.symbolLabel = tk.Label(self.root, text="Operation")
    self.symbolEntry = tk.Entry(self.root)

    self.numLabel = tk.Label(self.root, text="Number")
    self.numEntry = tk.Entry(self.root)

    self.symbolLabel.grid(row=0, column=0, padx=5, pady=2.5, ipadx=3, ipady=3)
    self.symbolEntry.grid(row=0, column=1, padx=5, pady=2.5, ipadx=3, ipady=3)

    self.numLabel.grid(row=1, column=0, padx=5, pady=2.5, ipadx=3, ipady=3)
    self.numEntry.grid(row=1, column=1, padx=5, pady=2.5, ipadx=3, ipady=3)

    self.enterButton = tk.Button(self.root, text="Enter", command=self.enter, padx=3, pady=3)
    self.enterButton.grid(row=0, column=2, rowspan=2, ipadx=3, ipady=3)

    self.warning = ""
    self.warningLabel = tk.Label(self.root, text="")
    self.warningLabel.config(text=self.warning)
    self.warningLabel.grid(row=2, column=0, columnspan=3)

    self.outputText = tk.Text(self.root, height=12, width=50, state="disabled", padx=5, pady=5)
    self.outputText.grid(row=3, column=0, columnspan=3)

  def loop(self):
    self.root.mainloop()

  def enter(self):

    self.operation = self.symbolEntry.get()
    self.number = self.numEntry.get()

    if self.checkOperation(self.operation) and self.checkNum(self.number):
      self.warning = ""
      self.warningLabel.config(text=self.warning)
      self.setOutput()

    elif not self.checkOperation(self.operation):
      self.warning = "The operation is invalid"
      self.warningLabel.config(text=self.warning)
    else:
      self.warning = "The number is invalid"
      self.warningLabel.config(text=self.warning)

  def setOutput(self):
    self.ops = ops = {"+": (lambda x,y: x+y), 
                      "-": (lambda x,y: x-y), 
                      "/": (lambda x,y: round(x/y, 2)),
                      "*": (lambda x,y: x*y)}

    self.number = int(self.number)
    self.nums = range(0, self.number + 1)

    self.output = "{} |".format(self.operation)
    for num in self.nums:
      self.output = "{} {}".format(self.output, num)

    length = len(self.output)

    self.output = self.output + "\n"

    for x in range(length):
      self.output = self.output + '-'

    self.output= self.output + '\n'

    for num in self.nums:
      self.output = "{}{} |".format(self.output, num)
      for x in range(self.number + 1):
        try:
          self.output = "{} {}".format(self.output, self.ops[self.operation](num, x))
        except ZeroDivisionError:
          self.output = "{} Na".format(self.output)

      self.output = self.output + "\n"

    self.outputText.configure(state='normal')
    self.outputText.delete('1.0', tk.END)
    self.outputText.insert('end', self.output)
    self.outputText.configure(state='disabled')

  def checkOperation(self, operation):
    if not operation in ['+', '-', '/', '*']:
      return False

    return True

  def checkNum(self, num):
    try:
      num = int(num)
    except:
      return False
    if num < 0:
      return False
    return True


w = Window()
w.loop()
