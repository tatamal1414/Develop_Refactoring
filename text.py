def print_text(str1, num1_weight, num2_height):
    """_summary_
    文字列と数値２つの引数をとり、以下のチェックを行い文字列を返却する関数

    5文字以上10文字以下でなければエラーメッセージを表示(例外を発生させてもよい)
    アルファベット(a～z, A～Z)以外が使われていればエラーメッセージを表示(例外を発生させてもよい)



    Args:
        str1 (string): 5文字以上10文字以内のアルファベット
        num1_weight (int): 横に繰り返す数値
        num2_height (int): 縦に繰り返す数値

    Raises:
        Exception: _description_
        Exception: _description_
    """
    str1 = "あいうえお"
    num1_weight = 123456
    num2_height = 12345678
    if not 5 <= len(str1) <=10:
        raise Exception('5文字以下もしくは10文字以上です')
    if not(str1.isalpha() and str1.isascii()):
        raise Exception('アルファベット(a~z,A~Z)で入力してください')
    #TODO:エラー文以外の結果を出力したい


