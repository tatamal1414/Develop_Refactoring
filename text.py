def print_text(str1, num1_weight, num2_height):
    str1 = "あいうえお"
    num1 = 123456
    if not 5 <= len(str1) <=10:
        raise Exception('5文字以下もしくは10文字以上です')
    if not(str1.isalpha() and str1.isascii()):
        raise Exception('アルファベット(a~z,A~Z)で入力してください')



