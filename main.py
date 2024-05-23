from env import WebDino
from DQ_train import createNetwork


if __name__ == '__main__':

    model = createNetwork()
    WebDino().train()