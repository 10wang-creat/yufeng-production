# -*- coding: utf-8 -*-
"""
準備 GitHub Pages 部署檔案
將 HTML 應用複製為 index.html（GitHub Pages 預設入口）
"""
import shutil
import os

# 來源：你之前從 Claude 下載的 HTML 檔案
# 請確認路徑正確，可能在「下載」資料夾
possible_sources = [
    os.path.expanduser(r"~\Downloads\yufeng_app.html"),
    os.path.expanduser(r"~\Downloads\昱鋒生產管理系統.html"),
    os.path.expanduser(r"~\Desktop\yufeng_app.html"),
    os.path.expanduser(r"~\Desktop\昱鋒生產管理系統.html"),
    # 也檢查 OneDrive 桌面
    os.path.expanduser(r"~\OneDrive\桌面\yufeng_app.html"),
    os.path.expanduser(r"~\OneDrive\桌面\昱鋒生產管理系統.html"),
]

dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

copied = False
for src in possible_sources:
    if os.path.exists(src):
        shutil.copy2(src, dest)
        size = os.path.getsize(dest)
        print(f"✅ 已複製: {src}")
        print(f"   → {dest} ({size//1024}KB)")
        copied = True
        break

if not copied:
    print("❌ 找不到 HTML 檔案！")
    print("   請手動將下載的 HTML 檔案複製到此資料夾，並重命名為 index.html")
    print(f"   目標路徑: {dest}")
    print()
    print("   或者輸入檔案路徑:")
    path = input("   > ").strip().strip('"')
    if os.path.exists(path):
        shutil.copy2(path, dest)
        print(f"✅ 已複製: {path} → {dest}")
    else:
        print(f"❌ 路徑不存在: {path}")

print()
print("=" * 50)
print("接下來執行以下 Git 指令:")
print("=" * 50)
print()
print(f"  cd {os.path.dirname(os.path.abspath(__file__))}")
print("  git init")
print("  git add .")
print('  git commit -m "初始版本：昱鋒生產管理系統"')
print("  git branch -M main")
print("  git remote add origin https://github.com/你的帳號/yufeng-production.git")
print("  git push -u origin main")
print()
print("推上去後，到 GitHub repo → Settings → Pages → Source 選 main branch")
print("等幾分鐘後就能用 https://你的帳號.github.io/yufeng-production/ 存取了")
