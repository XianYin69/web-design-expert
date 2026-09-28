# 键盘与 ARIA

## 键盘判据

- Tab 顺序＝视觉与逻辑顺序，无陷阱（模态内闭环、Esc 可退并归还焦点到触发元素）。
- 焦点可见：`- 焦点必须可见：`outline` 不得清零；自定义焦点环与相邻色对比 ≥3:1、厚度 ≥2px。
- 跳转链接（skip link）指向主内容；分页/表格支持方向键与 Home/End。
- 快捷键不得与浏览器/读屏键冲突；单字符快捷键需可关闭（2.1.4）。
- 正偏移 `tabindex`（>0）＝顺序污染，一律判 P1。

## ARIA 第一法则

能用原生语义标签就不用 ARIA；ARIA 只补语义、不改行为（加了 `role=button` 必须自己实现键盘与点击）。

| 检查 | 判据 |
|---|---|
| 角色合法 | 不在 `div` 上乱加 `button` 而不给键盘 |
| 必具有关 | `role=checkbox` 需 `aria-checked` |
| 名称来源 | `aria-label` 覆盖可见文本＝错误（2.5.3） |
| 活区 | 动态提示用 `aria-live=polite`，错误摘要用 assertive |
| 隐藏 | `aria-hidden=true` 的元素不得可聚焦 |
| 展开/选中 | 折叠、选项卡、菜单暴露 `aria-expanded/selected` |

## 相关

- [知识索引](../knowledge.md) · [可访问性WCAG](../可访问性WCAG/可访问性WCAG.md) · [组件状态](../组件状态/组件状态.md)
