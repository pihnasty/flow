class A:

    def method_a(self):
        c = self.method_b(2)
        print(c)

    def method_b(self, b):
        return b * b


if __name__ == "__main__":
    A().method_a()
