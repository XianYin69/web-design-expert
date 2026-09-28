# dependence（依赖声明）

声明本技能包依赖的技能包/软件/仓库地址：每行一条 `名称 | 类型 | 来源`，类型为 skill|software|repo。

```
Skill_Generator | skill | local:Skill_Generator
file_ops | skill | local:skill_manage_system
web-design-guidelines | skill | local:web-design-guidelines
ui-design | skill | local:ui-design
frontend-dev | skill | local:frontend-dev
code-guidelines | skill | local:code-guidelines
pavedpath-code | skill | local:pavedpath-code
python | software | system:>=3.9（脚本仅用标准库）
git | software | system:git（版本工作流）
chromium-devtools | software | npm:puppeteer / 浏览器自带 DevTools
axe-core | software | npm:axe-core（可选·读屏与规则复核）
WCAG2-quickref | repo | https://www.w3.org/WAI/WCAG22/quickref/
MDN-CSS-layout | repo | https://developer.mozilla.org
```

## 用途映射

| 依赖 | 承担 | 触发节点 |
|---|---|---|
| `file_ops` | 联网搜索/抓取（`ff_lite.py search/fetch`，须 `:grant network`） | 经验查询 / 浏览器学习 / 知识库构建 |
| `code-guidelines` · `pavedpath-code` | 落地规范互补（本技能只诊断不改码） | 改进清单 / 复审确认 |
| `web-design-guidelines` · `ui-design` · `frontend-dev` | 规范扫描互补与实现承接 | 领域路由 / 收尾沉淀 |
| `python` · `git` | 脚本运行与版本工作流 | 全程 |

## 说明

- 薄技能声明：本技能**只传意图＋参数**给依赖技能，由其自行读取自身 SKILL.md 执行，
  不在本目录内嵌依赖正文（避免副本漂移·见 [评审边界约束](../resistance/评审边界约束/评审边界约束.md)）。
- `local:` 为同机相邻技能：本技能只做**判断与建议**，实现由 `frontend-dev`/`ui-design` 承接，
  规范合规扫描可与 `web-design-guidelines` 互为补充，不互相覆盖目录。
- 脚本 `contrast_check.py` / `a11y_probe.py` / `design_review.py` 零第三方依赖，离线可跑。
- 联网取证（W3C/MDN/豆瓣/知乎）经 `file_ops` 的 `ff_lite.py`；未授权时按
  [证据约束](../resistance/证据约束/证据约束.md) 降级，境外不可达站点标 `[本地]` 不臆造 URL。

SMS 包管理器安装技能包时，本目录条目与技能包本体接受同样的检查与净化（trust 标注·未审/隔离拒装·
仓库下载须网络授权·见 skill_manage_system pkg_deps.py），审过后方可下载安装执行。
