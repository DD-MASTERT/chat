from chat.utils import talk
from chat.utils import click_create_text_element
from chat.utils import send_and_update



OPTIONS = True  
#是否开启无头模式，即不打开网页，或者 False打开网页

TOKEN = ''

#这个是你自己本地谷歌浏览器保存的token，是长期的。过期需要重新登录获得。


def test(driver):

    while True:
        try:
            # 获取用户输入
            message = input("请输入消息（输入'退出'结束程序）: ")

            if message == "退出":
                print("程序结束。")
                break  # 退出循环

            if message == "新建对话":
                click_create_text_element(driver)
                continue  # 跳过循环的剩余部分，直接回到循环的开始
            
            # 调用 send_and_update 函数
            element_text = send_and_update(driver, message)
            
            # 打印返回的清洗后的元素文本
            if element_text:  # 检查 element_text 是否为 None 或其他无效值
                print(element_text)
                message = "" 

        except Exception as e:
            print(f"发生错误：{e}")
            driver.quit()  # 发生异常时关闭浏览器
            break  # 退出循环

    # 如果程序正常结束循环，也关闭浏览器
    driver.quit()

driver = talk(OPTIONS, TOKEN)
test(driver)
