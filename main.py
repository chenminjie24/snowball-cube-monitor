import pysnowball as ball

if __name__ == '__main__':
    ball.set_token("xq_a_token=cd82cf959785ada23a18243e5863b61ff4e950fb")
    print(ball.rebalancing_history("ZH3334492", 2, 1))