class Queue:
    def __init__(self, size = 5):
        self.queue = []
        self.size = size
        self.front = 0
        self.rear = 0
    
    def add(self, data):
        if data not in self.queue:
            if self.rear < self.size:
                self.queue.append(data)
                self.rear += 1
                print("큐에 {}를(을) 추가합니다.".format(data))
            else:
                print("큐가 가득차서 {}를(을) 추가할 수 없습니다.".format(data))
        else:
            print("{}는(은) 중복된 데이터입니다.".format(data))
        #self.list()

    def remove(self):
        if self.rear <= 0 or self.rear == self.front:
            print("큐에 저장된 데이터가 없습니다.", end = "")
        else:
            print("출력된 데이터 : {}".format(self.queue[self.front]))
            self.queue[self.front] = ""
            self.front += 1;
            #self.list()

    def list(self):
        print("=============================================================")
        print("큐에 저장된 데이터 : ", end = "")
        if self.rear <= 0 or self.rear == self.front:
            print("큐에 저장된 데이터가 없습니다.", end = "")
        else:
            for i in range(len(self.queue)):
                if i > self.front:
                    print(", ", end = "")
                print(self.queue[i], end = "")
        print("\n=============================================================")

if __name__ == "__main__":
    queue = Queue();
    menu = 0
    while True:
        while True:
            print("======================================")
            print("  1.입력  2.출력  3.목록보기  4.종료  ")
            print("======================================")
            menu = int(input("원하는 메뉴를 선택하세요 : "))
            if menu >= 1 and menu <= 4:
                break
            print("메뉴는 1 ~ 4만 선택할 수 있습니다.")
        #=================================================

        if menu == 1:
            data = input("큐에 저장할 데이터 : ")
            queue.add(data)
        elif menu == 2:
            queue.remove()
        elif menu == 3:
            queue.list();
        elif menu == 4:
            break
    #====================================================
    print("프로그램을 종료합니다.")

