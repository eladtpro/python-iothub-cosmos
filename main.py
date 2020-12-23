from models.configuration import Configuration
from simulateddevice import run
from hublistener import listen

def main():
    config = Configuration()
    #run(config)
    listen(config)
if __name__ == '__main__':
    main()
