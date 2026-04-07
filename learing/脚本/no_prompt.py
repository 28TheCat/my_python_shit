from getpass import getpass

try:
    p = getpass(prompt="")
except Exception as e:
    print(f"Error: {e}")
else:
    if p:
        print(f"密码获取成功，长度为: {len(p)}")
    else:
        print("未输入任何内容。")