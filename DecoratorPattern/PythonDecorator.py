def condiment(bev):
    def cost():
        return .20 + bev()

    return cost


@condiment
def beverage():
    return 1.99


if __name__ == '__main__':
    print(beverage())
