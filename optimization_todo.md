# ICBM单位代码生成器优化任务清单

## 当前状态
- 开始时间: 2025-12-13 下午2:40
- 基于feedback-251213#2.md的优化需求
- 当前版本: NewCode.py (2025-12-13)

## 优化任务清单

### 阶段1: 界面布局优化
- [ ] 1.1 修改底部按钮区域为固定高度布局
- [ ] 1.2 调整主窗口布局结构，确保按钮始终可见
- [ ] 1.3 测试不同窗口尺寸下的显示效果

### 阶段2: 代码生成逻辑重构
- [ ] 2.1 重写BuildCodeString()方法，按照标准格式
- [ ] 2.2 修正基础信息字段输出语法和顺序
- [ ] 2.3 实现正确的行为控制字段格式 (true/Yes/No)
- [ ] 2.4 修正生产单位和搭载单位语法
- [ ] 2.5 实现正确的子单位语法 (Airway编号规则)
- [ ] 2.6 修正武器配置格式
- [ ] 2.7 修正雷达和修改器输出
- [ ] 2.8 修正升级项格式 (ImprovedBy语法)

### 阶段3: 格式化改进
- [ ] 3.1 在代码生成中添加板块间空行
- [ ] 3.2 确保代码结构清晰易读

### 阶段4: 武器面板重新设计
- [ ] 4.1 删除现有武器面板
- [ ] 4.2 创建左右双列布局 (配置 | 武器)
- [ ] 4.3 实现配置表格 (名称、Default、OnlyFull复选框)
- [ ] 4.4 实现武器表格 (名称、数量、Launch、Time、复选框)
- [ ] 4.5 添加"无配置"选项和锁定机制
- [ ] 4.6 修正武器关联操作逻辑

### 阶段5: 功能完善
- [ ] 5.1 新增音量控制输入框 (Sound Volume)
- [ ] 5.2 修改修改器表格，移除Value列
- [ ] 5.3 重写FillDefault()方法，确保完全清除旧数据
- [ ] 5.4 优化用户体验和错误提示

### 阶段6: 测试与验证
- [ ] 6.1 生成代码格式验证
- [ ] 6.2 界面响应性测试
- [ ] 6.3 功能完整性检查
- [ ] 6.4 与用户沟通确认

## 关键改进点

### 代码格式标准 (参考用户提供的模板)
```ini
[UNIT] "TestUnit"
    Tech "U_TestUnit"
    Movie "Units/Images/[Type]/Topdown/Example.midx"
    Sound 137 Volume 0.5

    Power 225
    Speed 100
    TrunSpeed 30

    FixedRotationAngle true
    AttackerInPlanner Yes
    HiddenFromAllies Yes

    Produces "TestUnit1"
    CanCarryUnit "TestUnit3"

    Airway Launch 1 Time 180
    CanHostAircrafts "TestHelicopter" 2 Patrol 2 AIAutoPatrol

    Config "ConfigExample" Default
        Weapon "TestWeapon1" 1 Time 600

    Radar "TestRadar"

    Modifier "BM_Accuracy_Damage_Penalty"

    ImprovedBy "T_Tech1" AttackDelay 0.35
```

### 武器面板新布局
- 左侧: 配置管理
  - 配置名称输入框
  - Default复选框
  - OnlyFull复选框
  - 锁定"无配置"选项
- 右侧: 武器管理
  - 武器名称、数量输入框
  - Launch、Time输入框
  - AutoEngage、Principal、DefaultOff复选框
