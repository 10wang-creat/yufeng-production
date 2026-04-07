# -*- coding: utf-8 -*-
"""修正 index.html 的月份選擇器問題"""
import os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

# 1. 計件篩選：把 <input type="month"> 改成 <select>
old1 = '<label>月份:</label><input type="month" id="pw-filter-month" onchange="filterWork()">'
new1 = '<label>月份:</label><select id="pw-filter-month" onchange="filterWork()"><option value="">全部月份</option></select>'
if old1 in html:
    html = html.replace(old1, new1)
    changes += 1
    print("✅ 已修正：計件篩選月份")
else:
    print("ℹ️ 計件篩選月份：已是新版或格式不同")

# 2. 月報表：把 <input type="month"> 改成 <select>
old2 = '<div class="form-group"><label>選擇月份</label><input type="month" id="rpt-month"></div>'
new2 = '<div class="form-group"><label>選擇月份</label><select id="rpt-month"><option value="">-- 請選擇 --</option></select></div>'
if old2 in html:
    html = html.replace(old2, new2)
    changes += 1
    print("✅ 已修正：月報表月份選擇器")
else:
    print("ℹ️ 月報表月份選擇器：已是新版或格式不同")

# 3. 加入自動填充月份下拉選單的初始化函數
old3 = '// ====== INIT ======\nrenderDashboard();'
new3 = '''// ====== INIT ======
function populateMonthSelects() {
  const yms = new Set();
  DB.workRecords.forEach(r=>{
    if(r.d && r.d.startsWith('20')) yms.add(r.d.substring(0,7));
  });
  const sorted = [...yms].sort().reverse();
  ['pw-filter-month','rpt-month'].forEach(id=>{
    const sel = document.getElementById(id);
    if(!sel) return;
    const firstOpt = sel.options[0];
    sel.innerHTML = '';
    sel.add(firstOpt);
    sorted.forEach(ym=>{
      const [y,m] = ym.split('-');
      sel.add(new Option(y+'年'+parseInt(m)+'月', ym));
    });
  });
}
populateMonthSelects();
renderDashboard();'''

if old3 in html:
    html = html.replace(old3, new3)
    changes += 1
    print("✅ 已加入：月份下拉選單自動填充")
else:
    print("ℹ️ 初始化區塊：已是新版或格式不同")

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n共修改 {changes} 處")
print(f"檔案大小: {os.path.getsize(path)//1024}KB")
print("\n✅ index.html 已更新完成！")
