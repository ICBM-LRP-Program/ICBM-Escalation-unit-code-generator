# 反馈完善任务清单 (2025-12-13 #2)

## 已完成 ✅
- [x] 分析任务需求和文件结构
- [x] 创建详细的待办事项清单
- [x] 修复武器配置关联表格缺少按钮的问题
- [x] 添加武器配置关联表格的按钮对应方法
- [x] 修复了MoveAssocUp方法
- [x] 修复了MoveAssocDown方法
- [x] 修复了ClearAllAssociations方法
- [x] 修复了LoadAssociation方法
- [x] 修复了SaveAssociation方法
- [x] 测试程序是否能正常运行
- [x] 修复武器配置面板中的武器关联验证逻辑
- [x] 修复响应式布局（窗口可调整大小）
- [x] 修复语言切换功能（实时更新界面文本）

## 待完成 🔄

### 1. 修复按钮区域布局
- [ ] 将底部按钮区域设置为固定高度
- [ ] 防止窗口高度不足时按钮被隐藏
- [ ] 使用PanedWindow或Frame来分隔主内容和按钮区域

### 2. 修正代码生成格式
- [ ] 按照反馈中的模板修正代码输出格式
- [ ] 确保字段顺序正确
- [ ] 修正各种数据类型和格式：
  - Sound字段添加Volume控制
  - 修正行为控制字段输出
  - 修正子单位配置语法
  - 修正武器配置输出格式

### 3. 重新设计武器面板
- [ ] 删除现有的复杂武器面板
- [ ] 创建简单的双列布局（配置列 + 武器列）
- [ ] 配置列：配置名称、Default复选框、OnlyFull复选框
- [ ] 武器列：武器名称、数量、Launch、Time、AutoEngage、Principal、DefaultOff
- [ ] 实现配置与武器的关联逻辑

### 4. 新增音量控制
- [ ] 在基础数据组中添加Volume输入框
- [ ] 修正Sound字段生成格式：`Sound 137 Volume 0.5`
- [ ] 默认为1，不输出Volume字段

### 5. 修正修改器表格
- [ ] 删除Value列
- [ ] 只保留修改器名称列

### 6. 修正默认值填充逻辑
- [ ] 修改FillDefault方法，清除所有表格内容
- [ ] 填充符合模板的默认值
- [ ] 确保所有字段都有合理的默认值

### 7. 修正子单位语法
- [ ] 实现Airway编号引用系统
- [ ] CanHostAircrafts语法：`CanHostAircrafts "UnitName" Count [Airway N] Patrol N AIAutoPatrol`

### 8. 修正代码结构
按照反馈模板：
```
[UNIT] "TestUnit"
    Tech "U_TestUnit"
    Movie "Units/Images/[Type]/Topdown/Example.midx"
    AbstractMovie "Units/Images/[Type]/Abstract/Example.midx"
    Model "Units/Images/[Type]/Example.midx"
    Icon "Units/Images/Icons/[Type]/Example.png"
    Type Ground
    Class "UC_Ground"
    DrawSize 20
    AbstractDrawSize 35
    Sound 137 Volume 0.5
    
    Power 225
    Speed 100
    TrunSpeed 30
    Size 0.2
    SelfDestructTime 20
    HangarMaxLoad 3
```

## 技术要点
- 使用PanedWindow分隔主界面和按钮区域
- 重新设计武器配置的数据结构和UI
- 修正所有BuildXxxCode方法的输出格式
- 添加Volume字段处理
- 修正默认值模板

## 测试验证
- [ ] 测试窗口缩放时按钮区域保持可见
- [ ] 测试代码生成格式符合模板
- [ ] 测试武器面板操作流程
- [ ] 测试音量控制功能
- [ ] 测试修改器表格
- [ ] 测试默认值填充
