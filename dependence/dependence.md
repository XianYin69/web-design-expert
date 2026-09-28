# dependence（依赖声明）

声明本技能包依赖的技能包/软件/仓库地址：每行一条 `名称 | 类型 | 来源`，类型为 skill|software|repo。

```
Skill_Generator | skill | local:Skill_Generator
web-design-guidelines | skill | local:web-design-guidelines
ui-design | skill | local:ui-design
frontend-dev | skill | local:frontend-dev
python | software | >=3.9（脚本仅用标准库）
chromium-devtools | software | npm:puppeteer / 浏览器自带 DevTools
axe-core | software | npm:axe-core（可选·读屏与规则复核）
WCAG2-quickref | repo | https://www.w3.org/WAI/WCAG22/quickref/
MDN-CSS-layout | repo | https://developer.mozilla.org
```

## 说明

- `local:` 为同机相邻技能：本技能只做**判断与建议**，实现由 `frontend-dev`/`ui-design` 承接，
  规范合规扫描可与 `web-design-guidelines` 互为补充，不互相覆盖目录。
- 脚本 `contrast_check.py` / `a11y_probe.py` / `design_review.py` 零第三方依赖，离线可跑。
- 联网取证（W3C/MDN）需 SMS 网络授权；未授权时按 [证据约束](../resistance/证据约束/证据约束.md) 降级。

SMS 包管理器安装技能包时，本目录条目与技能包本体接受同样的检查与净化（trust 标注·未审/隔离拒装·
仓库下载须网络授权·见 skill_manage_system pkg_deps.py），审过后方可下载安装执行。
