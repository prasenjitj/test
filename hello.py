
class Hello:
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        print "Hello %s !" %self.name

def main():
    hello =  Hello("prasenjit");
    hello.sayHello()

if __name__ == '__main__':
    main()
