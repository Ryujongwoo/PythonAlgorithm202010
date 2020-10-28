class Stack:
    def __init__(self, size = 5):
        self.stack = []
        self.size = size
        self.top = 0

    def push(self, data):
        if data not in self.stack:
            if self.size > self.top:
                self.stack.append(data)
                self.top += 1
                print("스택에 {}을(를) PUSH 합니다.".format(data))
            else:
                print("스택이 가득차서 {}을(를) PUSH 할 수 없습니다.".format(data))
        else:
            print("{}은(는) 중복된 데이터입니다.".format(data))
        self.list()

    def pop(self):
        if self.top <= 0:
            print("스택에 저장된 데이터가 없습니다.")
        else:
            print("POP 데이터 :", self.stack.pop())
            self.top -= 1;
            self.list()

    def list(self):
        print("=============================================================")
        print("스택에 저장된 데이터 : ", end = "")
        if self.top <= 0:
            print("스택에 저장된 데이터가 없습니다.", end = "")
        else:
            for i in range(len(self.stack)):
                if i > 0:
                    print(", ", end = "")
                print(self.stack[i], end = "")
        print("\n=============================================================")


if __name__ == "__main__":
    stack = Stack()
    #menu = 0
    while True:
        while True:
            print("=================================")
            print("  1.PUSH  2.POP  3.LIST  4.QUIT  ")
            print("=================================")
            menu = int(input("원하는 메뉴를 선택하세요 : "))
            if menu >= 1 and menu <= 4:
                break
            print("메뉴는 1 ~ 4만 선택할 수 있습니다.")
        #=================================================

        if menu == 1:
            data = input("스택에 저장할 데이터 : ")
            stack.push(data)
        elif menu == 2:
            stack.pop()
        elif menu == 3:
            stack.list();
        elif menu == 4:
            break
    #====================================================
    print("프로그램을 종료합니다.")























