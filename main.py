#导入自定义的utils模块
import utils
#定义函数
def main():
  print("===欢迎使用团队管理系统===")
  while True:
#打印空行
    print("\n---功能菜单---")
#打印功能选项
    print("1.录入成员")
    print("2.查询成员")
    print("3.技能统计")
    print("0.退出系统")
#使用try-except捕获用户输入和功能执行中的异常
    try:
#获取用户的功能选择
        choice=input("\n请输入你的选择: ")
        if choice == "1":
            utils.add_member()
        elif choice == "2":
            utils.search_member()
        elif choice == "3":
            utils.analyze_skills()
        elif choice == "0":
            print("再见")
#跳出循环
            break
        else:
            print("输入有误，请重新输入！")
#捕获所有未预期的异常，避免程序崩溃
    except Exception as e:
        print(f"程序出现异常，请重新操作")
#程序入口判断：当该脚本作为主程序运行时，执行main函数
if __name__=="__main__":
    main()
    
