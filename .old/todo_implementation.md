# ICBM单位代码生成器修改任务

## 任务目标
按照用户要求修正NewCode.py文件

## 执行步骤

### 第1步：删除整个武器面板
- [ ] 找到并删除CreateWeaponTab方法
- [ ] 从Notebook中移除武器配置标签页
- [ ] 删除所有武器相关的变量和数据结构
- [ ] 保留其他所有功能不变

### 第2步：为音频添加Volume控制
- [ ] 在基础数据组中新增Volume输入框
- [ ] 设置默认值为1
- [ ] 修改Sound字段输出逻辑，添加Volume参数

### 第3步：修正输出格式
- [ ] 修正字段顺序（Tech, Movie, AbstractMovie, Model, Icon, Type, Class, DrawSize, AbstractDrawSize, Sound）
- [ ] 修正字段名（TurnSpeed → TrunSpeed, SelfDestruct → SelfDestructTime）
- [ ] 修正属性数据输出顺序
- [ ] 修正子单位配置语法
- [ ] 修正其他所有BuildXxxCode方法

## 重要原则
- 每步完成后立即测试
- 严格按顺序执行，不跳跃
- 保持现有功能不被破坏
- 布尔值保持Yes/No格式
