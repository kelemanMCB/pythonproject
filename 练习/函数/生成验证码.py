# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random


def yanzhengma():
    all_chars = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    len_ma = 4
    code = ""

    for x in range(len_ma):
        index = random.randint(0, len(all_chars)-1)
        code = code + all_chars[index]

    return code

if __name__ == "__main__":
    print(yanzhengma())