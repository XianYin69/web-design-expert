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

## 0.1.1 — 浏览器学习节点 + file_ops 依赖 + 书目联网确证（Skill_Generator 修改路径）

- 依赖：`dependence/dependence.md` 追加薄技能声明 `file_ops | skill | local:skill_manage_system`
  （承担联网搜索/抓取 `ff_lite.py search/fetch`，须 `:grant network`；触发节点＝经验查询/浏览器学习/知识库构建），
  并声明 `code-guidelines`、`pavedpath-code` 为 `skill|local`，`python`、`git` 为 `software|system`；
  新增「用途映射」表，规则表述保留「只传意图＋参数、不内嵌正文」。
- 流程：新建横切节点 `branch/流程/浏览器学习/浏览器学习.md`（触发＝使用本技能遇到不明白的
  UI/前端/无障碍/设计规范问题，强制先派 `file_ops` 检索学习并给出出处再作答；含中国大陆可达性策略），
  `流程.md` 增「横切节点」段与步骤行。
- 约束：新建 `resistance/浏览器学习约束/浏览器学习约束.md`（必须/禁止/兜底/违规后果），
  `resistance.md` 目录清单同步。
- 知识库：新建 `knowledge/参考书目/参考书目.md`，14 条书目/规范条目经豆瓣读书、w3.org、MDN 逐条 HTTP 实测确证
  标 `[联网]`＋可溯 URL，2 条不可达标 `[本地]`；`knowledge.md` 增「确证标记」段并挂入入口组。
- SKILL.md：工作原则新增「不懂先联网」、执行路径标注横切触发、可用工具表新增 `check_links.py`，
  红线补「不得臆造 URL／书名／条款号」；全文保持 50 行。
- 脚本：新增 `scripts/check_links.py`（适配自 cpp-expert 同名脚本）——悬空链接校验＋≤50 行检查＋
  `[联网]`/`[本地]` 计数；本次输出：悬空链接数 = 0、超长文件数 = 0；书目叶确证 15 条已联网、3 条未确证。
- 勘误：`CSS揭秘` 作者为 Lea Verou（非 Ana Tudor），已在书目条目注明。
- 违反后果：跳过检索＝结论无据；臆造 URL＝知识库污染；不可达即否定＝漏判真规范。
