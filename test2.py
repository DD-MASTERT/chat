from chat.kimi import kimisend_and_update
from chat.kimi import kimiclick_create_text_element
from chat.kimi import kimitalk

#kimi的cookie是动态的，我能力有限，只能每次打开都手动登录了，也不能无头模式聊天了

def test(driver):

    while True:
        try:
            # 获取用户输入
            message = input("请输入消息（输入'退出'结束程序）: ")

            if message == "退出":
                print("程序结束。")
                break  # 退出循环

            if message == "新建对话":
                kimiclick_create_text_element(driver)
                continue  # 跳过循环的剩余部分，直接回到循环的开始
            
            # 调用 send_and_update 函数
            element_text = kimisend_and_update(driver, message)
            
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

driver = kimitalk()
test(driver)