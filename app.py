"""
    レストラン検索APIを使って
    「freeword検索」←入力として受け取る
        ↓
    次の形式で必要な情報を出力する
    「
        吉野家,URL,〇〇線〇〇駅徒歩〇〇分
        すき家,URL,〇〇線〇〇駅徒歩〇〇分
"""
import requests
import os


def main():
    search_word = input('フリーワード検索: ')
    #search_word = '牛丼'

    res_dic = search_freeword(search_word)

    rest_list = get_csv_list(res_dic)

    display_csv_list(rest_list)


def display_csv_list(rest_list):
    for data in rest_list:
        print(data)


def search_freeword(search_word):
    key_id = os.environ['KEY_ID']
    api_url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
    url_str = f'{api_url}?keyid={key_id}&freeword={search_word}'
    response = requests.get(url_str)
    res_dic = response.json()
    return res_dic


def get_csv_list(res_dic):
    rest_list = []
    for rest_dic in res_dic['rest']:
        access_dic = rest_dic['access']
        access_str = f'{access_dic["line"]} {access_dic["station"]} 徒歩{access_dic["walk"]}分'
        csv_str = f'{rest_dic["name"]},{rest_dic["url"]},{access_str}'
        rest_list.append(csv_str)
    return rest_list


if __name__ == '__main__':
    main()

