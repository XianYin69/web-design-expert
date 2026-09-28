# CHANGELOG

## 1.0.0 — web-design-expert 初版（Skill_Generator 创建路径产出）

- 流程：初始化→需求确认→领域路由→证据采集→专家诊断→改进清单→复审确认→收尾沉淀（8 节点）。
- 知识库：六组 16 叶（骨架／视觉语言／行为／合规／性能／表达）＋索引，互引闭合，判定不可再拓扑。
- 脚本：`contrast_check.py`（WCAG 对比度实算）、`a11y_probe.py`（静态异味扫）、
  `design_review.py`（发现项排序归并出报告）；均标准库实现、≤50 行、英文命名。
- 约束：评审边界（只诊断不改码）、证据分级（实测/静态/推断/未实测）、优先级 P0–P3、
  知识更新（规范条款不改写）、五大机制用法。
- 资产：`asset/评审报告模板.md`、`asset/findings_example.json`。
- 依赖：`dependence/dependence.md` 声明相邻技能分工（web-design-guidelines / ui-design /
  frontend-dev 只互补不覆盖）与可选工具（axe-core、DevTools）。
- 来源留痕：W3C、MDN 抓取与 provenance 存 tmp/downloads，不入库。
- 违反后果：越权改码＝破坏调用方职责；无证据判定＝结论不可信；条款改写＝合规基线漂移。
