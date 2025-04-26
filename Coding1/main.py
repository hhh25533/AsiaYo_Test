def find_most_frequent_word(filename):
    # 建立一個dic 來儲存單字和次數
    word_count = {}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # 讀取檔案內容並轉換為小寫
            content = file.read().lower()

            # 分割成單字
            words = content.split()

            # 計算每個單字出現的次數
            for word in words:
                # 移除標點符號
                word = word.strip('.,!?()[]{}":;')
                if word:
                    # 搜尋單字是否在字典中，若不在則初始化為 0
                    word_count[word] = word_count.get(word, 0) + 1

            # 找出出現最多次的單字
            if word_count:
                # 使用 max 和 lambda 表達式來找出出現次數最多的單字
                most_frequent = max(word_count.items(), key=lambda x: x[1])
                # 同時 return 出現次數最多的單字和它的計數
                return most_frequent[0], most_frequent[1]
            else:
                return None, 0

    except FileNotFoundError:
        print(f"Error：file not found '{filename}'")
        return None, 0


# 執行程式
word, count = find_most_frequent_word('words.txt')
if word:
    print(f"{count} '{word}'")
else:
    print("Not Found")