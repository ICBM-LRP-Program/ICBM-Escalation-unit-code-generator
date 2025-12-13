## 反馈体验 2025-12-13 #2
仍然存在相当影响体验的问题

#### 你现在需要完善……（按照顺序）
- 当窗口的高小于一定值时，最下面的”清除“”默认“”生成“按钮会被挤没，你需要修改布局，使按钮区域空间固定。
- 大多数字符串的输出格式不是这样，具体请看我解析。
- 武器面板的操作逻辑存在相当大的问题，具体请看我解析。
- 填充默认值时没有清除所有的输入框和表格内容，你需要清除默认。
- 修改器的表格不应该有Value选项。
- 音频编码还应该新增一个音量控制选项，具体请看我解析。

完成这些后，你需要和我沟通，然后进一步修改

#### 单位代码结构示例

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
        
        FixedRotationAngle true
        AttackerInPlanner Yes
        HiddenFromAllies Yes
        AttackIfDestroyed Yes
        CanAccessGlobalStorage No
        AlwaysVisibleOnEnemyTerritory No

        Produces "TestUnit1"
        Produces "TestUnit2"

        CanCarryUnit "TestUnit3"
        CanCarryUnit "TestUnit4"

        Airway Launch 1 Time 180
        Airway Launch 1 Time 90
        CanHostAircrafts "TestHelicopter" 2 Patrol 2 AIAutoPatrol	
        CanHostAircrafts Airway 2 "TestHeli2" 2 Patrol 2 AIAutoPatrol	

        Config "ConfigExample2" Default
            Weapon "TestWeapon1" 1 Time 600
        Config "ConfigExample2" Default 
            Weapon "TestWeapon2" 1 Time 600

        Radar "TestRadar"

        Modifier "BM_Accuracy_Damage_Penalty" 

        ImprovedBy "T_Tech1" AttackDelay 0.35
        ImprovedBy "T_Tech2" Set Size 0.99

请确保语序正确，你必须按照这个模板单位制作默认按钮的填充值。

#### 音量控制
其中，`Sound 137 Volume 0.5`后面的Volume是指新增的音量控制控制。如果留空，那么便代表着默认为1。

        Airway Launch 1 Time 180
        Airway Launch 1 Time 90
        CanHostAircrafts "TestHelicopter" 2 Patrol 2 AIAutoPatrol	
        CanHostAircrafts Airway 2 "TestHeli2" 2 Patrol 2 AIAutoPatrol

#### 子单位语法
`Airway`的编号由其顺序决定，例如"TestHeli2"引用的就是第二个Airway，即Airway 2。如果没有指定Airway，就像"TestHelicopter"一样，那么就默认为Airway 1。


#### 武器面板
删除现有的面板，添加两个纵列，左为配置，右为武器。
在配置表格，包含配置名称输入框、默认启用复选框、全部武器可用时才启用复选框。当选中配置时，显示所选配置的武器内容。同时提供一个"无配置"配置，它不允许被移动也不允许被删除。
在武器表格，包含武器名称输入框、武器数量输入框、发射数量输入框（无则留空）、发射时间输入框（无则留空）、自动交战复选框、显示备弹复选框、默认关闭复选框。


