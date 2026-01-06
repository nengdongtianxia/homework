#导入os模块（检查文件是否存在...）
import os
#定义函数
def add_member():
#告知用户当前进入成员信息录入功能
    print("成员信息录入")
    while True:
#获取用户输入的姓名，strip去除首尾输入的空格
        name=input("姓名:").strip()
        if name:
            break
        print("错误")
    while True:
        character=input("角色:").strip()
        if character:
            break
        print("错误")
    while True:
        skill=input("技能:").strip()
        if skill:
            break
        print("错误")
    while True:
        label=input("标签:").strip()
        if label:
            break
        print("错误")
    while True:
        phone=input("电话:").strip()
        if phone:
            break
        print("错误")
    while True:
        date=input("加入日期:").strip()
        if date:
            break
        print("错误")
#拼接用户输入内容，\n表换行
    team_data=f"{name}/{character}/{skill}/{label}/{phone}/{date}\n"
#定义要保存信息的文件路径和文件名
    file_path="team_data.txt"
#以"a"模式打开文件，指定编码为utf-8，避免中文乱码
    with open("team_data.txt","a",encoding="utf-8")as f:
#判断文件是否不存在，或者文件存在但大小为0
        if not os.path.exists("team_data.txt")or os.path.getsize("team_data.txt")==0:
#若满足条件，先向文件写入表头信息
            f.write("姓名/角色/技能/标签/电话/加入日期\n")
#将拼好的成员信息写入文件
            f.write(team_data)
    print(f"已成功录入")
#调用函数
add_member()
#定义函数
def search_member():
#提示用户进入查询功能
    print("\n成员信息查询")
#循环获取查询关键词，确保输入不不为空
    while True:
        keyword=input("请输入关键词(姓名/技能").strip()
        if keyword:
            break
        print("错误，请重新输入")
#定义文件路径
    file_path="team_data.txt"
#检查文件是否存在，若不存在，提示用户先录入信息
    if not os.path.exists(file_path):
        print("无")
#直接结束当前函数
        return
#默认状态下未找到
    found = False
#以只读模式打开文件，指定编码为utf-8
    with open(file_path,"r",encoding="utf-8") as f:
#跳过文件的第一行（表头信息）
        next(f)
#逐行读取文件内容
        for line in f:
#去除每行首尾的空白字符
            line = line.strip()
#若当前行是空行，则跳过
            if not line:
                continue
#将关键词和行内容都转为小写，实现不区分大小写
            if keyword.lower() in line.lower():
#按/分割行内容
                name,character,skill,label,phone,date = line.split("/")
#输出分隔线，美化显示
                print("-" * 30)
#输出成员信息
                print(f"姓名:{name}")
                print(f"角色:{character}")
                print(f"技能:{skill}")
                print(f"标签:{label}")
                print(f"电话:{phone}")
                print(f"加入日期:{date}")
#输出结束分隔线
                print("-" * 30)
#标记为已找到
                found = True
#若未找到匹配内容，输出未找到
            if not found:
                print(f"未找到")
#调用函数
