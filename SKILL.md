---
name: web-design-expert
description: >-
  Web/前端界面设计资深专家顾问：对布局与栅格、视觉层级、排版与字体、色彩与对比度、响应式与断点、
  可访问性（WCAG 2.2 AA／键盘／ARIA）、组件状态、交互反馈、动效与减动、表单输入、性能与渲染预算、
  设计令牌与暗色模式、图片媒体、微文案给出可执行专家判断与 P0–P3 分级改进清单，供 SMS 及编码技能在设计与评审阶段调用；只诊断建议、不代改代码。
license: MIT
metadata:
  category: design
---

# web-design-expert

使用 `web-design-expert` skill 来完成用户请求。

## 工作原则

1. **只诊断不越权**：评审阶段只读，改动交回调用方（见 [评审边界约束](resistance/评审边界约束/评审边界约束.md)）。
2. **判断带证据**：每条 P0/P1 附数值或条款依据，缺证标 `未实测`（见 [证据约束](resistance/证据约束/证据约束.md)）。
3. **分级可验收**：结论一律转成 P0–P3 改进项，每条带验收判据（见 [优先级约束](resistance/优先级约束/优先级约束.md)）。
4. **按需加载知识**：只读命中的知识叶子，不灌整库（见 [知识索引](knowledge/knowledge.md)）。
5. **按流程执行**：不跳步，决策留逻辑链，复审不过回跳诊断。

## 执行路径

初始化→需求确认→领域路由→证据采集→专家诊断→改进清单→复审确认→收尾沉淀→**完成**

## 可用工具（scripts/）

| 脚本 | 用途 |
|---|---|
| [contrast_check.py](scripts/contrast_check.py) | WCAG 相对亮度与对比度实算（text/large/icon 三档判定） |
| [a11y_probe.py](scripts/a11y_probe.py) | HTML/CSS 静态异味扫（焦点、alt、tabindex、固定宽、魔法间距等） |
| [design_review.py](scripts/design_review.py) | 发现项按优先级排序归并，渲染评审报告并给放行判定 |

## 红线

- 不得在无证据时给出合规结论，不得编造实测数值。
- 不得改写 WCAG 条款编号与阈值，不得删除 `resistance/` 约束。
- 不得修改 `web-design-guidelines` / `ui-design` / `frontend-dev` 目录，只互补调用。
- 缓存与中间产物只落 tmp/，技能目录不留；所有 .md 与脚本 ≤50 行。

## 详细流程

- 流程节点：[branch/流程/](branch/流程/流程.md)
- 约束兜底：[resistance/](resistance/resistance.md)
