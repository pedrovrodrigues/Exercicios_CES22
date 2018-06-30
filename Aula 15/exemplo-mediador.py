class Mediator:
    def __init__(self):
        self._colleague_1 = Colleague1(self)
        self._colleague_2 = Colleague2(self)
        self._colleague_3 = Colleague3(self)
    def tell_all(self, info, sender):
        if(sender == "colleague1"):
            print("Hey colleagues 2 and 3, "+sender+" says \""+info+"\"!")
        if(sender == "colleague2"):
            print("Hey colleagues 1 and 3, "+sender+" says \""+info+"\"!")
        if(sender == "colleague3"):
            print("Hey colleagues 2 and 1, "+sender+" says \""+info+"\"!")

class Colleague:
    def __init__(self, mediator):
      self._mediator = mediator
    def repass_info(self, info):
        pass

class Colleague1(Colleague):
     def repass_info(self, info):
        self._mediator.tell_all(info, "colleague1")

class Colleague2(Colleague):
    def repass_info(self, info):
        self._mediator.tell_all(info, "colleague2")

class Colleague3(Colleague):
    def repass_info(self, info):
        self._mediator.tell_all(info, "colleague3")

def main():
    med = Mediator()
    col1 = med._colleague_1
    col2 = med._colleague_2
    col3 = med._colleague_3
    col1.repass_info("Hi I'm 1!")
    col2.repass_info("Hi I'm 2!")
    col3.repass_info("Hi I'm 3!")

if __name__ == "__main__":
    main()